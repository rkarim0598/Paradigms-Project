import re, json
import cherrypy
from _tv_database import _tv_database

class UserController(object):
	def __init__(self, database=None):
		if database is None:
			self.td = _tv_database()
		else:
			self.td = database
		self.td.load_users('../fetch_data/users.txt')

	def get_value(self, key):
		return self.td.get_user(key)

	#even handlers for resource requests
	def GET_UID(self, uid):
		#rule 1
		output = {'result' : 'success'}

		#rule 2 - check your data - key or payload
		key = str(uid)

		#rule 3 - try - except
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

	def GET(self):
		output = {'result' : 'success'}

		try:
			output['output'] = self.td.get_users()
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	def POST(self):
		output = {'result': 'success'}

		#extract message from body
		data = json.loads(cherrypy.request.body.read())
		
		try:
			self.td.set_user(data['uname'],data['pname'],data['password'],'../fetch_data/users.txt')
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {'result': 'success'}

		try:
			self.td.users = {}
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE_UID(self, uid):
		output = {'result': 'success'}

		key = str(uid)
		try:
			self.td.delete_user(key,'../fetch_data/users.txt')
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
