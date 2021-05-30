# FTPython
Servidor FTP simples em Python

## Uso:

### Instalação e configuração:

Inicialmente, como root, instale a biblioteca pyftpdlib.

No Ubuntu 20.04, use:
````
sudo apt-get install python3-pyftpdlib
````

No Ubuntu 14.04, 16.04, and 18.04, use:
````
sudo apt-get install python-pyftpdlib
````

### Iniciar servidor:

No Ubuntu 20.04, utilize o comando abaixo:
````
python3 /opt/ftpython/ftpython.py >>/opt/ftpython/ftpython.log 2>&1 &
````

No Ubuntu 14.04, 16.04, and 18.04, utilize o comando abaixo:
````
python /opt/ftpython/ftpython.py >>/opt/ftpython/ftpython.log 2>&1 &
````

### Encerrar servidor:

Para encerrar a execução do servidor FTP, utilize o comando kill com o process id obtido com o comando abaixo:
````
ps -ef | grep ftpython | grep -v grep | awk '{print $2}'
````
