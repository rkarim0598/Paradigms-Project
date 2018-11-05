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
	def __init__(self):
		self.tvshows = {}
	
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
                        
		return self.tvshows
        
        def get_show(self, sid):
                sid = str(sid)
                
                if sid in self.tvshows:
                        output = self.tvshows[sid]
                        output['result'] = 'success'
                else:
                        output = { 'result': 'failure' }

                return output

        def set_show(self, sid, d = {}):
                if len(d) == 6:
                        self.tvshows[sid] = d

        def get_shows(self):
                return [i for i in self.tvshows.keys()]

        def reset_shows(self):
                self.tvshows = load_tvshows('shows.txt')

        def delete_shows(self):
                self.tvshows = {}

        def delete_show(self, sid):
                if sid in self.tvshows:
                        self.tvshows.pop(sid)
