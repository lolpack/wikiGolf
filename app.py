from flask import Flask, render_template, request, Response, redirect, url_for # Flask module
import jinja2 #Templating

import wikipedia as W #Main wikipedia module leveraged for wikipedia API calls
import pymongo #Mongo connection

###Helpers###
import json 
import string, re 
import random
import os

#Flask and Mongo Setup

app = Flask(__name__)

from pymongo import MongoClient

MONGO_URL = os.environ.get('MONGOHQ_URL')
 
if MONGO_URL:
    # Get a connection
    client = MongoClient(MONGO_URL)

    # Get the database
    db= client.get_default_database()
else:
    # Not on an app with the MongoHQ add-on, do some localhost action
    client = MongoClient('localhost', 27017)
    db = client['wikiGolf']

preCourses = db.preLoadedCourses

print preCourses.find_one()

class WikiPage():
	"""Represents wikipedia page. Responsible for loading pages
	and getting links, html and title for each page"""


	def __init__(self):
		self.pageCon = None

	def loadRandWikiPage(self):
		"""Grabs a random wiki page for start and end of course.
		Returns tuple: links first position, title second"""

		try:
			Random1 = W.random()
			self.randomPage = W.page(Random1) #If first random page throws ambiguity error, try again
		except:
			self.loadRandWikiPage()

		if self.randomPage.title:
			return self.randomPage.links, self.randomPage.title
		else:
			print "Not valid"

	def loadGivenWikiPage(self, page, preloaded = False):
		"""Grabs a specified wiki page.
		Returns tuple: links first position, title second"""

		self.Page = W.page(page)

		if self.Page.title:
			print type(self.Page.title)
			self.pageCon = self.Page.html()
			return self.Page.links, self.Page.title
		else: 
			print "Not Valid"

	def contentWithLinks(self, page):
		"""Goes through the list of links associated with a  page
		and finds the instances of those words in a plain text version
		of the page."""

		links, title = self.loadGivenWikiPage(page)
		pageContent = self.pageCon

		pageContent = pageContent.replace( 'wiki/', "#wiki/")
		#pageContent = pageContent.replace( '<span class="mw-editsection"', "")
		
		img = re.compile(r'<img.*?/>')
		audio = re.compile(r'<audio.*?</audio>')
		edit = re.compile(r'<span class="mw-editsection".*?]</span>')
		pageContent = img.sub('', pageContent)
		pageContent = audio.sub('', pageContent)
		pageContent = edit.sub('', pageContent)
		return pageContent

class Game():
	"""Represents state of the game. Responsible for starting the game,
	clearing the board and interacting with the Wikipage class"""


	def __init__(self, Wiki, user):
		self.W = Wiki
		self.user = user
		self.coursePath = [] #List of objects containg course name and all links associated with that page.
		self.courseHTML = [] #list of HTML for a given course (single strings)
		self.startPage = None
		self.startLinks = None
		self.endPage = None

	
	def startGame(self, Random = True, par = None): 
		"""Picks a start and end point based on two randomly generated wiki pages"""
		if Random:
			self.startLinks, self.startPage = self.W.loadRandWikiPage() #First random wiki page for initial course load
			links, self.endPage = self.W.loadRandWikiPage() #Page that the user needs to end up on
			self.courseHTML.append(self.startPage)
		else: 
			courses = preCourses.find_one({"par":par})
			print "Courses" + str(len(courses['courses']))
			course = courses['courses'][random.randrange(len(courses['courses'])-1)]
			self.endPage = course['finish']
			self.startLinks, self.startPage = self.W.loadGivenWikiPage(course['start'])
			self.courseHTML.append(self.startPage)

	def checkWinner(self):
		if self.title == self.endPage:
			return True
		else:
			return False

	def makeWikiObjects(self, random = False): #Creats a dictionary of links
		if random:
			links, self.title = self.startLinks, self.startPage #Returns dict for a random page
			content = self.W.contentWithLinks( self.startPage )
		else: 
			page = self.courseHTML[len(self.courseHTML)-1] 
			withUnderscores = string.replace(page  , " " , "_" ) #Returns dict for a given page
			links, self.title =  WP.loadGivenWikiPage( withUnderscores )
			content = self.W.contentWithLinks( page )
		self.listObjects = []
		self.listObjects.append({"id": 1, "current": self.title, "startPage":self.startPage,
									 "endPage": self.endPage, "gameOver" : self.checkWinner(), "coursePath": self.courseHTML,
									 "courseContent": content})
		return self.listObjects

	def clearGame(self):
		self.user.strokes = 0
		self.coursePath = []
		self.courseHTML = []

class User:
	"""Represents a user in the game and her/his profile. This section to be filled out more completely 
	as user profile functionality is built out"""

	def __init__(self):
		self.strokes = 0
		self.history = {"courseHistory": [None]}


WP = WikiPage()
user = User()
game = Game(WP, user)

###Application routes and main game logic###

@app.route("/")
def main():

	game.clearGame()
	return render_template('index.html')

@app.route("/user", methods = ['POST', 'GET']) #End point for AJAX calls to get user data
def getJSON():

	if request.method == 'POST':
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps({"strokes": user.strokes}), content_type='application/json')

@app.route("/nextWiki", methods= ['POST', 'GET']) #Route when you choose a course or click a link to the next page
def nextWiki():

	if request.method == 'POST':
		if request.json["next"] == 'random': #Random course
			game.startGame()
			game.coursePath.append(game.makeWikiObjects(random = True))
		elif request.json["next"].startswith('par'): #Pre loaded (par) course
			par = int(request.json["next"][-1])
			game.startGame(Random= False, par=par)
			game.coursePath.append(game.makeWikiObjects(random = False))
		else:
			game.courseHTML.append(request.json["next"]) #When a specific link is click on to load the next wikiPage
			game.coursePath.append(game.makeWikiObjects())
			user.strokes += 1
		return "Success!"

	elif request.method == 'GET':
		return Response(json.dumps(game.coursePath.pop()), content_type='application/json') 
		#Return JSON data from game course array

@app.route("/fist", methods = ['GET']) #Not used for production. Used to test raw html output with 'test.html' page
def firstCourse():

	test = WP.contentWithLinks()
	return render_template('test.html', test = test)

if __name__ == "__main__":
	app.run(debug=True, host = '0.0.0.0', port = int(os.environ.get('PORT', 5000)))

