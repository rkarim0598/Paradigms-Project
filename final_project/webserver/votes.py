import cherrypy
import json

class VoteController(object):
	# constructor
	def __init__(self, tdb=None):
		if tdb is None:
			self.tdb = dict()
		else:
			self.tdb = tdb

	# get movie rec depending on given uid's previous ratings
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

	# add user vote given json data
	def PUT_REC(self, uid):
		uid = str(uid)
		output = { 'result' : 'success' }
		
		data = json.loads(cherrypy.request.body.read())

		try:
			sid = self.tdb.set_user_rating(uid, str(data['sid']), int(data['rating']))
			output['sid'] = sid
		except Exception as ex:
			output['result'] = 'failure'
			output['message'] = str(ex)

		return json.dumps(output)	
