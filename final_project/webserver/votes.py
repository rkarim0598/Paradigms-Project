import cherrypy
import json

class VoteController(object):
	def __init__(self, tdb=None):
		if tdb is None:
			self.tdb = dict()
		else:
			self.tdb = tdb

	def GET_REC(self, uid):
		output = { 'result': 'success' }
		uid = str(uid)

		try:
			rec = self.tdb.get_recommendation(uid)
			output['sid'] = rec
		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)

	def PUT_REC(self, uid):
		uid = str(uid)
		output = { 'result' : 'success' }
		
		data = json.loads(cherrypy.request.body.read())

		try:
			self.tdb.set_user_rating(uid, str(data['sid']), int(data['rating']))
		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)	
