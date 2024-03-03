import socket 
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'
fake = Faker()

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'starting up on {server_address}')
sock.bind(server_address)

while True:
    print(f'\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
    print(f'received {len(data)} bytes from {address}')
    print(data)

    if data:
        response = sock.sendto(bytes(fake.text(), encoding='utf-8'), address)
        print(f'sent {response} bytes back to {address}')
