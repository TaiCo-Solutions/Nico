import os
import sqlite3


class XmlDocument:

    current_directory = os.getcwd()

    def __init__(self, proveedor="", cedula="", documento_tipo=1, clave="", consecutivo="", fecha="", moneda="CRC", gravado=0.00,
                 exento=0.00, exonerado=0.00, subtotal=0.00, descuento=0.00, impuesto=0.00, otros=0.00, total=0.00, respuesta_hacienda=2,
                 detalle_mensaje="", xml_documento="", xml_respuesta="", tarifa_0=0, tarifa_1=0, tarifa_2=0, tarifa_4=0, tarifa_8=0, tarifa_13=0, otros_impuestos=0):
        self.proveedor = proveedor
        self.cedula = cedula
        self.documento_tipo = documento_tipo
        self.clave = clave
        self.consecutivo = consecutivo
        self.fecha = fecha
        self.moneda = moneda
        self.gravado = gravado
        self.exento = exento
        self.exonerado = exonerado
        self.subtotal = subtotal
        self.descuento = descuento
        self.impuesto = impuesto
        self.otros = otros
        self.total = total
        self.respuesta_hacienda = respuesta_hacienda
        self.detalle_mensaje = detalle_mensaje
        self.xml_documento = xml_documento
        self.xml_respuesta = xml_respuesta
        self.tarifa_0 = tarifa_0
        self.tarifa_1 = tarifa_1
        self.tarifa_2 = tarifa_2
        self.tarifa_4 = tarifa_4
        self.tarifa_8 = tarifa_8
        self.tarifa_13 = tarifa_13
        self.otros_impuestos = otros_impuestos

    def connect_sqlite(self):
        db_path = os.path.join(self.current_directory, "nico.db")
        conn = sqlite3.connect(db_path)
        return conn

    def get_edoc_data(self, query="", query_list=()):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT documento_electronico.proveedor, documento_electronico.cedula, documento_tipo.descripcion, documento_electronico.clave, 
            documento_electronico.consecutivo, documento_electronico.fecha, documento_electronico.moneda, documento_electronico.gravado, 
            documento_electronico.exento, documento_electronico.exonerado, documento_electronico.subtotal, documento_electronico.descuento, 
            documento_electronico.tarifa_0, documento_electronico.tarifa_1, documento_electronico.tarifa_2, documento_electronico.tarifa_4, documento_electronico.tarifa_8, documento_electronico.tarifa_13, documento_electronico.otros_impuestos,  
            documento_electronico.impuesto, documento_electronico.otros, documento_electronico.total, respuesta_hacienda.estado, documento_electronico.detalle_mensaje            
            FROM documento_electronico, respuesta_hacienda, documento_tipo {query} 
            AND respuesta_hacienda.id = documento_electronico.respuesta_hacienda AND documento_tipo.id = documento_electronico.documento_tipo 
             ORDER BY documento_electronico.moneda, documento_electronico.documento_tipo, documento_electronico.fecha""", query_list)

            data = cursor.fetchall()

            if data:
                return data
            else:
                return []

    def verify_registered_edoc(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT id FROM documento_electronico WHERE clave = ?""", (self.clave, ))

            data = cursor.fetchone()
            print(data)
            if data:
                print(data[0])
                return data[0] >= 1
            else:
                return False

    def save_edoc_data(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            query_str = """INSERT INTO documento_electronico (proveedor, cedula, documento_tipo, clave, consecutivo, fecha, moneda, gravado, 
            exento, exonerado, subtotal, descuento, impuesto, otros, total, respuesta_hacienda, detalle_mensaje, xml_documento, xml_respuesta,
            tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos) 
            VALUES (?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query_str,
                           (self.proveedor, self.cedula, self.documento_tipo, self.clave, self.consecutivo, self.fecha, self.moneda, self.gravado, self.exento,
                            self.exonerado, self.subtotal, self.descuento, self.impuesto, self.otros, self.total, self.respuesta_hacienda, self.detalle_mensaje,
                            self.xml_documento, self.xml_respuesta, self.tarifa_0, self.tarifa_1, self.tarifa_2, self.tarifa_4, self.tarifa_8,
                            self.tarifa_13, self.otros_impuestos))
            connection.commit()
            return True
        else:
            print("error")
            return False

    def update_edoc_response(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            query_str = """UPDATE documento_electronico SET respuesta_hacienda = ?, detalle_mensaje = ?, xml_respuesta = ? WHERE clave = ?"""
            cursor.execute(query_str, (self.respuesta_hacienda,
                                       self.detalle_mensaje, self.xml_respuesta, self.clave, ))
            connection.commit()
            return True

    def insert_edoc_response(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            query_str = """INSERT INTO documento_electronico (clave, respuesta_hacienda, detalle_mensaje, xml_respuesta) VALUES (?, ?, ?, ?)"""
            cursor.execute(query_str, (self.clave, self.respuesta_hacienda,
                                       self.detalle_mensaje, self.xml_respuesta, ))
            connection.commit()
            return True

    def set_document_type(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT id FROM documento_tipo WHERE codigo = ?""", (self.documento_tipo, ))
            data = cursor.fetchone()
            self.documento_tipo = data[0]

    def insert_edoc_data(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            query_str = """INSERT INTO documento_electronico (proveedor, cedula, documento_tipo, clave, consecutivo, fecha, moneda, gravado, 
            exento, exonerado, subtotal, descuento, impuesto, otros, total, xml_documento, 
            tarifa_0, tarifa_1, tarifa_2, tarifa_4, tarifa_8, tarifa_13, otros_impuestos) 
            VALUES (?, ?, ?, ?, 
            ?, ?, ?, ?,  
            ?, ?, ?, ?,  
            ?, ?, ?, ?,
            ?, ?, ?, 
            ?, ?, ?, ?)"""
            cursor.execute(query_str,
                           (self.proveedor, self.cedula, self.documento_tipo, self.clave, self.consecutivo, self.fecha, self.moneda, self.gravado, self.exento,
                            self.exonerado, self.subtotal, self.descuento, self.impuesto, self.otros, self.total, self.xml_documento,
                            self.tarifa_0, self.tarifa_1, self.tarifa_2, self.tarifa_4, self.tarifa_8,
                            self.tarifa_13, self.otros_impuestos))
            connection.commit()
            return True
        else:
            print("error")
            return False

    def update_edoc_data(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            query_str = """UPDATE documento_electronico SET proveedor = ?, cedula = ?, documento_tipo = ?, consecutivo = ?, fecha = ?, moneda = ?, gravado = ?, 
            exento = ?, exonerado = ?, subtotal = ?, descuento = ?, impuesto = ?, otros = ?, total = ?, xml_documento  = ?, 
            tarifa_0 = ?,  tarifa_1 = ?, tarifa_2 = ?, tarifa_4 = ?, tarifa_8 = ?, tarifa_13 = ?, otros_impuestos = ? WHERE clave = ? """
            cursor.execute(query_str,
                           (self.proveedor, self.cedula, self.documento_tipo, self.consecutivo, self.fecha, self.moneda, self.gravado, self.exento,
                            self.exonerado, self.subtotal, self.descuento, self.impuesto, self.otros, self.total, self.xml_documento,
                            self.tarifa_0, self.tarifa_1, self.tarifa_2, self.tarifa_4, self.tarifa_8,
                            self.tarifa_13, self.otros_impuestos, self.clave))
            connection.commit()
            return True
        else:
            print("error")
            return False

    def get_provider_list(self):
        connection = self.connect_sqlite()
        if connection:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT DISTINCT proveedor FROM documento_electronico ORDER BY proveedor""")
            data = cursor.fetchall()
            return data
        else:
            return []
