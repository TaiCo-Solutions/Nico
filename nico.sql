BEGIN TRANSACTION;
DROP TABLE IF EXISTS "documento_tipo";
CREATE TABLE IF NOT EXISTS "documento_tipo" (
	"id"	INTEGER NOT NULL UNIQUE,
	"codigo"	TEXT NOT NULL UNIQUE,
	"descripcion"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "respuesta_hacienda";
CREATE TABLE IF NOT EXISTS "respuesta_hacienda" (
	"id"	INTEGER NOT NULL UNIQUE,
	"estado"	TEXT NOT NULL DEFAULT Sin respuesta,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "user_data";
CREATE TABLE IF NOT EXISTS "user_data" (
	"nombre"	TEXT NOT NULL,
	"cedula"	TEXT NOT NULL UNIQUE,
	"correo"	TEXT NOT NULL,
	"servidor"	TEXT NOT NULL,
	"clave"	TEXT NOT NULL,
	"puerto_entrada"	TEXT NOT NULL DEFAULT 993,
	"puerto_salida"	TEXT NOT NULL DEFAULT 25,
	"ubicacion"	TEXT NOT NULL,
	"codificador"	TEXT NOT NULL,
	"p12"	TEXT,
	"pin"	TEXT,
	PRIMARY KEY("cedula")
);
DROP TABLE IF EXISTS "documento_electronico";
CREATE TABLE IF NOT EXISTS "documento_electronico" (
	"id"	INTEGER NOT NULL UNIQUE,
	"proveedor"	TEXT,
	"cedula"	TEXT,
	"documento_tipo"	INTEGER,
	"clave"	TEXT NOT NULL UNIQUE,
	"consecutivo"	TEXT,
	"fecha"	TEXT,
	"moneda"	TEXT DEFAULT 'CRC',
	"gravado"	REAL DEFAULT 0,
	"exento"	REAL DEFAULT 0,
	"exonerado"	REAL DEFAULT 0,
	"tarifa_0"	REAL,
	"tarifa_1"	REAL,
	"tarifa_2"	REAL,
	"tarifa_4"	REAL,
	"tarifa_8"	REAL,
	"tarifa_13"	REAL,
	"otros_impuestos"	REAL,
	"subtotal"	REAL DEFAULT 0,
	"descuento"	REAL DEFAULT 0,
	"impuesto"	REAL DEFAULT 0,
	"otros"	REAL DEFAULT 0,
	"total"	REAL DEFAULT 0,
	"respuesta_hacienda"	INTEGER DEFAULT 2,
	"detalle_mensaje"	TEXT,
	"xml_documento"	TEXT,
	"xml_respuesta"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("respuesta_hacienda") REFERENCES "respuesta_hacienda"("id"),
	FOREIGN KEY("documento_tipo") REFERENCES "documento_tipo"("id")
);
INSERT INTO "documento_tipo" VALUES (1,'FacturaElectronica','Factura Electronica');
INSERT INTO "documento_tipo" VALUES (2,'MensajeHacienda','Mensaje de respuesta de Hacienda');
INSERT INTO "documento_tipo" VALUES (3,'MensajeReceptor','Mensaje de aceptacion o rechazo de los documentos electronicos por parte del obligado tributario');
INSERT INTO "documento_tipo" VALUES (4,'NotaCreditoElectronica','Nota de Credito');
INSERT INTO "documento_tipo" VALUES (5,'NotaDebitoElectronica','Nota de Debito');
INSERT INTO "documento_tipo" VALUES (6,'TiqueteElectronico','Tiquete Electronico');
INSERT INTO "respuesta_hacienda" VALUES (1,'Aceptado');
INSERT INTO "respuesta_hacienda" VALUES (2,'Sin respuesta');
INSERT INTO "respuesta_hacienda" VALUES (3,'Rechazado');
COMMIT;
