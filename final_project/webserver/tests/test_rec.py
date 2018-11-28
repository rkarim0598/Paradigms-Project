import unittest
import requests
import json

class TestRecommendations(unittest.TestCase):
	SITE_URL = 'http://student04.cse.nd.edu:52048'
	RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
	RATINGS_URL = SITE_URL + '/ratings/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_recommendations_get(self):
		self.reset_data()
		uid = "rkarim"
		r = requests.get(self.RECOMMENDATIONS_URL + uid)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['sid'], '216')

	def test_recommendations_put(self):
		self.reset_data()
		uid = "rkarim"
		sid = "216"
		rating = 4

		s = {}
		s['sid'] = sid
		s['rating'] = rating

		r = requests.put(self.RECOMMENDATIONS_URL + uid, data = json.dumps(s))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.RECOMMENDATIONS_URL + uid)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['sid'], '82')

if __name__ == "__main__":
	unittest.main()
