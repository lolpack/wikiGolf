from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
from string import replace

app = Flask(__name__)

def loadRandWikiPage():
	
	try:
		random = W.random()
		randomPage = W.page(random)
		return randomPage.links, randomPage.title
	except:
		loadRandWikiPage()

def loadGivenWikiPage(page):
	Page = W.page(page)
	return Page.links, Page.title

links_title = loadRandWikiPage()

coursePath = []

dab = [{"id":1,  "name": "First", "facebookPointer": None},
		{"id": 2, "name": "John"},
		{"id": 3, "name": links_title[0]}]

@app.route("/")
def main():
	entries = {"title": "wikiGolf", "wikiPage": links_title[0], "wikiTitle": links_title[1], "links" : links_title[0] }
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
		withUnderscores = replace( request.json["Page"] , " " , "_" )
		print loadGivenWikiPage( withUnderscores )
		return "Success"

if __name__ == "__main__":
    app.run(debug = True)

