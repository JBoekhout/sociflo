import socket
from threading import Thread
import time
from typing import Dict, List, type_check_only 

modeset = {0:{  'ouptut_loc':   drivers.networking.Node(0),
                'label':        "std dataq"}}



class DataQueue(object):

    loop_t = None
    dataQ = {}
    log_mode = 1
    reset = 0

    def __init__(self, mode, output_loc = None)
        self.state = "initializing"
        threading = 1
        if threading:
            t = Thread(target=self.setup_autopush(output_loc, freq))
        elif not threading:
            self.setup_autopush(output_loc, freq=None)
    def push(loc):
        #displacing the ackets integre im most imfluked
    def inbetweenr_loop(self):
        t0= time.time

        while True:
            self.push(self.dataQ)
            t = time.time 
            if t - t0 >= 3:
                break



    def setup_autopush(self, loc, freq, ):
        self.state = "Setting up autopushQ, inbetween layering goes for insta q"
        
        t0 = time.time
        dt = 0 + "hardwaredelay"
        while True:
            
            
import socket
class socketlogic():
    packet_standards = {"SOCK_STREAM": {"payload_len":None,
                                        "header_divisor":"x",
                                        "Header_range/list/catgs":None}}
    import socket
    def __init__(self):
        netguns = socket.socketpair()
        gunout = (netguns[0], 0)
        gunvest = (netguns[1],0)
    def format_packet(type, header, data):
        packet
        packet_s_s
        return packet_s_s # packets_strung and split potetnially
    def gunner(packet_s, destination): #relay stack o pack's
        if type(packet_s) == (List or Dict):
            if check_format(packet_s, 'gunner'): 
                self.gunout[0].connect(destination)
                for each in packet_s:
                    self.gunout[0].send(packet_s)
            else:
                print("pakcetformat untransferrable")


#sockets a dataqueue ansich on its own.
