import unittest

from segment.segmenter import Analyzer


class TestPySegment(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(True)

    def test_frequency(self):
        s = Analyzer('en')
        self.assertTrue(s.frequency("abe") > 0.0)

    def test_segment(self):
        s = Analyzer('en')
        self.assertEqual(s.segment("AbeLincoln"), ["Abe", "Lincoln"])

    def test_segment_twitter(self):
        s = Analyzer('twitter')
        self.assertEqual(
            s.segment("bieberlovesbeliebers"), ['bieber', 'loves',
                                                'beliebers'])

    def test_segment_anchor(self):
        s = Analyzer('anchor')
        self.assertEquals(
            s.segment("wordpress&sex"), ['wordpress', '&', 'sex'])


if __name__ == '__main__':
    unittest.main()
