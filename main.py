#!/usr/bin python
# -*- coding: utf-8 -*- 

from email_back import send_to_email
from back import copy_files
from back import find_files
import email_back

# Função principal. 

def main():

# configuração dos arquivos encontrados, para o redirecionamento para a pasta desejada

# tanto em linux quanto em windows...

# aprimorarei para iOS e android!
    
    import yaml
    import getpass
    from pprint import pprint
    from jinja2 import Template

    # set that to your paths... 
    
    backup_config = """

    Storages:
        - &Storage1 '/home/{{UserName}}/teste3' 
        - &Storage2 '/media/{{UserName}}/USB/teste' 
        - &Storage3 'F:\\B981-EC91\\{{UserName}}'
        - &Storage4 'G:\\B981-EC91\\{{UserName}}'
        - &Storage5 'H:\\B981-EC91\\{{UserName}}'
        - &Storage6 'C:\\Users'
    FileSets:
        - &LinuxSet
          - ['/home/{{UserName}}/Imagens', '.']
          - ['/home/{{UserName}}/Downloads', '.']
        - &WindowsSet
          - ['C:\\', '.']
          - ['D:\\', '.']
          - ['E:\\', '.']
    Jobs:
        - FileSet: *LinuxSet
          Storage: *Storage1
        - FileSet: *LinuxSet
          Storage: *Storage2
        - FileSet: *WindowsSet
          Storage: *Storage3
        - FileSet: *WindowsSet
          Storage: *Storage4
        - FileSet: *WindowsSet
          Storage: *Storage4
        - FileSet: *WindowsSet
          Storage: *Storage6
    """
# em &Storage1 define-se a pasta/pen drive para qual os arquivos serão copiados. No meu caso, o nome do pendrive está como ANDROID. E defini a pasta de downloads para fazer a cópia. ( - ['/home/{{UserName}}/Downloads', '.']) 

# assim como &Storage2, 3, 4... 

# em FileSets são as pastas em que estão os arquivos a serem copiados, neste caso /home/user/Downloads 

    t = Template(backup_config)
    config = yaml.safe_load(t.render(UserName=getpass.getuser())) # ye. this gets the username of pc, then access automatically the path. 

    print(pprint(config))


    for job in config['Jobs']:
        for fileset in job['FileSet']:
            print("copy_files('{}', '{}', '{}')".format(fileset[1], fileset[0], job['Storage']))
            copy_files(fileset[1], fileset[0], job['Storage'])
       
            send_to_email()


if __name__ == "__main__":
    
    
    main()
              #  elif not copy_files(fileset[1], fileset[0], job['Storage']))
        #pass

# copia para a unidade USB indicada, ou para alguma pasta, e envia para o email definido  

# do a copy to a USB drive given, or some path, and send to defined email

