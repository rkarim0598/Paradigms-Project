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
			components = line.split(":")
			'''
			etc
			'''
			self.tvshows[tvid] = ''' SOMETHING '''
		return self.tvshows
