from db import db
from sqlalchemy import TIMESTAMP
from datetime import datetime

class user_information(db.Model):
    # __tablename = 'users'
    gpid = db.Column(db.Integer, nullable=False,unique = True)
    email_id = db.Column(db.String(255),primary_key=True)
    first_name = db.Column(db.String(255),nullable = False)
    # last_name =  db.Column(db.String(255),nullable = False)
   
    # db.relationship parameter
    chat_info_relationship = db.relationship('chat_info',backref="user_info")
    file_info_relationship = db.relationship('file_info',backref="user_info")
    folder_info_relationship = db.relationship('folder_info',backref='user_info')



class folder_info(db.Model):
    folder_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    folder_name = db.Column(db.String(255),nullable = False,unique=True)
    email_id =  db.Column(db.String(255),db.ForeignKey("user_information.email_id"))
    folder_update_date = db.Column(TIMESTAMP,default=datetime.utcnow)
    # latest_status = db.Column(db.String(255))


    # db.relationship parameter
    file_info_relationship = db.relationship('file_info',backref="file_info")





class file_info(db.Model):
    file_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    file_name = db.Column(db.String(255),nullable = False)
    folder_name = db.Column(db.String(255),db.ForeignKey('folder_info.folder_name'),nullable = False)
    email_id = db.Column(db.String(255),db.ForeignKey('user_information.email_id'),nullable = False)
    file_update_date = db.Column(TIMESTAMP,default=datetime.utcnow)



class chat_info(db.Model):
    session_id = db.Column(db.String(255),nullable = False)
    chat_id = db.Column(db.Integer,nullable = False,primary_key = True)
    email_id =  db.Column(db.String(255),db.ForeignKey('user_information.email_id'),nullable = False)
    user_question = db.Column(db.Text,nullable = False)
    assistant_response = db.Column(db.Text,nullable = False)
    timestamp = db.Column(TIMESTAMP,default=datetime.utcnow)
    # keywords
    feedback = db.Column(db.Boolean)