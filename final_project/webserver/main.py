import cherrypy

# create all these
from shows import ShowController
#from users import UserController
from votes import VoteController
from ratings import RatingController
from reset import ResetController

from _tv_database import _tv_database

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()
	
	tdb = _tv_database()
	
	showController = ShowController(tdb)
	#userController = UserController(tdb)
	voteController = VoteController(tdb)
	ratingController = RatingController(tdb=tdb)
	resetController = ResetController(tdb)
	
	''' dispatcher connects '''
	# Shows
	dispatcher.connect('show_get', '/shows/', controller=showController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('show_delete', '/shows/', controller=showController,            action='DELETE', conditions=dict(method=['DELETE']))
	
	# Shows w/ sid
	dispatcher.connect('show_get_sid', '/shows/:sid', controller=showController,       action='GET_SID', conditions=dict(method=['GET']))
	dispatcher.connect('show_put_sid', '/shows/:sid', controller=showController,       action='PUT_SID', conditions=dict(method=['PUT']))
	dispatcher.connect('show_delete_sid', '/shows/:sid', controller=showController,    action='DELETE_SID', conditions=dict(method=['DELETE']))
	
	# Ratings
	dispatcher.connect('rating_get', '/ratings/:sid', controller=ratingController,        action='GET_RATING', conditions=dict(method=['GET']))
	
	# Users w/ uid
#	dispatcher.connect('user_get_uid', '/users/:uid', controller=userController,          action='GET_UID', conditions=dict(method=['GET']))
#    dispatcher.connect('user_delete_uid', '/users/:uid', controller=userController,       action='DELETE_UID', conditions=dict(method=['DELETE']))
	
	# Users
#	dispatcher.connect('user_get', '/users/', controller=userController, action='GET',    conditions=dict(method=['GET']))
#    dispatcher.connect('user_post', '/users/', controller=userController, action='POST',  conditions=dict(method=['POST']))
#    dispatcher.connect('user_delete', '/users/', controller=userController,               action='DELETE', conditions=dict(method=['DELETE']))
	
	# Votes w/ uid
	dispatcher.connect('vote_get_uid', '/recommendations/:uid', controller=voteController, action='GET_REC', conditions=dict(method=['GET']))
	dispatcher.connect('vote_put_uid', '/recommendations/:uid',                           controller=voteController, action='PUT_REC', conditions=dict(method=['PUT']))
	
	# Reset
	dispatcher.connect('reset_index', '/reset/', controller=resetController,              action='PUT_INDEX', conditions=dict(method=['PUT']))
	dispatcher.connect('reset_sid', '/reset/:sid', controller=resetController,            action='PUT_SID', conditions=dict(method=['PUT']))

	conf = { 'global' : { 'server.socket_host' : 'student04.cse.nd.edu', 'server.socket_port' : 52094 }, '/' : { 'request.dispatch': dispatcher } }
	
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == "__main__":
	start_service()
