import unittest
import requests
import json

class TestUsers(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52094' #replace with your port number
	USERS_URL = SITE_URL + '/users/'
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

	def test_users_get(self):
		self.reset_data()
		user_id = 'pbouchon'
		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['pname'], 'Patrick Bouchon')

	def test_users_delete(self):
		self.reset_data()
		user_id = 'pbouchon'

		m = {}
		r = requests.delete(self.USERS_URL + str(user_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
	unittest.main()

