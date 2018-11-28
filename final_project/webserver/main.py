import cherrypy

# create all these
from shows import ShowController
from users import UserController
from votes import VoteController
from ratings import RatingController
from reset import ResetController

from _tv_database import _tv_database

class OptionsController:
	def OPTIONS(self, *args, **kargs):
		return ""

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
	# create route dispatcher
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	
	# create tv database object
	tdb = _tv_database()
	
	# pass tdb to each controller
	showController = ShowController(tdb)
	userController = UserController(tdb)
	voteController = VoteController(tdb)
	ratingController = RatingController(tdb=tdb)
	resetController = ResetController(tdb)
	optionsController = OptionsController()
	
	''' dispatcher connects '''
	# Shows
	dispatcher.connect('show_get', '/shows/', controller=showController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('show_delete', '/shows/', controller=showController,            action='DELETE', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('show_all_options', '/shows/', controller=optionsController, action="OPTIONS", conditions=dict(method=['OPTIONS']))
	
	# Shows w/ sid
	dispatcher.connect('show_get_sid', '/shows/:sid', controller=showController,       action='GET_SID', conditions=dict(method=['GET']))
	dispatcher.connect('show_put_sid', '/shows/:sid', controller=showController,       action='PUT_SID', conditions=dict(method=['PUT']))
	dispatcher.connect('show_delete_sid', '/shows/:sid', controller=showController,    action='DELETE_SID', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('show_options', '/shows/:sid', controller=optionsController, action="OPTIONS", conditions=dict(method=['OPTIONS']))

	# Ratings
	dispatcher.connect('rating_get', '/ratings/:sid', controller=ratingController,        action='GET_RATING', conditions=dict(method=['GET']))

	dispatcher.connect('rating_options', '/ratings/:sid', controller=optionsController, action="OPTIONS", conditions=dict(method=['OPTIONS']))
	
	# Users w/ uid
	dispatcher.connect('user_get_uid', '/users/:uid', controller=userController,          action='GET_UID', conditions=dict(method=['GET']))
	dispatcher.connect('user_delete_uid', '/users/:uid', controller=userController,       action='DELETE_UID', conditions=dict(method=['DELETE']))
	
	dispatcher.connect('user_options', '/users/:uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

	# Users
	dispatcher.connect('user_get', '/users/', controller=userController, action='GET',    conditions=dict(method=['GET']))
	dispatcher.connect('user_post', '/users/', controller=userController, action='POST',  conditions=dict(method=['POST']))
	dispatcher.connect('user_delete', '/users/', controller=userController,               action='DELETE', conditions=dict(method=['DELETE']))

	dispatcher.connect('user_all_options', '/users/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	
	# Votes w/ uid
	dispatcher.connect('vote_get_uid', '/recommendations/:uid', controller=voteController, action='GET_REC', conditions=dict(method=['GET']))
	dispatcher.connect('vote_put_uid', '/recommendations/:uid',                           controller=voteController, action='PUT_REC', conditions=dict(method=['PUT']))

	dispatcher.connect('vote_options', '/recommendations/:uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	
	# Reset
	dispatcher.connect('reset_index', '/reset/', controller=resetController,              action='PUT_INDEX', conditions=dict(method=['PUT']))
	dispatcher.connect('reset_sid', '/reset/:sid', controller=resetController,            action='PUT_SID', conditions=dict(method=['PUT']))

	dispatcher.connect('reset_all_options', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('reset_options', '/reset/:sid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

	# set up conf
	conf = { 
		'global' : { 
			'server.socket_host' : 'student04.cse.nd.edu',
			'server.socket_port' : 52048 }, 
		'/' : { 
			'request.dispatch': dispatcher,
			'tools.CORS.on': True 
		} 
	}
	
	# start
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == "__main__":
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
