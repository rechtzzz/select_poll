import socket
import sys

messages = ['This is the message. ',

            ]
server_address = ('localhost', 10000)

# Create a TCP/IP socket
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM)]
# socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(100)]
#一次性建立一百个链接

# Connect the socket to the port where the server is listening
print(sys.stderr, 'connecting to %s port %s' % server_address)
#逐个建立链接
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print (sys.stderr, '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode('utf-8'))

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print (sys.stderr, '%s: received "%s"' % (s.getsockname(), data))
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname())
            s.close()