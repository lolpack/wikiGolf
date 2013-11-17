from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
import string
import pymongo

#Flask and Mongo Setup

app = Flask(__name__)

"""from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
db= client.wikiGolf
posts = db.preLoadedCourses


print db.collection_names()"""

class WikiPage():


	def loadRandWikiPage(self):
		"""Grabs a random wiki page for start and end of course"""

		random = W.random()
		self.randomPage = W.page(random)
		if self.randomPage.title:
			print self.randomPage.title
			print type(self.randomPage.title)
			return self.randomPage.links, self.randomPage.title
		else:
			"Not valid"

	def loadGivenWikiPage(self, page):
		"""Grabs a specified wiki page"""

		self.Page = W.page(page)
		print self.Page.title
		return self.Page.links, self.Page.title

class Game():

	def __init__(self, Wiki):
		self.W = Wiki
		self.coursePath = [] #list of links that user clicked on
		self.courseLinks = [] #List of objects 
		self.startPage = None
		self.endPage = None

	
	def startGame(self):
		self.startPage = self.W.loadRandWikiPage() #First random wiki page for initial course load
		self.endPage = self.W.loadRandWikiPage() #Page that the user needs to end up on
		self.courseLinks.append(self.startPage[1])

	def checkWinner(self):
		if self.coursePath[len(self.coursePath) - 1] == self.endPage:
			return True
		else:
			return False

	def makeWikiObjects(self, random = False): #Creats a dictionary of links
		if random:
			links, title = self.startPage #Returns dict for a random page
		else: 
			withUnderscores = string.replace(self.courseLinks[len(self.courseLinks)-1]  , " " , "_" ) #Returns dict for a given page
			links, title =  WP.loadGivenWikiPage( withUnderscores )
		self.listObjects = []
		id = 1
		for link in links:
			self.listObjects.append({"id":id, "name":link, "current": title, "startPage":self.startPage[1],
									 "endPage": self.endPage[1]})
			id += 1
		return self.listObjects

WP = WikiPage()
game = Game(WP)







@app.route("/")
def main():
	return render_template('index.html')


@app.route("/users", methods = ['POST', 'GET'])
def getJSON():
	if request.method == 'POST':
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(dab), content_type='application/json')

@app.route("/nextWiki", methods= ['POST', 'GET']) #Route when you choose a course or click a link to the next page
def nextWiki():
	print request.json
	if request.method == 'POST':
		if request.json["next"] == 'random':
			game.startGame()
			game.coursePath.append(game.makeWikiObjects(random = True))
		elif request.json["next"].startswith('par'):
			game.startGame()
			game.coursePath.append(game.makeWikiObjects(random = True))
		else:
			game.courseLinks.append(request.json["next"])
			game.coursePath.append(game.makeWikiObjects())
		print "Course path: "+ str(game.courseLinks)
		print game.checkWinner()
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(game.coursePath.pop()), content_type='application/json')

@app.route("/fistCourse", methods = ['GET']) #Deprecated
def firstCourse():
	if request.method == 'GET':
		if request.json == 'par1':
			t = posts.find_one()
			pager.append(t['par1'][0])
			return Response(json.dumps(makeWikiObjects()), content_type='application/json')

if __name__ == "__main__":
	app.run(debug = True)

