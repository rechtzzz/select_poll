import socket
import sys

client = socket.socket()
server_address = ('localhost', 10000)
client.connect(server_address)

print(sys.stderr, 'connecting to %s port %s' % server_address)

while True:
    mes = input('please input >>')
    if mes == 'q':
        print('quit...')
        client.close()
        break
    else:
        client.send(mes.encode('utf-8'))

        data = client.recv(1024)
        print (sys.stderr, '%s: received "%s"' % (client.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', client.getsockname())