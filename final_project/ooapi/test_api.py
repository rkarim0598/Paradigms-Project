from _tv_database import _tv_database
import unittest

class TestTVDatabase(unittest.TestCase):

        SID = '35'
        SNAME = "The Killing"
        d = _tv_database()
        showsFile = '../fetch_data/shows.txt'
        shows = d.load_tvshows(showsFile)

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
                
if __name__ == "__main__":
        unittest.main()
		


