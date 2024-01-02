from orm import folder_info
from db import db
import time
import random


def addingFolder_streaming():
    
    def streaming():
        ind = 5
        while ind>0:
            ind-=1
            yield(f"index-{ind}")
            time.sleep(1)
            
    for data in streaming():
        print(f"{data}")
        yield f"{data}\n"
    
    return "found"

def addingFolder(folder_name,email_id):
    new_data = random.random()
    folder_name = f"{folder_name}-{new_data}"
    email_id = f"{email_id}-{new_data}"
    
    
    data_storage(folder_name,email_id)
    return addingFolder_streaming()


def data_storage(folder_name,email_id):
    print("storing data : ")
    new_folder_info = folder_info(folder_name = folder_name,email_id = email_id)
    
    db.session.add(new_folder_info)
    db.session.commit()
    