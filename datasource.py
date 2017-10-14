'''
    datasource.py
    James Yang, Vermilion Villarreal
    Modified October 14, 2017
'''

class DataSource:

	def __init__():
		# Get the database login info
		database = 'boardgames'
		user = 'yangj2'
		password = getpass.getpass()
		try:
    		connection = psycopg2.connect(database=database, user=user, password=password)
    		cursor = connection.cursor()
		except Exception, e:
    		print 'Connection error: ', e
    		exit()

    #use -1 to indicate no user input for that field
    #if user doesn't select any option, then we return a list of games in alphabetical order
    def mainSearch(self, genre, minPlayers, searchInput):
    	if (genre == -1 and minPlayers != -1):
    		self.playerInputSearch(minPlayers, searchInput)
    	elif (genre != -1 and minPlayers == -1):
    		self.genreInputSearch(genre, searchInput)
    	elif (genre == -1 and minPlayers == -1):
    		self.nameSearch(searchInput)
    	else:
    		self.fullSearch(genre, minPlayers, searchInput)

    def listAZSearch(self):
    	try:
    		query = 'SELECT gameDescription, gameName, thumbnailURL FROM boardgames ORDER BY gameName DESC'
    		cursor.execute(query)
    		for row in cursor:
      	  		print row
      	except Exception, e:
      		print 'Cursor error', e
    		connection.close()
    		exit()

    def newgamesSearch(self):
    	try:
    		query = 'SELECT gameDescription, gameName, thumbnailURL FROM boardgames \
    				 where yearPublished>2000 ORDER BY yearPublished DESC'
    		cursor.execute(query)
    		for row in cursor:
    			print row
    	except Exception, e:
    		print 'Cursor error', e
    		connection.close()
    		exit()

    def randomSearch(self):





    