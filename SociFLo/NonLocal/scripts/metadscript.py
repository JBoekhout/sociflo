import os
import json
d = {}
i = 0
for each in os.scandir(os.getcwd()+"/NonLocal/AppCache"):
    i+=1

    d[i] = each.name
    

json.dump(d)
