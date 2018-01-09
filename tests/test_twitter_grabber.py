from unittest import TestCase
from MyTweets import twitter_grabber


class test_twitter_grabber(TestCase):

    def setUp(self):
        self.twitter = twitter_grabber

    def test_check_status_true(self):
        tf = self.twitter.check_status(200)
        self.assertEquals(tf, True)

    def test_check_status_false(self):
        tf = self.twitter.check_status(100)
        self.assertEquals(tf, False)
        tf = self.twitter.check_status(300)
        self.assertEquals(tf, False)
        tf = self.twitter.check_status(400)
        self.assertEquals(tf, False)
