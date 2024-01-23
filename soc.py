import argparse
import socket 

parser = argparse.ArgumentParser(description='Arguements')
parser.add_argument('-flag', help='A flag.', action='store_true')
parser.add_argument('--host',default='localhost')

args = parser.parse_args()

Flag=args.flag
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if Flag:
    s.bind(("", 830))
    s.listen()
    (client_socket,adress)=s.accept()

    text=client_socket.recv(10)
    if text!=b'Hey stinky':
        raise ValueError('Ce n est pas le message attendu')
    
    client_socket.send(b'1/ch')


else: 
    s.connect((args.host,830))
    s.send(b'Hey stinky')

    text=s.recv(4)
    if text!=b'1/ch':
        raise ValueError('Ce n est pas le message attendu')
    print('It works')



