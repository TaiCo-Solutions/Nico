import xml
import base64
import xmltodict
import os
from XmlDocument import XmlDocument
from User import User


class XmlFinder():

    def __init__(self, text_message):
        self.current_user = User()
        self.current_user.get_user_data()
        self.text_message = text_message
        self.text_message.append(
            "\nIniciando búsqueda y clasificación de documentos electrónicos.")
        self.search_for_xml()

    def search_for_xml(self):
        folder_path = self.current_user.ubicacion
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)

        if os.path.isdir(folder_path):
            file_list = os.listdir(folder_path)
            total_files = len(file_list)
            self.text_message.append(f"Clasificando: {total_files} archivos.\nPor favor espere...")
            for file_name in file_list:
                file_path = os.path.join(folder_path, file_name)
                if ".xml" in file_name or ".XML" in file_name:
                    file_data = open(file_path, "r", encoding='utf-8')
                    file_data_str = file_data.read()
                    try:
                        file_data_str = file_data_str.encode('latin1')
                    except:
                        file_data_str = file_data_str.encode('utf-8')
                    file_data.close()
                    try:
                        xml_data = file_data_str.decode('cp1252')
                        if "<" not in xml_data:
                            xml_data = file_data_str.decode("ISO-8859-1")
                    except:
                        xml_data = file_data_str.decode("utf-8")

                    if self.explore_xml(xml_data):
                        os.remove(file_path)

                elif ".zip" in file_name or ".ZIP" in file_name or ".rar" in file_name or ".RAR" in file_name:
                    continue
                else:
                    os.remove(file_path)

    def extract_taxes(self, article_line, tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos):
        tax = float(article_line['Impuesto']['Monto'])
        try:
            tariff = float(article_line['Impuesto']['Tarifa'])
        except:
            tariff = -1

        if tariff == -1:
            otros_impuestos += tax
        elif tariff == 0:
            tarifa_0 += tax
        elif tariff == 1:
            tarifa_1 += tax
        elif tariff == 2:
            tarifa_2 += tax
        elif tariff == 4:
            tarifa_4 += tax
        elif tariff == 8:
            tarifa_8 += tax
        else:
            tarifa_13 += tax

        return tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos

    def explore_xml(self, xml_data):
        xml_response = base64.b64encode(xml_data.encode())
        if xml_data.find("<") >= 0:
            xml_data = xml_data[xml_data.find("<"):]
        xml_data = xml_data.replace("\r\n", "")
        xml_data = xml_data.replace("\n", "")
        if len(xml_data) > 0:
            xml_dictionary = xmltodict.parse(xml_data)
            if "<RespuestaHacienda" in xml_data:
                xml_dictionary = xml_dictionary["RespuestaHacienda"]

            if "<MensajeHacienda" in xml_data:
                xml_dictionary = xml_dictionary["MensajeHacienda"]
                if "NumeroCedulaEmisor" in xml_dictionary:
                    cedula = xml_dictionary["NumeroCedulaEmisor"]

                    if self.current_user.cedula not in cedula:
                        try:
                            clave = xml_dictionary["Clave"]
                        except:
                            clave = xml_dictionary["clave"]

                        try:
                            xml_respuesta = xml_dictionary["Mensaje"]
                        except:
                            xml_respuesta = '2'

                        try:
                            detalle_mensaje = xml_dictionary["DetalleMensaje"]
                        except:
                            detalle_mensaje = ""

                        electronic_doc = XmlDocument(clave=clave, respuesta_hacienda=xml_respuesta,
                                                     detalle_mensaje=detalle_mensaje, xml_respuesta=xml_response.decode('utf-8'))

                        if electronic_doc.verify_registered_edoc():
                            return electronic_doc.update_edoc_response()
                        else:
                            return electronic_doc.insert_edoc_response()
                return True

            else:
                documento_tipo = ""
                if "<NotaCreditoElectronica" in xml_data:
                    xml_dictionary = xml_dictionary["NotaCreditoElectronica"]
                    documento_tipo = "NotaCreditoElectronica"
                elif "<FacturaElectronica" in xml_data:
                    xml_dictionary = xml_dictionary["FacturaElectronica"]
                    documento_tipo = "FacturaElectronica"
                elif "<NotaDebitoElectronica" in xml_data:
                    xml_dictionary = xml_dictionary["NotaDebitoElectronica"]
                    documento_tipo = "NotaDebitoElectronica"
                elif "<TiqueteElectronico" in xml_data:
                    xml_dictionary = xml_dictionary["TiqueteElectronico"]
                    documento_tipo = "TiqueteElectronico"

                if len(documento_tipo) > 0:
                    proveedor = xml_dictionary['Emisor']['Nombre'].upper()
                    cedula = xml_dictionary['Emisor']['Identificacion']['Numero']
                    if not cedula == self.current_user.cedula:
                        try:
                            clave = xml_dictionary["Clave"]
                        except:
                            clave = xml_dictionary["clave"]

                        consecutivo = xml_dictionary['NumeroConsecutivo']
                        fecha = xml_dictionary['FechaEmision']
                        fecha = fecha[:fecha.find("T")]

                        tarifa_0 = 0
                        tarifa_1 = 0
                        tarifa_2 = 0
                        tarifa_13 = 0
                        tarifa_4 = 0
                        tarifa_8 = 0
                        otros_impuestos = 0

                        # Lines

                        if 'DetalleServicio' in xml_dictionary:
                            xml_line = xml_dictionary['DetalleServicio']
                            if 'LineaDetalle' in xml_line:
                                try:
                                    for article_line in xml_line['LineaDetalle']:
                                        if 'Impuesto' in article_line:
                                            tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos = self.extract_taxes(
                                                article_line, tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos)

                                except:
                                    if 'Impuesto' in xml_line['LineaDetalle']:
                                        tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos = self.extract_taxes(
                                            xml_line['LineaDetalle'], tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos)

                        # Currency

                        if "CodigoTipoMoneda" in xml_data:
                            moneda = xml_dictionary["ResumenFactura"]["CodigoTipoMoneda"]["CodigoMoneda"]
                        else:
                            moneda = ""

                        # Totals

                        if "TotalExento" in xml_data:
                            exento = xml_dictionary["ResumenFactura"]["TotalExento"]
                        else:
                            exento = 0
                        if "TotalExonerado" in xml_data:
                            exonerado = xml_dictionary["ResumenFactura"]["TotalExonerado"]
                        else:
                            exonerado = 0

                        if "TotalGravado" in xml_data:
                            gravado = xml_dictionary["ResumenFactura"]["TotalGravado"]
                        else:
                            gravado = 0

                        subtotal = xml_dictionary["ResumenFactura"]["TotalVenta"]

                        if "TotalDescuentos" in xml_data:
                            descuento = xml_dictionary["ResumenFactura"]["TotalDescuentos"]
                        else:
                            descuento = 0

                        if "TotalImpuesto" in xml_data:
                            impuesto = xml_dictionary["ResumenFactura"]["TotalImpuesto"]
                        else:
                            impuesto = 0

                        if "TotalOtrosCargos" in xml_data:
                            otros = xml_dictionary["ResumenFactura"]["TotalOtrosCargos"]
                        else:
                            otros = 0

                        total = xml_dictionary["ResumenFactura"]["TotalComprobante"]

                        electronic_doc = XmlDocument(proveedor=proveedor, cedula=cedula, documento_tipo=documento_tipo, clave=clave, consecutivo=consecutivo,
                                                     fecha=fecha, moneda=moneda, gravado=gravado, exento=exento, exonerado=exonerado, subtotal=subtotal, descuento=descuento,
                                                     impuesto=impuesto, otros=otros, total=total, xml_documento=xml_response.decode(
                                                         'utf-8'),
                                                     tarifa_0=tarifa_0, tarifa_1=tarifa_1, tarifa_2=tarifa_2, tarifa_4=tarifa_4, tarifa_8=tarifa_8, tarifa_13=tarifa_13, otros_impuestos=otros_impuestos)

                        electronic_doc.set_document_type()

                        if electronic_doc.verify_registered_edoc():
                            return electronic_doc.update_edoc_data()
                        else:
                            return electronic_doc.insert_edoc_data()

                # print(xml_data)
                return True
