from flask import Flask, render_template, Markup, request, Response, redirect, url_for
import jinja2
import wikipedia as W
import json
import string
import pymongo
import random
import os

#Flask and Mongo Setup


app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(os.environ['MONGOHQ_URL'])
db= client.wikiGolf
preCourses = db.preLoadedCourses


class WikiPage():

	def __init__(self):
		self.pageCon = None

	def loadRandWikiPage(self):
		"""Grabs a random wiki page for start and end of course.
		Returns tuple: links first position, title second"""


		try:
			Random1 = W.random()
			self.randomPage = W.page(Random1)
		except:
			Random1 = W.random()
			self.randomPage = W.page(Random1)

		if self.randomPage.title:
			print type(self.randomPage.title)
			self.pageCon = self.randomPage.content
			return self.randomPage.links, self.randomPage.title
		else:
			print "Not valid"

	def loadGivenWikiPage(self, page):
		"""Grabs a specified wiki page.
		Returns tuple: links first position, title second"""

		try:
			self.Page = W.page(page)
		except:
			self.Page = W.page(page)

		if self.Page.title:
			print type(self.Page.title)
			self.pageCon = self.Page.content
			return self.Page.links, self.Page.title
		else: 
			print "Not Valid"

	def contentWithLinks(self, page = None, Random = True):
		"""Goes through the list of links associated with a  page
		and finds the instances of those words in a plain test version
		of the page."""

		if Random:
			links, title = self.loadRandWikiPage()
			pageContent = self.pageCon
			for link in links:
				if link in pageContent:
					pageContent = pageContent.replace( link, u"<a href='#wiki/{link}'>{link}</a>".format(link=link)).encode("utf-8")
		else:
			links, title = self.loadGivenWikiPage(page)
			pageContent = self.pageCon
			for link in links:
				if link in pageContent:
					pageContent = pageContent.replace( link, u"<a href='#wiki/{link}'>{link}</a>".format(link=link)).encode("utf-8")
		return pageContent

class Game():

	def __init__(self, Wiki, user):
		self.W = Wiki
		self.user = user
		self.coursePath = [] #List of objects containg course name and all links associated with that page.
		self.courseLinks = [] #list of title (single strings) that user clicked on
		self.startPage = None
		self.startLinks = None
		self.endPage = None

	
	def startGame(self, Random = True, par = None): 
		"""Picks a start and end point based on two randomly generated wiki pages"""
		if Random:
			self.startLinks, self.startPage = self.W.loadRandWikiPage() #First random wiki page for initial course load
			links, self.endPage = self.W.loadRandWikiPage() #Page that the user needs to end up on
			self.courseLinks.append(self.startPage)
		else: 
			courses = preCourses.find_one({"par":par})
			print "Courses" + str(len(courses['courses']))
			course = courses['courses'][random.randrange(len(courses['courses'])-1)]
			self.startLinks, self.startPage = self.W.loadGivenWikiPage(course['start']) #Should this grab pages or passed in as an arg??
			endLinks, self.endPage = self.W.loadGivenWikiPage(course['finish']) #endLinks unused
			self.courseLinks.append(self.startPage)

	def checkWinner(self):
		if self.title == self.endPage:
			return True
		else:
			return False

	def makeWikiObjects(self, random = False): #Creats a dictionary of links
		if random:
			links, self.title = self.startLinks, self.startPage #Returns dict for a random page
			page = None
		else: 
			page = self.courseLinks[len(self.courseLinks)-1] 
			withUnderscores = string.replace(page  , " " , "_" ) #Returns dict for a given page
			links, self.title =  WP.loadGivenWikiPage( withUnderscores )
		self.listObjects = []
		id = 1
		for link in links:
			self.listObjects.append({"id":id, "name":link, "current": self.title, "startPage":self.startPage,
									 "endPage": self.endPage, "gameOver" : self.checkWinner(), "coursePath": self.courseLinks,
									 "courseContent": None}) #"self.W.contentWithLinks()"
			id += 1
		return self.listObjects

class User:

	def __init__(self):
		self.strokes = 0
		self.history = {"courseHistory": [None]}


WP = WikiPage()
user = User()
game = Game(WP, user)







@app.route("/")
def main():
	game.courseLinks = []
	user.strokes = 0
	return render_template('index.html')



@app.route("/user", methods = ['POST', 'GET'])
def getJSON():
	if request.method == 'POST':
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps({"strokes": user.strokes}), content_type='application/json')

@app.route("/nextWiki", methods= ['POST', 'GET']) #Route when you choose a course or click a link to the next page
def nextWiki():
	print request.json
	if request.method == 'POST':
		if request.json["next"] == 'random':
			game.startGame()
			game.coursePath.append(game.makeWikiObjects(random = True))
		elif request.json["next"].startswith('par'):
			par = int(request.json["next"][-1])
			game.startGame(Random= False, par=par)
			game.coursePath.append(game.makeWikiObjects(random = False))
		else:
			game.courseLinks.append(request.json["next"])
			game.coursePath.append(game.makeWikiObjects())
			user.strokes += 1
		print "Course path: "+ str(game.courseLinks)
		print "Winner?????" + str(game.checkWinner())
		
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(game.coursePath.pop()), content_type='application/json') #Return JSON data from game course array

@app.route("/fistCourse", methods = ['GET']) #Deprecated
def firstCourse():
	if request.method == 'GET':
		if request.json == 'par1':
			t = posts.find_one()
			pager.append(t['par1'][0])
			return Response(json.dumps(makeWikiObjects()), content_type='application/json')

if __name__ == "__main__":
	app.run(host = '0.0.0.0')
