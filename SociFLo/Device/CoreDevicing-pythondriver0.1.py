import csv, os, io, socket, threading, json
from typing import Dict, List, 
#mb strip down this module file further to stay true to 'Core'

share_q = []

class Config(Dict):

    def __init__(self):
        conf_cache = json.load(open("./conf.json").read())
        self.ID = conf_cache["ID"]
        self.Presets = conf_cache["Presets"]
        self.Apps = conf_cache["Apps"]
        self.LLDs = conf_cache["ll_daemons"] #lowllevel i presume


                    #self.Presets = [{pi[0]:pi[1:] for pi in row[1:]]
    def write(catg, label, confdata):
        if catg == 0:
            self.ID[label]
class NetworkIntfcings():

    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = []
    def loop(self, procspecs = None, ):

    def push_all(network_q: List = share_q):
        for qi_i in range(len(network_q)):
            try:
                push(network_q.pop(qi_i))
            except e:
                print("Failed to loopback 2 network") # logging code
                
                    
            
    
        

        

class Storage():
    root = open(os.Path("./stor/"))
        #Low mem load through network off-lift
    def __init__(self, mode=):
        self.state = ""
        sel
    def push(loc, data):
        self.root.write(data)
    
class dtTreeJunct():
    Black = 0
    def __init__(self, color=Black, presetdt=None):
        if presetdt != None:
            self.pushcolor(color)
            self.pushdt(presetdt[1], codec=presetdt[0])
        else:
            self.pushcolor(color)
    def pushcolor(self, color):
        
def init():
    conf = Config()
    preset_stack = [pi for pi in conf.Presets]
    process_stack = [p for p in conf.Apps + conf.LLDs]
     def main():
         process



