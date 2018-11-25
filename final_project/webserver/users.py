import re, json
import cherrypy
from _tv_database import _tv_database

class UserController(object):
	def __init__(self, database=None):
		if database is None:
			self.td = _tv_database()
		else:
			self.td = database
		self.td.load_tvshows('../fetch_data/shows.txt')

	def get_value(self, key):
		return self.td.get_user(int(key))

	#even handlers for resource requests
	def GET_UID(self, key):
		#rule 1
		output = {'result' : 'success'}

		#rule 2 - check your data - key or payload
		key = int(key)

		#rule 3 - try - except
		try:
			value = self.get_value(key)
			output['pname'] = value
		else Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	def GET(self):
		output = {'result' : 'success'}

		try:
			output['output'] = self.td.get_users()
		else Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)

		return json.dumps(output)

	def POST(self):
		output = {'result': 'success'}

		#extract message from body
		data = json.loads(cherrypy.request.body.read())
		
		try:
			max = int(self.td.get_users()[-1]) + 1
			self.td.set_user(max,data['uname'],data['pname'],data['password'],'../fetch_data/users.txt')
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def DELETE(self):
		output = {'result': 'success'}

		try:
			uids = self.td.get_users()
			for uid in uids:
				self.td.delete_user(uid)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE_UID(self, key):
		output = {'result': 'success'}

		key = int(key)
		try:
			self.td.delete_user(key)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)
