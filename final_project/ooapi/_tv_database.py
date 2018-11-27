'''
Ryker McIntyre
Rayyan Karim
Patrick Bouchon

TV Database Class

October 30, 2018
'''

import requests
import json

class _tv_database:
	# Constructor
	def __init__(self):
		self.tvshows = {}
		self.users	 = {}
		self.ratings = {}
		self.userRatings = {}
	
	# Loads all the tv shows from file, returns dict of tv shows
	def load_tvshows(self, tvshows_file):
		f = open(tvshows_file)
		self.tvshows = {}
		for line in f:
			line = line.rstrip()
			components = line.split("::")

			self.tvshows[components[0]] = {}
			self.tvshows[components[0]]['name'] = components[1]
			self.tvshows[components[0]]['genres'] = components[2]
			self.tvshows[components[0]]['site'] = components[3]
			self.tvshows[components[0]]['rating'] = components[4]
			self.tvshows[components[0]]['image'] = components[5]
			self.tvshows[components[0]]['summary'] = components[6]
		f.close()
		
		return self.tvshows
	
	# Get show by show id, add a result field
	def get_show(self, sid):
		sid = str(sid)
		
		if sid in self.tvshows:
			output = self.tvshows[sid]
			output['result'] = 'success'
		else:
			output = { 'result': 'failure' }
		
		return output
	
	# Set a show to something else (or add a show)
	def set_show(self, sid, d = {}):
		sid = str(sid)
		if len(d) == 6:
			self.tvshows[sid] = d
			self.tvshows[sid]['rating'] = self.tvshows[sid]['rating']
	
	# Get all show ids
	def get_shows(self):
		return [i for i in self.tvshows.keys()]
	
	# Reset all shows, return the new dictionary of shows
	def reset_shows(self, fname):
		self.tvshows = self.load_tvshows(fname)
		return self.tvshows
	
	# Delete all shows from database
	def delete_shows(self):
		self.tvshows = {}
	
	# Delete a show from the database by sid
	def delete_show(self, sid):
		sid = str(sid)
		if sid in self.tvshows:
			self.tvshows.pop(sid)
	
	# Load all users who have logged in before (from a file)
	def load_users(self, user_file):
		f = open(user_file)
		self.users = {}
		for line in f:
			line = line.rstrip()
			components = line.split(",")
			pname = components[0]
			uname = components[1]
			self.users[uname] = pname

		return self.users
	
	# Return a list of all usernames
	def get_users(self):
		return [i for i in self.users.keys()]
	
	# Get the name of a user by their username
	def get_user(self, uid):
		if uid in self.users:
			return self.users[uid]
		else:
			return None
	
	# Create a new user with a username, name, and a password (and add to file)
	def set_user(self, uid, pname, password, user_file):
		self.users[uid] = pname
		f = open(user_file, 'a')
		f.write(pname + ',' + uid + ',' + password + '\n')
		f.close()
	
	# Submit a new rating for a user
	def set_user_rating(self, uid, sid, rating):
		uid = str(uid)
		sid = str(sid)
		rating = int(rating)

		if uid in self.userRatings:
			self.userRatings[uid][sid] = rating
		else:
			self.userRatings[uid] = dict()
			self.userRatings[uid][sid] = rating

	# Get what the user rated a specific show
	def get_user_rating(self, uid, sid):
		if str(sid) in self.tvshows and self.userRatings[str(uid)] != {} and str(uid) in self.userRatings:
			return self.userRatings[uid][sid]
		else:
			return None

	# Submit a new rating for a user
	#def set_user_rating(self, uid, sid, rating):
	#	sid = str(sid)
	#	if sid in self.ratings:
	#		self.ratings[sid][uid] = rating
	#	else:
	#		self.ratings[sid] = {uid:rating}
	
	# Get what the user rated a specific show
	#def get_user_rating(self, uid, sid):
	#	if str(sid) in self.ratings and uid in self.ratings[str(sid)]:
	#		return self.ratings[str(sid)][uid]
	#	else:
	#		return None

	# Delete a user from the database by uid
	def get_rating(self, sid):
		sid = str(sid)
		info = self.get_show(sid)
		if info['result'] == 'success':
			if info['rating'] == 'None':
				return 0
			return info['rating']
		else:
			return 0

	# delete all ratings for every show
	def delete_ratings(self):
		for uid in self.userRatings:
			self.userRatings[uid] = {}

	def get_recommendation(self, uid):
		ratmax = 0
		maxid = -1
		uid = str(uid)
		showList = self.get_shows()
		userList = []

		if self.userRatings[uid]:
			for show in self.userRatings[uid]:
				userList.append(show)
	
		if len(userList) > 0:
			for sid in showList:
				sid = str(sid)
				if sid not in userList:
					rating = float(self.get_rating(sid))
					if rating > ratmax:
						ratmax = rating
						maxid = int(sid)
					elif rating == ratmax and int(sid) < maxid:
						maxid = int(sid)
		else:
			for sid in showList:
				sid = str(sid)
				rating = float(self.get_rating(sid))
				if rating > ratmax:
					ratmax = rating
					maxid = int(sid)
				elif rating == ratmax and int(sid) < maxid:
					maxid = int(sid)
		return str(maxid)
 
	def delete_user(self, uid):
		sid = str(uid)
		if uid in self.users:
			self.users.pop(uid)

	# reset show to original content
	def reset_show(self, sid, tvshows_file):
		sid = str(sid)

		# open tvshows_file and get data from there
		f = open(tvshows_file, "r")

		# parse
		for line in f:
			line = line.rstrip()
			if sid == line.split("::")[0]:
				components = line.split("::")

				# assign original content
				self.tvshows[sid] = {}
				self.tvshows[sid]['name'] = components[1]
				self.tvshows[sid]['genres'] = components[2]
				self.tvshows[sid]['site'] = components[3]
				self.tvshows[sid]['rating'] = components[4]
				self.tvshows[sid]['image'] = components[5]
				self.tvshows[sid]['summary'] = components[6]

		# close stream
		f.close()

	# get list of all episodes from every season for given show w/ sid
	def get_episodes(self, sid):
		# get data from api and decode
		r = requests.get('http://api.tvmaze.com/shows/' + str(sid) + '?embed=episodes').content.decode()
		d = json.loads(r)
		episodes = []

		# parse each entry
		for episode in d['_embedded']['episodes']:
			season = episode['season']
			name = episode['name']
			number = episode['number']
			image = episode['image']['medium']
			summary = episode['summary']
			episodes.append({'season':season,'name':name,'number':number,'image':image,'summary':summary})
		
		return episodes

