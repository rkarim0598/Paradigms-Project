import cherrypy
import json

class RatingController(object):
	def __init__(self, tdb=None):
		if tdb is None:
			self.tdb = dict()
		else:
			self.tdb = tdb

	def GET_RATING(self, sid):
		output = { 'result' : 'success' }
		sid = str(sid)

		try:
			rating = self.tdb.get_rating(sid)
			output['rating'] = rating
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
