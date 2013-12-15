#Unit tests for Flask app

from app import WikiPage, Game, User
import unittest
from pymongo import MongoClient
import wikipedia as W 

###STUB mongo DB###

client = MongoClient('localhost', 27017)
db = client['wikiGolf']

preCourses = db.preLoadedCourses
usersDB = db.users

class TestWikiGolf(unittest.TestCase):

	def setUp(self):
		self.WP = WikiPage()
		self.User = User(usersDB) ##not testing user yet
		self.Game = Game(self.WP, self.User)


		"""Tests for WikiPage Class"""

	def testRandomWiki(self):
		"""Tests that a Wikipedia page is succesfully loaded"""
		randomPage = self.WP.loadRandWikiPage()
		self.assertTrue(randomPage)

	def testGivenPagePass(self):
		"""Tests that a specific Wikipedia page is succesfully loaded"""
		givenPage = self.WP.loadGivenWikiPage('Vegetarian_bacon')
		self.assertEqual(givenPage[1], 'Vegetarian bacon')

		self.assertEqual(self.WP.pageCon, baconHTML)

	def testGivenPageFail(self):
		"""Tests that an ambiguos page returns the proper HTML informing
		the user that something has gone wrong"""
		givenPage = self.WP.loadGivenWikiPage('Italian')
		self.assertEqual(givenPage[1], "Unavailable")
		self.assertEqual(self.WP.pageCon, unavailable)

	def testContentWithLinks(self):
		"""Tests to make sure that the html is having all the href's changed for backbone
		and having the right tags left out."""
		pageContent = self.WP.contentWithLinks('Vegetarian_bacon')
		self.assertTrue(pageContent)

	"""Tests for Game class"""
	
	def testStartGameRandom(self):
		"""Ensures that the HTML for a random course is added to the courseHTML list
		when method is called"""
		self.Game.startGame(Random = True)
		self.assertTrue(self.Game.courseHTML[0])
		self.assertTrue(self.Game.startPage)
		self.assertTrue(self.Game.endPage)

	def testStartGamenotRandom(self):
		"""Ensures that the HTML for a course loaded from Mongo is added to the courseHTML list
		when method is called"""
		self.Game.startGame(Random = False, par = 3)
		self.assertTrue(self.Game.courseHTML[0])
		self.assertTrue(self.Game.startPage)
		self.assertTrue(self.Game.endPage)

	def testCheckWinnerTrue(self):
		"""Tests if the current path is the same as the end path. If so, return True"""
		self.Game.title = 'Vegetarian bacon'
		self.Game.endPage = 'Vegetarian bacon'
		gameState = self.Game.checkWinner()
		self.assertTrue(gameState)

	def testMakeWikiObjectsRandom(self):
		"""Test that the wikiObject for a Random page that is sent to the client is created and formatted properly"""
		self.Game.startPage = 'Vegetarian_bacon'
		self.Game.startLinks = ["homestarrunner.com"]
		objects = self.Game.makeWikiObjects(random=True)
		self.assertEqual(objects[0]['id'], 1)
		self.assertEqual(objects[0]['startPage'], 'Vegetarian_bacon')
		self.assertEqual(objects[0]['endPage'], None)
		self.assertEqual(objects[0]['gameOver'], False)
		self.assertEqual(objects[0]['coursePath'], [])
		self.assertTrue(objects[0]['courseContent'])

	def testMakeWikiObjectsNotRandom(self):
		"""Test that the wikiObject for a given page that is sent to the client is created and formatted properly"""
		self.Game.courseHTML = ['Vegetarian_bacon']
		self.Game.startPage = 'Vegetarian_bacon'
		objects = self.Game.makeWikiObjects(random=True)
		self.assertEqual(objects[0]['id'], 1)
		self.assertEqual(objects[0]['startPage'], 'Vegetarian_bacon')
		self.assertEqual(objects[0]['endPage'], None)
		self.assertEqual(objects[0]['gameOver'], False)
		self.assertEqual(objects[0]['coursePath'], ['Vegetarian_bacon'])
		self.assertTrue(objects[0]['courseContent'])

	def testClearGame(self):
		"""Makes sure that the function clears the strokes, coursePath and courseHtml"""
		self.User.strokes = 10
		self.Game.coursePath = ['oh', 'hai', 'there']
		self.Game.courseHtml = '<html> My awesome website </html>'
		self.Game.clearGame()
		self.assertEqual(self.User.strokes, 0)
		self.assertEqual(self.Game.coursePath, None)
		self.assertEqual(self.Game.courseHTML, [])

###TEST STRINGS###


baconHTML = W.page('Vegetarian_bacon').html()

unavailable = "Barnacles! This page is unavailable through the API. Please try <a href='/'> starting over </a>."


if __name__ == '__main__':
    unittest.main()