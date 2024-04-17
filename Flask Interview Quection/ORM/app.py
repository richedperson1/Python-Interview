from flask import Flask, jsonify, request,jsonify,Response,stream_with_context
from flask_sqlalchemy import SQLAlchemy
import random
import time
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'  # SQLite database file

db = SQLAlchemy(app)
app.app_context().push()
# Define Pet and Owner models with a relationship
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text)

    # pets = db.relationship('Pet', backref='owner_info_backref')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    Owner_backref = db.relationship('Owner', backref='owner_info_backref')



class streaming_data:
    def generate_data(self):
        self.stream = ""
        for i in range(10):
            time.sleep(1)  # Simulate data generation
            yield f"Data chunk {i+1}\n"
            self.stream+=f"Data chunk {i+1}\n"
        self.storing_data_db()
    def storing_data_db(self):
        new_owner = Owner(id = 5,name = "Rutvik",details = self.stream)
        
        db.session.add(new_owner)
        db.session.commit()
        
@app.route('/stream')
def stream_response():
    obj = streaming_data()
    return Response(stream_with_context(obj.generate_data()), content_type='text/plain')


db.create_all()

# Routes to add and retrieve pet and owner information
@app.route('/add_owner', methods=['POST'])
def add_owner():
    data = request.get_json()
    name = data.get('name')

    new_owner = Owner(name=name)
    db.session.add(new_owner)
    db.session.commit()

    return jsonify({'message': 'Owner added successfully'}), 201

@app.route('/add_pet', methods=['POST'])
def add_pet():
    data = request.get_json()
    name = data.get('name')
    species = data.get('age')
    owner_id = data.get('owner_id')

    new_pet = Pet(name=name, age=species, owner_id=owner_id)
    db.session.add(new_pet)
    db.session.commit()

    return jsonify({'message': 'Pet added successfully'}), 201

@app.route('/get_owners', methods=['GET'])
def get_owners():
    owners = Owner.query.all()
    owners_data = [{'id': owner.id, 'name': owner.name} for owner in owners]
    return jsonify({'owners': owners_data})

@app.route('/get_pets', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    pets_data = [{'id': pet.id, 'name': pet.name, 'species': pet.species, 'owner_id': pet.owner_id} for pet in pets]
    return jsonify({'pets': pets_data})

if __name__ == '__main__':
    app.run(debug=True)
