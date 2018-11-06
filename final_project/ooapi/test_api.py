from _tv_database import _tv_database
import unittest
import os

class TestTVDatabase(unittest.TestCase):

	SID = '35'
	SNAME = "The Killing"
	d = _tv_database()
	showsFile = '../fetch_data/shows.txt'
	usersFile = '../fetch_data/users.txt'
	shows = d.load_tvshows(showsFile)
	users = d.load_users(usersFile)
	
	def reset_data(self):
		self.d.reset_shows(self.showsFile)
	
	def test_get_show(self):
		self.reset_data()
		show = self.d.get_show(self.SID)
		self.assertEqual(show['name'], self.SNAME)
	
	def test_set_show(self):
		self.reset_data()
		self.shows[self.SID]['name'] = 'Avatar: The Last Airbender'
		
		self.d.set_show(self.SID, self.shows[self.SID])
		output = self.d.get_show(self.SID)
		self.assertEqual(output['name'], 'Avatar: The Last Airbender')
	
	def test_delete_shows(self):
		self.reset_data()
		l = self.d.get_shows()
		self.assertEqual(len(l), 240)
		
		self.d.delete_shows()
		l = self.d.get_shows()
		self.assertEqual(len(l), 0)
	
	def test_delete_show(self):
		self.reset_data()
		l = self.d.get_shows()
		self.assertEqual(len(l), 240)
		x = self.d.get_show(self.SID)
		self.assertEqual(x['result'], 'success')
		
		self.d.delete_show(self.SID)
		l = self.d.get_shows()
		self.assertEqual(len(l), 239)
		x = self.d.get_show(self.SID)
		self.assertEqual(x['result'], 'failure')
	
	def test_set_user(self):
		self.reset_data()
		fakeUser = "skumar"
		fakeName = "Shreya Kumar"
		fakePassword = "put_a_pin_in_it"
		x = self.d.get_user(fakeUser)
		self.assertEqual(x, None)
		
		self.d.set_user(fakeUser, fakeName, fakePassword, self.usersFile)
		x = self.d.get_user(fakeUser)
		self.assertEqual(x, fakeName)
		
		x = self.d.get_users()
		self.assertEqual(True, fakeUser in x)
		
		f = open(self.usersFile, "r+")
		g = open("fakeFile", "a+")
		for line in f:
			s = line.rstrip().split(",")[1]
			if s != fakeUser:
				g.write(line)
		f.close()
		os.remove(self.usersFile)
		os.rename("fakeFile", self.usersFile)
		g.close()
	
	def test_set_user_rating(self):
		self.reset_data()
		x = self.d.get_user_rating("pbouchon", self.SID)
		self.assertEqual(x, None)
		self.d.set_user_rating("rkarim", self.SID, 5)
		self.d.set_user_rating("rmcinty3", self.SID, 3)
		self.d.set_user_rating("pbouchon", self.SID, 1)
		x = self.d.get_user_rating("pbouchon", self.SID)
		self.assertEqual(x, 1)
		x = self.d.get_rating(self.SID)
		self.assertEqual(x, 3)
		

if __name__ == "__main__":
	unittest.main()


