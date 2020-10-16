from PySide2.QtGui import QTextCursor
import imaplib
import email
import os
import time
import base64
import random
import string
from User import User


class EmailDownload:

    date_string = ""
    letters = string.ascii_lowercase

    def __init__(self, text_message):
        self.current_user = User()
        self.current_user.get_user_data()
        self.text_message = text_message
        self.connection = False

        self.text_message.append(
            f"\nEstableciendo conexión con : {self.current_user.servidor}")
        self.connection = imaplib.IMAP4_SSL(
            self.current_user.servidor, self.current_user.puerto_entrada)
            
        if self.connection:
            self.start_login()

    def start_login(self):
        self.connection.login(self.current_user.correo, self.current_user.clave)
        self.connection.select('INBOX')

    def get_mail_data(self, date_start, date_end):
        search_result, message_ids = self.connection.search(
            None, '(SINCE "{}" BEFORE "{}")'.format(date_start, date_end))

        if search_result == "OK":
            if message_ids:
                if len(message_ids) > 0:
                    emails_to_read = message_ids[0].split()
                    self.text_message.append(f"Leyendo: {len(emails_to_read)} mensajes\n\nPor favor espere...")
                    for counter, current_email_id in enumerate(emails_to_read):
                        try:
                            result, data = self.connection.fetch(current_email_id, '(RFC822)')
                            raw_bytes = email.message_from_bytes(data[0][1])
                            self.get_attachments(raw_bytes)
                        except:
                            self.connection = imaplib.IMAP4_SSL(self.current_user.servidor, self.current_user.puerto_entrada)
                            self.start_login()
                            result, data = self.connection.fetch(current_email_id, '(RFC822)')
                            raw_bytes = email.message_from_bytes(data[0][1])
                            self.get_attachments(raw_bytes)
                    self.text_message.append(
                        f"\n **** PROCESO FINALIZADO **** \n")
                    self.text_message.moveCursor(QTextCursor.End)

    def get_attachments(self, message):
        folder_path = self.current_user.ubicacion

        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)

        for part in message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            file_name = part.get_filename()
            if bool(file_name):
                if "LnhtbA" in file_name or "ueG1s" in file_name or "54bWw" in file_name:
                    file_name = f"{file_name}.xml"
                if "?" in file_name:
                    file_name = file_name.replace("=?UTF-8?Q?", "")
                    file_name = file_name.replace("=?utf-8?B?", "")
                    file_name = file_name.replace("=?iso - 8859 - 1?Q?", "")
                    file_name = file_name.replace("?", "")

                file_name = file_name.strip().replace("\r\n", "")
                file_name = file_name.replace("/", "")
                file_name = file_name.replace("\n", "")
                file_name = file_name.replace("\t", "")
                file_name = file_name.replace("=", "")
                file_name = file_name.replace(" ", "")
                file_name = file_name.strip()
                file_name = f"""{self.get_random_string()}_{file_name}"""
                file_path = os.path.join(folder_path, file_name)

                with open(file_path, 'wb') as fp:
                    fp.write(part.get_payload(decode=True))

    def get_random_string(self):
        return ''.join(random.choice(self.letters) for i in range(4))
