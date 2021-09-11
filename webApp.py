#Contributors: Austin Truong and Austin Tran

import fileSearch
from flask import Flask, render_template, request


searchObject = fileSearch.QuerySearch()
app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args['query']
    searchResults = searchObject.corpusSearch(query)
    return render_template("index.html", query=query, searchResults=searchResults)