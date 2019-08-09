#!/usr/bin python 
# -*- coding: utf-8 -*- 

import smtplib

import os, sys
import re
import shutil
#import zipfile

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# função para mandar os arquivos copiados em uma pasta em formato .zip para o email desejado.
       
def send_to_email():
    
    fromaddress = "email that will send the file"
    toaddress = "email to receive the files" # mudar para mandar para a pessoa desejada

    msg = MIMEMultipart()

    msg['de'] = fromaddress 
    msg['para'] = toaddress
    msg['assunto'] = "POR FAVOR NÃO MATE SUA MULHER"

    body = " TESTE "

    msg.attach(MIMEText(body, 'plain'))
    fl = os.listdir(".")
    print ("\n") 
    full_file_name = raw_input("choose the file to send: \n")  
      
    attachment = open(full_file_name, "rb")
   

    part = MIMEBase('application', 'octet-stream') 
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=' + full_file_name)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddress, "your email password")
    text = msg.as_string()
    server.sendmail(fromaddress, toaddress, text)
    print ("\nfeito\narquivo enviado\n")
    server.quit()  

