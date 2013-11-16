from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
import string
import pymongo

#Flask and Mongo Setup

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
db= client.wikiGolf
posts = db.preLoadedCourses


print db.collection_names()

class WikiPage():


	def loadRandWikiPage(self):
		"""Grabs a random wiki page for start and end of course"""

		random = W.random()
		self.randomPage = W.page(random)
		print type(self.randomPage.title)
		return self.randomPage.links, self.randomPage.title

	def loadGivenWikiPage(self, page):
		"""Grabs a specified wiki page"""

		self.Page = W.page(page)
		print self.Page.title
		return self.Page.links, self.Page.title

WP = WikiPage()

links1, title1 = WP.loadRandWikiPage() #First random wiki page for initial course load
links2, title2 = WP.loadRandWikiPage() #Page that the user needs to end up on


firstPage = title1


resp = []

pager = [firstPage] #list of links that user clicked on

coursePath = {"startPage": firstPage, "endPage": title2}


def makeWikiObjects(random = False): #Creats a dictionary of links
	if random:
		links, title = WP.loadRandWikiPage() #Returns dict for a random page
	else: 
		withUnderscores = string.replace(pager[len(pager)-1]  , " " , "_" ) #Returns dict for a given page
		links, title =  WP.loadGivenWikiPage( withUnderscores )
	listObjects = []
	id = 1
	for link in links:
		listObjects.append({"id":id, "name":link, "current": title})
		id += 1
	return listObjects



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
			resp.append(makeWikiObjects(random = True))
		elif request.json["next"].startswith('par'):
			resp.append(makeWikiObjects(random = True))
		else:
			pager.append(request.json["next"])
			resp.append(makeWikiObjects())
		print resp
		print pager
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(resp[len(resp)-1]), content_type='application/json')

@app.route("/fistCourse", methods = ['GET'])
def firstCourse():
	if request.method == 'GET':
		if request.json == 'par1':
			t = posts.find_one()
			pager.append(t['par1'][0])
			return Response(json.dumps(makeWikiObjects()), content_type='application/json')

if __name__ == "__main__":
	app.run(debug = True)

