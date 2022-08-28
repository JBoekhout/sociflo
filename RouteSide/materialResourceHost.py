import queue, multiprocessing.pool
import time
import nodingFunctionals
from typing import Dict

#merge this data mould'\ with more broad economic dataset graphic mgr

imprt Dict
def Node_loop(s: NodeRoot):

class processMngr:
    urgent_prio_delta = 2
    def __init__(self, nodeintfc):
        Queue =     [   [],
                        [],
                        [],
                        [],
                        []]
        


    def addtoqueue(self, a: Dict):
        """ a: dict data packet discussing local recipe addition. 
        Recipe(): struct teardown
            "urgency" : process urgency Int() targetting process-queue priority levels -> bin 0 through n , with n being strategic layer count.
            "target": Label() Identifier of recipe objective
            "source": ()

             """

        if a["urgency"] < (-1 + self.urgent_prio_delta): #tdo urgency sort
            pfs = time.perf_counter()
            with multiprocessing.pool.Pool as pool:
                pool.apply_async(self.Queue[a["urgency"]].append((a["target"], a["recipe"]))) 
                pool.apply_async()
            pfe= time.perf_counter()
            print("perf = {pfe-pfs} seconds")
        elif a["urgency"]  < 3:
            self.Queue[a["urgency"]].append()
        
