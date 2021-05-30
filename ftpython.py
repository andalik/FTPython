from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_PORT = 21

FTP_USER = "usuario"
FTP_PASSWORD = "senha"
FTP_DIRECTORY = "/opt/ftpython/public/"

def main():
    authorizer = DummyAuthorizer()

    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    #
    handler.banner = "Bemvindo ao FTPython"

    handler.passive_ports = range(60000, 65535)

    handler.timeout = 3600

    address = ('', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()
