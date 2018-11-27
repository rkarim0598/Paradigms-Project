import unittest
import requests
import json

class TestShows(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:52094'
	SHOWS_URL = SITE_URL + '/shows/'
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

	def test_shows_get(self):
		self.reset_data()
		show_id = 1
		r = requests.get(self.SHOWS_URL + str(show_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		output = resp['output']
		episodes = resp['episodes']
		self.assertEqual(output['name'], 'Under the Dome')
		self.assertEqual(output['genres'], 'Drama|Science-Fiction|Thriller')
		self.assertEqual(output['site'], 'http://www.cbs.com/shows/under-the-dome/')
		self.assertEqual(output['rating'], '6.5')
		self.assertEqual(output['image'], 'http://static.tvmaze.com/uploads/images/medium_portrait/0/1.jpg')
		self.assertEqual(output['summary'][0:7], '<p><b>U')
		self.assertEqual(episodes[0]['season'], 1)
		self.assertEqual(episodes[0]['name'], 'Pilot')
		self.assertEqual(episodes[0]['number'], 1)
		self.assertEqual(episodes[0]['image'], 'http://static.tvmaze.com/uploads/images/medium_landscape/1/4388.jpg')
		self.assertEqual(episodes[0]['summary'][0:4], '<p>W')

	def test_shows_put(self):
		self.reset_data()
		show_id = 1

		r = requests.get(self.SHOWS_URL + str(show_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['output']['name'], 'Under the Dome')

		m = resp['output']
		m['name'] = 'Something Else'
		r = requests.put(self.SHOWS_URL + str(show_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.SHOWS_URL + str(show_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['output']['name'], 'Something Else')

	def test_shows_delete(self):
		self.reset_data()
		show_id = 1

		m = {}
		r = requests.delete(self.SHOWS_URL + str(show_id), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.SHOWS_URL + str(show_id))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')
	
	def test_shows_get_all(self):
		self.reset_data()
		
		r = requests.get(self.SHOWS_URL)
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
		self.assertEqual(r['output'][0]['name'], 'Under the Dome')
		self.assertEqual(len(r['output']), 240)
	
	def test_shows_delete_all(self):
		self.reset_data()
		
		m = {}
		r = requests.delete(self.SHOWS_URL, data = json.dumps(m))
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
		
		r = requests.get(self.SHOWS_URL)
		r = json.loads(r.text)
		self.assertEqual(r['result'], 'success')
		self.assertEqual(len(r['output']), 0)
	
if __name__ == "__main__":
	unittest.main()

