	# Shows
#	dispatcher.connect('show_get', '/shows/', controller=showController, action='GET', conditions=dict(method=['GET']))
#    dispatcher.connect('show_delete', '/shows/', controller=showController,            action='DELETE', conditions=dict(method=['DELETE']))
	
	# Shows w/ sid
#	dispatcher.connect('show_get_sid', '/shows/:sid', controller=showController,       action='GET_SID', conditions=dict(method=['GET']))
#    dispatcher.connect('show_put_sid', '/shows/:sid', controller=showController,       action='PUT_SID', conditions=dict(method=['PUT']))
#    dispatcher.connect('show_delete_sid', '/shows/:sid', controller=showController,    action='DELETE_SID', conditions=dict(method=['DELETE']))

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
	
	def DELETE_SID(self, sid):
		output = {'result': 'success'}
		sid = int(sid)
		
		try:
			self.tdb.delete_show(sid)
		except Exception as e:
			output['result'] = 'error'
			output['message'] = str(e)
		return json.dumps(output)
	
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
