"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet, People, UserFavorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# all the people
@app.route('/people', methods=['GET'])
def get_all_people():
    users = People.query.all()
    all_people = list(map(lambda x: x.serialize(), users))
    return jsonify(all_people), 200


# id of person
@app.route('/people/<int:user_id>', methods=['GET'])
def get_people_id(user_id):
    response_body = request.get_json()
    user = People.query.get(user_id)
    return jsonify(user), 200


# all planets
@app.route('/planets', methods=['GET'])
def get_planets_id():
    users = Planet.query.all()
    all_people = list(map(lambda x: x.serialize(), users))
    return jsonify(all_people), 200


# id of planets
@app.route('/planets/<int:user_id>', methods=['GET'])
def get_all_planets(user_id):
    response_body = request.get_json()
    user = Planet.query.get(user_id)
    return jsonify(user), 200



# all blog users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    all_people = list(map(lambda x: x.serialize(), users))
    return jsonify(all_people), 200


# user favorites 
@app.route('/users/favorites', methods=['GET'])
def get_all_user_favorites():
    users = UserFavorites.query.all()
    all_people = list(map(lambda x: x.serialize(), users))
    return jsonify(all_people), 200


#post


#post planets
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handle_planet():
    response_body = request.get_json()
    user = Planet(planets_id=response_body["planets_id"])
    db.session.add(user)
    db.session.commit()
    return jsonify(response_body), 200



# post people
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def handle_people():
    response_body = request.get_json()
    user = People(people_id=response_body["people_id"])
    db.session.add(user)
    db.session.commit()
    return jsonify(response_body), 200


# @app.route('/user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     response_body = request.get_json()
#     user = User.query.get(user_id)
    
#     if user is None:
#         raise APIException("user not found", 404)
#     if "email" in response_body:
#         user.email = response_body["email"]
#     if "password" in response_body:
#         user.password = response_body["password"]
#     db.session.commit()
#     return jsonify(response_body), 200



#delete


#delete planets
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_planets(planet_id):
    user = Planet.query.get(planet_id)
    if user is None:
        raise APIException("user not found", 404)
    db.session.delete(user)
    db.session.commit()
    return jsonify("planet has been deleted"), 200



#delete people
@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_people(person_id):
    user = People.query.get(person_id)
    if user is None:
        raise APIException("user not found", 404)
    db.session.delete(user)
    db.session.commit()
    return jsonify("person has been deleted"), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
