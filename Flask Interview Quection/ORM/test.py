from flask import current_app
from orm import chat_info
from db import db
import time
import random

def data_storage(data):
    print("Data is : ",data)

def addingFolder_streaming():
    def streaming():
        ind = 5
        while ind > 0:
            ind -= 1
            yield f"index-{ind}"
            time.sleep(0.2)

    final_data = ''
    for data in streaming():
        new_data_stream = data + str(random.random())
        yield f"{new_data_stream}\n"
        final_data += f"{new_data_stream}"

    data_storage(final_data)

def addingFolder(folder_name, email_id, obj):
    new_data = random.random()
    folder_name = f"{folder_name}-{new_data}"
    email_id = f"{email_id}-{new_data}"

    return addingFolder_streaming()
