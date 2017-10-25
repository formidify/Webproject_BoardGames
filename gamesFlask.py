#!/usr/bin/env python3
'''
    James Yang, Vermillion Villarreal
    Last updated: October 23rd 
'''
from datasource import DataSource
import flask
from flask import Flask, render_template, request
import json
import sys

app = Flask(__name__, template_folder='templates')
newQuery = DataSource()
A_ZList = newQuery.listAZSearch()
newGamesList = newQuery.newGamesSearch()

@app.route('/', methods = ['POST', 'GET'])
def homePage():
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<search>/'), code = 307)
    randomList = newQuery.randomSearch()
    #check if URL is valid
    return render_template('.html', list = randomList)

#default to 10 results per page for now
@app.route('/a_z/', methods = ['POST', 'GET'])
def azPage():
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<search>/'), code = 307)
    return render_template('results.html', list = A_ZList, total = len(A_ZList))

@app.route('/newgames/', methods = ['POST', 'GET'])
def newgamesPage():
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<search>/'), code = 307)
    return render_template('results.html', list = newGamesList, total = len(newGamesList))

@app.route('/<genre>+<minPlayers>+<search>/', methods = ['POST'])
def searchPage_form(genre, minPlayers, search):
    genre = request.form.get['genre']
    minPlayers = request.form.get['minPlayers']
    search = request.form.get['search']
    if genre == 'NA':
        genre = -1
    if minPlayers == 'NA':
        minPlayers = -1
    if minPlayers == 'NA':
        minPlayers = ''
    return redirect(url_for('/<genre>+<minPlayers>+<search>/', 
                            genre = genre, minPlayers = minPlayers, search = search),
                            code = 302)

@app.route('/<genre>+<minPlayers>+<search>/')
def searchPage_create(genre, minPlayers, search):
    resultList = newQuery.mainSearch(genre, minPlayers, search);
    if resultList:
        return render_template('results.html', list = resultList, total = len(resultList))
    return render_template('HTML of no result page')

@app.route('/<gameID>/')
def searchByID(gameID):
    resultList = newQuery.returnAllAttributes(gameID)
    return render_template('specific.html', list = resultList)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
