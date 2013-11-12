from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
app = Flask(__name__)

def loadWikiPage():
	random = W.random()
	randomPage = W.page(random)
	return randomPage.links, randomPage.title

links_title = loadWikiPage()

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
		print request.json
		return "Success"

if __name__ == "__main__":
    app.run(debug = True)

