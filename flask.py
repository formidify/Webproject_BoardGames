#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016
    Modified by Eric Alexander, January 2017

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import datasource.py
import flask
from flask import render_template request
import json
import sys

app = flask.Flask(__name__)
newQuery = DataSource()
A_ZList = newQuery.listAZSearch()
newGamesList = newQuery.newGamesSearch()

@app.route('/', methods = ['POST', 'GET'])
def homePage():
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<searchInput>/<number>'), code = 307)
    randomList = newQuery.randomSearch()
    #check if URL is valid
    return render_template('boardGamesWebsite.html', list = randomList)

#default to 10 results per page for now
@app.route('/a_z/<number>', methods = ['POST', 'GET'])
def azPage(number):
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<searchInput>/<number>'), code = 307)
    if (10*(number -1) > len(A_ZList)) || (number <= 0):
        return render_template('404.html'), 404
    else:
        returnList = A_ZList[(i-1)*10+1, i*10+1]
        return render_template('HTML of search page.', list = returnList, total = len(A_ZList))

@app.route('/newgames/<number>', methods = ['POST', 'GET'])
def newgamesPage(number):
    if request.method == 'POST':
        return redirect(url_for('/<genre>+<minPlayers>+<searchInput>/<number>'), code = 307)
    if (10*(number -1) > len(newGamesList)) || (number <= 0):
        return render_template('404.html'), 404
    else:
        returnList = newGamesList[(i-1)*10+1, i*10+1]
        return render_template('HTML of search page.', list = returnList, total = len(newGamesList))

@app.route('/<genre>+<minPlayers>+<input>/<number>', methods = ['POST'])
def searchPage_form():
    if request.form['genre'] == '':
        genre = -1
    if request.form['minPlayers'] == '':
        minPlayers = -1
    searchInput = request.form['searchInput']
    return redirect(url_for('/<genre>+<minPlayers>+<searchInput>/<number>', 
                            genre = genre, minPlayers = minPlayers, searchInput = searchInput, number = 1),
                            code = 302)

@app.route('/<genre>+<minPlayers>+<input>/<number>')
def searchPage_create(genre, minPlayers, searchInput, number):
    resultList = newQuery.mainSearch(genre, minPlayers, searchInput);
    if resultList:
        if (10*(number -1) > len(resultList)) || (number <= 0):
            return render_template('404.html'), 404
        else:
            returnList = A_ZList[(i-1)*10+1, i*10+1]
            return render_template('HTML of search page.', list = returnList, total = len(resultList))
    return render_template('HTML of no result page')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

 
#<!DOCTYPE html>
#<html>
#<body>

#<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com" style="width:104px;height:142px;">

#</body>
#</html>