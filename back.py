#!/usr/bin/python
# -*- coding: utf-8 -*-

# Execute o código sem previlégios de root; pois o 'username' deve ser detectado, e então, a cópia poder ser realizada, caso contrário o código irá capturar o hostname (root), ou seja, /media/root/PENDRIVE; o que acarretará em erro, já que o caminho para a pasta é dada por /media/USERNAME/PENDRIVE 

# Para enviar para o email o previlégio de root é válido.

# Aprimorado na próxima versão. 

import os
import re
import shutil

# função para encontrar os arquivos

# function to find the files

def find_files(pattern, path):
    for path, dirs, files in os.walk(path):
        for filename in files:
            full_file_name = os.path.join(path, filename)
            match = re.match(pattern, full_file_name)
            if match:
                yield full_file_name

# função para copiar os arquivos encontrados

# function to copy matched files
 
def copy_files(pattern, src_path, dest_path):    
    for full_file_name in find_files(pattern, src_path):
        print(full_file_name) + ' file copied into ' + (dest_path)
        try:
            shutil.copy(full_file_name, dest_path)
            #shutil.make_archive(full_file_name, 'zip', dest_path)
        except IOError:
            pass

