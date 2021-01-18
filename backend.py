from flask import Flask
from flask import request
from flask import jsonify
from flask import CORS
import json
app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
	return 'Hello, world!'


@app.route('/users/<id>')
def get_user(id):
	if id:
		for user in users['users_list']:
			if user['id'] == id:
				return user
		return ({})
	return users

@app.route('/users', methods = ['GET', 'POST', 'DELETE'])
def get_users():
	if request.method == 'GET':
		search_username = request.args.get('name')
		search_job = request.args.get('job')
		if search_username and search_job:
			subdict={'users_list' :[]} 
			for user in users['users_list']:
					if user['name'] == search_username and user['job'] == search_job:
							subdict['users_list'].append(user)
							return subdict
							break
		elif search_username and search_job == None: 
			subdict={'users_list' :[]} 
			for user in users['users_list']:
					if user['name'] == search_username:
							subdict['users_list'].append(user)
			return subdict
		return users
	elif request.method == 'POST':
		userToAdd = request.get_json()
		users['users_list'].append(userToAdd)
		resp = jsonify(success=True)
		return resp
	elif request.method == 'DELETE':
		search_username = request.args.get('name')
		if search_username:
			for user in range(len(users['users_list'])):
				if users['users_list'][user]['name'] == search_username:
					del users['users_list'][user]
					return search_username + "\n"
		return 'cannot find user'
	
