from flask import Flask, render_template, Markup
import jinja2
import wikipedia as W
app = Flask(__name__)

def loadWikiPage():
	random = W.random()
	randomPage = W.page(random)
	return Markup(randomPage.html())



@app.route("/")
def hello():
	entries = {"title": "wikiGolf", "wikiPage": loadWikiPage()}
	return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.run(debug = True)

