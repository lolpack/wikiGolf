from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
import string

app = Flask(__name__)

class WikiPage():


	def loadRandWikiPage(self):
		

		random = W.random()
		self.randomPage = W.page(random)
		print type(self.randomPage.title)
		return self.randomPage.links, self.randomPage.title

	def loadGivenWikiPage(self, page):
		self.Page = W.page(page)
		print self.Page.title
		return self.Page.links, self.Page.title

WP = WikiPage()

pager = []

links, title = WP.loadRandWikiPage()



coursePath = []


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
		print request.method
		pager.append(request.json["next"])
		print pager

		return "Success"
	elif request.method == 'GET':
		#print pager
		#withUnderscores = string.replace(pager[0]  , " " , "_" )
		#loaded =  WP.loadGivenWikiPage( withUnderscores )
		#print str(loaded[0]) + "somthings"
		return Response(json.dumps([{"id":2,  "next": "Link2"},{"id":1,  "next": "Link2"}]), content_type='application/json')

if __name__ == "__main__":
	app.run(debug = True)

