from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
import string

app = Flask(__name__)

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

links, title = WP.loadRandWikiPage() #First random wiki page for initial course load

firstPage = title

pager = [firstPage] #list of links that user clicked on

coursePath = []


def makeWikiObjects(): #Called after user clicks a link. Fetchs next batch of links for that page.
	withUnderscores = string.replace(pager[len(pager)-1]  , " " , "_" )
	links, t =  WP.loadGivenWikiPage( withUnderscores )
	listObjects = []
	id = 1
	for link in links:
		listObjects.append({"id":id, "name":link})
		id += 1
	return listObjects

dab = [{"id":1,  "name": "First", "facebookPointer": None},
		{"id": 2, "name": "John"},
		{"id": 3, "name": links}]

@app.route("/")
def main():
	entries = {"title": "wikiGolf", "wikiPage": title, "wikiTitle": title, "links" : links }
	return render_template('index.html', entries=entries)


@app.route("/users", methods = ['POST', 'GET'])
def getJSON():
	if request.method == 'POST':
		dab.append(request.json)
		print dab
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(dab), content_type='application/json')

@app.route("/nextWiki", methods= ['POST', 'GET'])
def nextWiki():

	if request.method == 'POST':
		re = request

		pager.append(request.json["next"])
		print pager

		return "Success"
	elif request.method == 'GET':
		return Response(json.dumps(makeWikiObjects()), content_type='application/json')

if __name__ == "__main__":
	app.run(debug = True)

