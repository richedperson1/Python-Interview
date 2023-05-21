"""
Serialization
It's the process at which we can convert python supported object into the either 
network supported object or file supported object.
"""

import json
import pickle
class obj:
    def __init__(self,name) -> None:
        self.fName = name
        self.lName = "Jaiswal"
        self.mobile= 9673062604
        self.city = "Jalgaon"


rutvik = obj("Rutvik")
with open("serialization.json","wb") as f:
    dataLoading = pickle.dump(rutvik,f)
    

with open("serialization.json","rb") as f:
    dataLoading = pickle.load(f)
    print(dataLoading.__dict__)