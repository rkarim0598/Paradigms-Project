import cherrypy
import json
from _tv_database import _tv_database

class ShowController(object):
	def __init__(self, tdb=None):
		if tdb is None:
			self.tdb = _tv_database()
		else:
			self.tdb = tdb
		
		self.tdb.load_tvshows('../fetch_data/shows.txt')
	
	# Get a show by specifying the show id
	def GET_SID(self, sid):
		output = {'result': 'success'}
		sid = int(sid)
	
		try:
			show = self.tdb.get_show(sid)
			sdict = {}
			if show['result'] is not 'failure':
				sdict['name'] = show['name']
				sdict['genres'] = show['genres']
				sdict['site'] = show['site']
				sdict['rating'] = show['rating']
				sdict['image'] = show['image']
				sdict['summary'] = show['summary']
				output['output'] = sdict
				output['episodes'] = self.tdb.get_episodes(sid)
			else:
				output['result'] = 'error'
				output['message'] = 'movie not found'
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		
		return json.dumps(output)
	
	# Change a show (put) by specifying a show id
	def PUT_SID(self, sid):
		output = {'result': 'success'}
		sid = int(sid)
		
		try:
			data = json.loads(cherrypy.request.body.read().decode())
			self.tdb.set_show(sid, data)
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
	
	# Delete a show by specifying show id
	def DELETE_SID(self, sid):
		output = {'result': 'success'}
		sid = int(sid)
		
		try:
			self.tdb.delete_show(sid)
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
	
	# Get all shows
	def GET(self):
		output = {'result': 'success'}
		try:
			sids = self.tdb.get_shows()
			shows = []
			for sid in sids:
				sdict = {}
				sid = int(sid)
				show = self.tdb.get_show(sid)
				if show['result'] is not 'failure':
					sdict['sid'] = sid
					sdict['name'] = show['name']
					sdict['genres'] = show['genres']
					sdict['site'] = show['site']
					sdict['rating'] = show['rating']
					sdict['image'] = show['image']
					sdict['summary'] = show['summary']
				else:
					sdict['result'] = 'error'
					sdict['message'] = 'movie not found'
				shows.append(sdict)
			output['output'] = shows
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
	
	# Delete all shows
	def DELETE(self):
		output = {'result': 'success'}
		
		try:
			sids = self.tdb.get_shows()
			for sid in sids:
				self.tdb.delete_show(sid)
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
