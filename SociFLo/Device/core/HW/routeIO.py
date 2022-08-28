from typing import ByteString
import drivers.*
import threading, socketserver, socket

class dano_intercom:
    def __init__(self):
        self.inbetweener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inbetweener.bind(socket.gethostname(), "99")
        self.inbetweener.listen(305)


    def HashOP(command, command_manifest="",): 
        pass

    def Push(packet: ByteString, address: drivers.cardano_base.Address,) #data transmission, packet data construction done inbound-task bytearray=inherent thus keep as coherent datatype construing mulitple costrucitve mirrors is off-key
        #pushingmorelocally is typical for priority messaging.
    def Retrieve(sock = self.inbetweener):
        prc = threading.Thread()

