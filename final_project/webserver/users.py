import re, json
import cherrypy
from _tv_database import _tv_database

class UserController(object):
	# Constructor
	def __init__(self, database=None):
		if database is None:
			self.td = _tv_database()
		else:
			self.td = database
		self.td.load_users('../fetch_data/users.txt')

	def get_value(self, key):
		return self.td.get_user(key)

	# GET request with a uid key, returns json with pname listed
	def GET_UID(self, uid):
		output = {'result' : 'success'}
		key = str(uid)

		try:
			value = self.get_value(key)
			if value is not None:
				output['pname'] = value
			else:
				output['result'] = 'error'
				output['message'] = 'not a valid uid'
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	# GET request with no uid key, returns json with all uids
	def GET(self):
		output = {'result' : 'success'}

		try:
			output['output'] = self.td.get_users()
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	# POST request creates a new user, and updates users.txt
	def POST(self):
		output = {'result': 'success'}
		data = json.loads(cherrypy.request.body.read())
		
		try:
			r = self.td.get_user(data['pname'])
			if r['result'] == 'error':
				self.td.set_user(data['uname'],data['pname'],data['password'],'../fetch_data/users.txt')
			else:
				r['result'] = 'error'
				r['message'] = 'user already exists'
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	# DELETE request with no uid key deletes all current users
	def DELETE(self):
		output = {'result': 'success'}

		try:
			self.td.users = {}
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	# DELETE request with uid key deletes chosen user, and updates users.txt
	def DELETE_UID(self, uid):
		output = {'result': 'success'}

		key = str(uid)
		try:
			self.td.delete_user(key,'../fetch_data/users.txt')
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
