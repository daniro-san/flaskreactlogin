# app.py

from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flasklogin'
app.config['MONGO_URI'] = 'mongodb+srv://flaskmongo:flaskmongopass@flasklogin-jdskx.mongodb.net/flasklogin'

mongo = PyMongo(app)

@app.route('/')
def index():
    return Response('Vates')

@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
  users = mongo.db.users
  name = request.json['name']
  password = request.json['password']
  login_user = users.find_one({ 'name' : name, 'password': password })
  
  if login_user: 
    return jsonify({'status' : '0', 'message': 'Login successful'})
  return jsonify({'status' : -1, 'message': 'username or password invalid'})

@app.route('/register', methods=['POST', 'GET'])
def register():
  users = mongo.db.users
  name = request.json['name']
  password = request.json['password']
  existing_user = users.find_one({ 'name' : name })
  
  if existing_user is None: 
    users.insert({'name': name, 'password': password })
    return jsonify({'status' : '0', 'message': 'New user created'})
  return jsonify({'status' : -1, 'message': 'username already registered, try using another'})

if __name__ == '__main__':
  app.run(debug=True)