from flask import Flask, render_template, Markup, request, Response
import jinja2
import wikipedia as W
import json
app = Flask(__name__)

def loadWikiPage():
	random = W.random()
	randomPage = W.page(random)
	return randomPage.links, randomPage.title

content_title = loadWikiPage()

dab = [{"name": "First", "facebookPointer": None}]
class db():
	def __init__(self):
		self.DB = ""
db = db()

@app.route("/")
def main():
	entries = {"title": "wikiGolf", "wikiPage": content_title[0], "wikiTitle": content_title[1], "links" : content_title[0] }
	return render_template('index.html', entries=entries)


@app.route("/users", methods = ['POST', 'GET'])
def getJSON():
	if request.method == 'POST':
		dab.append(request.json)
		print dab
		return "Success!"
	elif request.method == 'GET':
		return Response(json.dumps(dab), content_type='application/json')

if __name__ == "__main__":
    app.run(debug = True)

