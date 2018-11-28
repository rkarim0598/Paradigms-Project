import unittest
import requests
import json

class TestReset(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52048'
	RESET_URL = SITE_URL + '/reset/'
	SHOWS_URL = SITE_URL + '/shows/'

	def test_reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, data = json.dumps(m))
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
	
	def test_reset_show(self):
		m = {}
		r = requests.get(self.SHOWS_URL + str(1))
		r = json.loads(r.text)['output']
		self.assertEqual(r['name'], 'Under the Dome')
		r['name'] = 'Something Else'
		r = requests.put(self.SHOWS_URL + str(1), data = json.dumps(r))
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
		r = requests.get(self.SHOWS_URL + str(1))
		r = json.loads(r.text)['output']
		self.assertEqual(r['name'], 'Something Else')
		r = requests.put(self.RESET_URL + str(1), data = json.dumps(m))
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
		r = requests.get(self.SHOWS_URL + str(1))
		r = json.loads(r.text)['output']
		self.assertEqual(r['name'], 'Under the Dome')
		

if __name__ == "__main__":
	unittest.main()
