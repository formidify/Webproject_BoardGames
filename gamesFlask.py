#!/usr/bin/env python3
'''
    James Yang, Vermillion Villarreal
    Last updated: October 25th
'''
from datasource import DataSource
import flask
from flask import Flask, render_template, request, redirect, url_for
import json
import sys

#global variables
app = Flask(__name__, template_folder='templates')
newQuery = DataSource()
A_ZList = newQuery.listAZSearch()
newGamesList = newQuery.newGamesSearch()

#generates random games and displays on home page
@app.route('/', methods = ['POST', 'GET'])
def homePage():
    randomList = newQuery.randomSearch()
    #check if URL is valid
    return render_template('index.html', list = randomList)

'''
displays the first 99 games of all the games from A to Z 
because displaying everything at once takes too long to load
'''
@app.route('/a_z/', methods = ['POST', 'GET'])
def azPage():
    return render_template('results.html', list = A_ZList, total = len(A_ZList))

#displays 99 new games 
@app.route('/newgames/', methods = ['POST', 'GET'])
def newgamesPage():
    return render_template('results.html', list = newGamesList, total = len(newGamesList))

#gathers input from html form and inputs for search in datasource.py
@app.route('/search/', methods = ['POST', 'GET'])
def searchPage_form():
    if request.method == 'POST':
        genre = request.form.get('genre')
        minPlayers = request.form.get('minPlayers')
        search = request.form.get('search')
        if genre == '':
            genre = -1
        resultList = newQuery.mainSearch(genre, minPlayers, search)             
        if resultList != -1 or len(resultList) == 0:
            return render_template('results.html', list = resultList, total = len(resultList))
        return render_template('notFound.html')

#gets to the individual page of each game with input game ID
@app.route('/<gameID>/', methods = ['POST', 'GET'])
def searchByID(gameID):
    if gameID == 'favicon.ico' or gameID == 'NA':
        randomList = newQuery.randomSearch()
        return render_template('index.html', list = randomList)
    resultList = newQuery.returnAllAttributes(gameID)
    return render_template('specific.html', list = resultList)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
