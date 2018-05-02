import os

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
  try:

    users = mongo.db.users
    

    if request.method == 'POST':

      # name = request.form['name']
      # password = request.form['password']   
      name = 'abc'
      password = 'abc'

      # parametros = request.get_json()

      # name = parametros['name']
      # password = parametros['password']
      return jsonify({'retorno': jsonify(request)})

    else:
      
      name = request.args.get('name')
      password = request.args.get('password')

    autenticacao = users.find_one({ 'name' : name, 'password': password })
    if autenticacao: 
      return jsonify({'status' : '0', 'message': 'Login successful'})

    return jsonify({'status' : -1, 'message': 'username or password invalid'})

  except Exception as e:
      print('REQUEST /autenticar error ' + str(e) )
      return str(e)

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