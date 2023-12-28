from flask import Flask ,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine,TIMESTAMP
import requests
from datetime import datetime
from test import adding2db
from flask_migrate import Migrate, MigrateCommand
# Add this line to enable Flask-Migrate commands in the Flask CLI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db.init_app(app)
# migrate = Migrate(app, db)
# # migrate.init_app(app)
app.app_context().push()

# migrate = Migrate(app, db)
# migrate.init_app(app)
# app.cli.add_command("db",MigrateCommand)

with app.app_context():
    db.create_all()
    
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

db.create_all()
"""
    folder_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    folder_name = db.Column(db.String(255),nullable = False,unique=True)
    email_id =  db.Column(db.String(255),db.ForeignKey("user_information.email_id"))
    # latest_status = db.Column(db.String(255))
 
    # db.relationship parameter
    file_info_relationship = db.relationship('file_info',backref="file_info")
"""
@app.route('/add_folder', methods=['POST'])
def add_folder():
    data = request.get_json()

    # try:
    
    # folder_id = data['folder_id']
    folder_name = data['folder_name']
    email_id = data['email_id']
    adding2db(folder_info,db)
    new_folder_info = folder_info(folder_name = folder_name,email_id = email_id)
    
    db.session.add(new_folder_info)
    db.session.commit()
    # except Exception as e:
    #     return jsonify({"result":f"user already register : {e}"})

    return jsonify({'message': 'Owner added successfully'}), 201

"""
class file_info(db.Model):
    file_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    file_name = db.Column(db.String(255),nullable = False)
    folder_id = db.Column(db.Integer,db.ForeignKey('folder_info.folder_id'),nullable = False)
    email_id = db.Column(db.String(255),db.ForeignKey('user_information.email_id'),nullable = False)
    upload_date = db.Column(TIMESTAMP,server_default = 'CURRENT_TIMESTAMP')
"""
@app.route('/add_file', methods=['POST'])
def add_file():
    data = request.get_json()

    # try:
    file_name = data['file_name']
    folder_name = data['folder_name']
    email_id = data['email_id']
    
    
    new_file_info = file_info(file_name = file_name,folder_name = folder_name,email_id=email_id)
    db.session.add(new_file_info)
    db.session.commit()
    # except Exception as e:
    #     return jsonify({"result":f"user already register : {e}"})

    return jsonify({'message': 'Owner added successfully'}), 201



@app.route('/add_chat', methods=['POST'])
def add_chat():
    data = request.get_json()

    # try:
    session_id = data['session_id']
    chat_id = data['chat_id']
    email_id = data['email_id']
    user_question = data['user_question']
    assistant_response = data['assistant_response']
    # timestamp = data['timestamp']
    feedback = data['feedback']
    
    
    new_chat_info = chat_info(session_id = session_id,
                              chat_id=chat_id,email_id = email_id,user_question=user_question,
                              assistant_response = assistant_response,feedback = feedback
                              )

    db.session.add(new_chat_info)
    db.session.commit()
    # except Exception as e:
    #     return jsonify({"result":f"user already register : {e}"})

    return jsonify({'message': 'Owner added successfully'}), 201
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # try:
    
    print("datadatadatadatadatadatadatadata" ,data)
    new_user_info = user_information(gpid=data.get('gpid'," "),email_id=data['email_id'],
                                        first_name = data['first_name'])

    db.session.add(new_user_info)
    db.session.commit()
    # except Exception as e:
    #     return jsonify({"result":f"user already register : {e}"})

    return jsonify({'message': 'Owner added successfully'}), 201

@app.route('/remove_user', methods=['DELETE'])
def remove_user():
    data = request.get_json()

    # try:
    
    # print("datadatadatadatadatadatadatadata" ,data)
    remove_gpid = data.get("gpid")
    user_info = user_information.query.filter(user_information.gpid==remove_gpid).all()
    
    for user in user_info:
        db.session.delete(user)
    db.session.commit()
    # except Exception as e:
    #     return jsonify({"result":f"user already register : {e}"})

    return jsonify({'message': 'Owner added successfully'}), 201

# @app.route('/add_pet', methods=['POST'])
# def add_pet():
#     data = request.get_json()
#     name = data.get('name')
#     species = data.get('species')
#     # owner_id = data.get('owner_id')

#     new_pet = Pet(name=name, species=species, owner_backref='Rutvik')
#     db.session.add(new_pet)
#     db.session.commit()

#     return jsonify({'message': 'Pet added successfully'}), 201

@app.route('/get_owners', methods=['GET'])
def get_owners():
    owners = Owner.query.all()
    owners_data = [{'id': owner.id, 'name': owner.name} for owner in owners]
    return jsonify({'owners': owners_data})

# @app.route('/get_pets', methods=['GET'])
# def get_pets():
#     pets = Pet.query.all()
#     pets_data = [{'id': pet.id, 'name': pet.name, 'species': pet.species, 'owner_id': pet.owner_id} for pet in pets]
#     return jsonify({'pets': pets_data})

if __name__ == '__main__':
    app.run(debug=True,port = 3000)
    
