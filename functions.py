import socket
from socket import *
import threading

####  Server Functions USEAGE:: #######

server = socket(AF_INET,SOCK_STREAM)
server.bind(("localhost",8267))
names = []
clients = []


def stage_1():
    server.listen(10)
    while True:
        Client_ip, Client_address = server.accept()
        Client_ip.send("[*] What's ur name? ".encode('utf-8'))
        name_of_client = Client_ip.recv(2048).decode('utf-8')
        clients.append(Client_ip)
        print(f"[*] Name entered :{name_of_client}")
        names.append(name_of_client)
        getAndsend("[*] {0} has joined the chat!".format(name_of_client).encode('utf-8'))
        #Client_ip.send('[*] Connected to {0}'.format(socketgethostname).encode('utf-8'))
        t = threading.Thread(target=maneger,args=(Client_ip, Client_address))
        t.start()
def getAndsend(message):
    for client in clients:
        client.send(message)

def maneger(Client_ip, Client_address):
    print("[*] {0} connected".format(Client_address))
    is_client = True
    while is_client:
        message = Client_ip.recv(2048)
        getAndsend(message)
    Client_ip.close()

