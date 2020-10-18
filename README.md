# Nico

Módulo en desarrollo generado en Python 3 que permite la descarga, almacenaje y clasificación de documentos electrónicos emitidos en formato xml bajo la estructura establecida por el Ministerio de Hacienda de Costa Rica.

Dichos documentos se almacenan en SQLite. Puede descargar un archivo zip con el ejecutable x64 para Windows y su tabla de SQLite desde la carpeta dist.

# Uso

```
python Nico.py
```

# Interface

El módulo una vez inicializado despliega los siguientes componentes

## Parámetros de Búsqueda

El módulo permite el despliegue de los documentos descargados bajo los siguientes términos:
- Número de documento
- Nombre del Proveedor
- Rango de Fecha

## Tabla de Datos

Dependiendo del criterio de búsqueda, la tabla muestra la siguiente información de los documentos:
- Proveedor
- Cédula
- Tipo de Documento
- Número de Consecutivo
- Fecha
- Moneda
- Montos gravados, exentos y exonerados
- Subtotal
- Descuento
- Impuestos desde tarifa 0% hasta tarifa 13%
- Otros cargos
- Total
- Respuesta del Ministerio Hacienda
- Mensajes adicionales del documento de respuesta del Ministerio de Hacienda

La información de la tabla se puede exportar a formato de hoja de Microsoft Excel desde el botón exportar.

## Menú

El apartado **Archivo**  del menú principal cuenta con los siguientes apartados

### Importar Documentos

Puede escoger el rango de fechas que desea importar y clasificar desde su cuenta de correos.
El proceso se divide en dos fases:
1. Descarga desde el Servidor de Correos a la carpeta establecida en el apartado de **Configuración**.
2. Clasificación de los archivos de acuerdo a la información dentro del xml. Si es un archivo xml que cumple con la estructura establecida, se guarda en formato base64 dentro del SQLite. De lo contrario es eliminado de la carpeta. 

**IMPORTANTE** Si el archivo descargado es de formato .zip o .rar estos no serán abiertos ni eliminados luego de la clasificación. Si el usuario lo desea, puede extraer el contenido del archivo dentro de la carpeta establecida para que el sistema proceda con la lectura de los documentos compresos.

### Configuración

En este apartado se almacenan los datos del obligado tributario que recibe los documentos electrónicos:

- **Nombre**: Nombre del obligado tributario.
- **Cédula**: Número de identificación del obligado tributario
- **Carpeta**: Ubicación del directorio donde se descargarán y leerán los archivos importados desde el correo
- **P12**: Ubicación del archivo .P12 (Actualmente no se utiliza)
- **Correo**: Correo electrónico donde se reciben los documentos
- **Contraseña**: Contraseña del correo. Esta es encriptada antes de almacenarse en la base de datos.
- **Servidor**: Dirección del servidor de correos. Ejemplo
--- Gmail:  imap.gmail.com
--- Hotmail/Outlook:  imap-mail.outlook.com
--- Yahoo:  imap.mail.yahoo.com
- **Puerto de Entrada**: Puerto del servidor de correos para recepción. Ejemplo: 993
- **Puerto de Salida**: Puerto del servidor de correos para envío. Ejemplo: 465
- **Pin**: Pin del archivo .P12




# Requisitos

- altgraph>=0.17
- cffi>=1.14.3
- cryptography>=3.1.1
- dnspython>=2.0.0
- email-validator>=1.1.1
- future>=0.18.2
- idna>=2.10
- pefile>=2019.4.18
- pycparser>=2.20
- pyinstaller>=4.0
- pyinstaller-hooks-contrib>=2020.9
- PySide2>=5.15.1
- pywin32-ctypes>=0.2.0
- shiboken2>=5.15.1
- six>=1.15.0
- XlsxWriter>=1.3.7
- xmltodict>=0.12.0

