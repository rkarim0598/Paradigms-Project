import unittest
import requests
import json

class TestRatings(unittest.TestCase):
	SITE_URL = 'http://student04.cse.nd.edu:52048'
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, data = json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False
			
	def test_ratings_get(self):
		self.reset_data() # this reset causing issues with server
		sid = 216

		r = requests.get(self.RATINGS_URL + str(sid))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['rating'], '9.4')

if __name__ == "__main__":
	unittest.main()
