# Web Driven Database Project
# James Yang, Vermilion Villarreal
# Last Updated October 25th, 2017

*All the files are up-to-date and ready to be turned in. Failed to push tags because local repository is forked. 

Description of the project: 
Our project consists of a web driven database for board games searches. Users can search and find boardgames and their attributes, including description and thumbnail, etc. 

Features:
1. Users can find six recommended board games on the home page every time they refresh it. 
2. Users can click on What's New at the top and get access to 99 newest board games and their thumbnails. 
3. Users can click on List A-Z at the top and get access to all the board games in our database (only 99 in this case because it will take too long to load otherwise). 
4. Users can search for boardgames after inputting the minimum players, genre of the game and name of the game (or any of them) and our system will display all the board games that match the input. 
5. Users can click on the name of any game in any search result and our system will display an individual page of that game which displays many attributes of that particular game. 

Citations:
1. Our dataset is from https://github.com/9thcirclegames/bgg-analysis and then downloaded from the R package "bgg-analysis". 
2. The background picture on all the webpages is downloaded from http://www.analoggames.com/wp-content/uploads/2016/04/pyramid_arcade_andy_looney_labs_fluxx_board_card_game_analoggames_analog_games_02.jpg. 
3. The thumbnails/pictures of all the board games from geekdo-images, whose URLs are part of the dataset. 
4. The structure of our HTML templates is borrowed from https://www.quackit.com/html/templates/. 

What we wish we had implemented:
We wanted to implement pagination for all the search pages so we can display only 10 results per page instead of display everything. However, the interface we need to use is too complicated and time-consuming for this particular project, so we decided not to in the end. 

This repo contains starter code for the database-driven web project. It consists of the following files:

createtable.sql: A Python script used to create a database and set up the table(s), including table columns and types.

BoardGames.csv: A comma-space delimited text file containing board game names and their respective attributes, including description, publishers, published years, etc. 

datasource.py: A Python script that executes SQL queries using the psycopg2 library.

gamesFlask.py: A Python script that glues HTML and datasource.py in order to perform database queries from webpages. 

templates folder: HTML templates (index.html for home page, results.html for search results page, specific.html for individual board game page, and notFound.html in case no games are found for the user input) 

static folder: Images, CSS files, etc. used for our HTML templates
