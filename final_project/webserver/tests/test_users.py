import unittest
import requests
import json

class TestUsers(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52048'
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

	def test_users_get_uid(self):
		self.reset_data()
		user_id = 'pbouchon'
		r = requests.get(self.USERS_URL + str(user_id))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['pname'], 'Patrick Bouchon')

	def test_users_get(self):
		self.reset_data()
		r = requests.get(self.USERS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['output'], ["rkarim", "rmcinty3", "pbouchon"])

	def test_users_index_post(self):
		self.reset_data()

		m = {}
		m['pname'] = 'Test Test'
		m['uname'] = 'testtest9'
		m['password'] = 'password'
		r = requests.post(self.USERS_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USERS_URL + 'testtest9')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['pname'], 'Test Test')

		r = requests.delete(self.USERS_URL + 'testtest9', data = json.dumps({}))

	def test_users_delete_uid(self):
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

		m = {}
		m['pname'] = 'Patrick Bouchon'
		m['uname'] = 'pbouchon'
		m['password'] = 'peppermint'
		r = requests.post(self.USERS_URL, data = json.dumps(m))

	def test_users_delete_all(self):
		self.reset_data()

		m = {}
		r = requests.delete(self.USERS_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.USERS_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['output'], [])

if __name__ == "__main__":
	unittest.main()
