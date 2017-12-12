import unittest
import mediacloud
from app import MediaCloud

class MediaCloudAccessTest(unittest.TestCase):

    def setUp(self):
        self.mediacloud = MediaCloud() #ElectionResults('election_results_test_file.csv')

    def testLoad(self):
        assert self.mediacloud.mc is not None
        assert isinstance(self.mediacloud.mc, mediacloud.api.MediaCloud) is True
        #assert len(self.results.all_lines) > 0
    #
    # def testStateCount(self):
    #     self.results.load()
    #     state_count = self.results.state_count()
    #     assert state_count==2
    #
    # def testStates(self):
    #     self.results.load()
    #     names = self.results.states()
    #     assert len(names)==2
    #     assert names[0]=='Alaska'
    #     assert names[1]=='Alabama'


    def test_numbers_3_4(self):
        self.assertEqual( 1+1, 2)

    def test_strings_a_3(self):
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()
