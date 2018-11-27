import cherrypy
import json

from _tv_database import _tv_database

class ResetController(object):
	def __init__(self, tdb=None):
		if tdb is None:
			self.tdb = _tv_database()
		else:
			self.tdb = tdb
	
	def PUT_INDEX(self):
		output = {'result': 'success'}
		data = json.loads(cherrypy.request.body.read().decode())
		try:
			self.tdb.load_tvshows('../fetch_data/shows.txt')
			self.tdb.load_users('../fetch_data/users.txt')
			self.tdb.delete_ratings()
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
	
	def PUT_SID(self, sid):
		output = {'result': 'success'}
		sid = int(sid)
		
		try:
			data = json.loads(cherrypy.request.body.read().decode())
			tdb_tmp = _tv_database()
			tdb_tmp.load_tvshows('../fetch_data/shows.txt')
			show = tdb_tmp.get_show(sid)
			if show['result'] == 'success':
				show.pop('result')
				self.tdb.set_show(sid, show)
			else:
				output['result'] = 'error'
				output['message'] = 'Show not found'
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		
		return json.dumps(output)
