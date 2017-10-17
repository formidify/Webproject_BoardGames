'''
    datasource.py
    James Yang, Vermilion Villarreal
    Modified October 14, 2017
'''
import getpass
import psycopg2

class DataSource:

	def __init__(self):
		# Get the database login info
		database = 'boardgames'
		user = 'yangj2'
		password = getpass.getpass()
		try:
			connection = psycopg2.connect(database=database, user=user, password=password)
			cursor = connection.cursor()
		except Exception as e:
			print('Connection error: ', e)
			exit()

	#use -1 to indicate no user input for that field
	#if user doesn't select any option, then we return a list of games in alphabetical order
	def mainSearch(self, genre, minPlayers, searchInput):

		if (genre == -1 and minPlayers != -1):
			query = 'SELECT * FROM boardgames WHERE minPlayers >= %d', minPlayers
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers == -1):
			query = 'SELECT * FROM boardgames'
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1

		if (genre == -1 and minPlayers == -1):
			query = 'SELECT * FROM boardgames'
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers != -1):
			query = 'SELECT * FROM boardgames WHERE minPlayers >= %d', minPlayers
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1
			
		if searchInput:
			return self.findGames(resultList, searchInput)

		else:
			return resultList

	#helper functions which take a list and an input and return a list that only contains the given input
	def findGenres(self, list, genreInput):
		#return a list if found, or else return -1
	def findGames(self, list, searchInput):


	def listAZSearch(self):
		try:
			query = 'SELECT gameDescription, gameName, thumbnailURL FROM boardgames ORDER BY gameName DESC'
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
				print(resultList[1][0])
				print(resultList[1][1])
				print(resultList[1][2])
				return resultList
			else:
				return -1
		except Exception as e:
			print('Cursor error', e)
			connection.close()
			exit()

	def newgamesSearch(self):
		try:
			query = 'SELECT gameDescription, gameName, thumbnailURL FROM boardgames \
			where yearPublished>2000 ORDER BY yearPublished DESC'
			cursor.execute(query)
			if cursor:
				resultList = cursor.fetchall()
				print(resultList[1][0])
				print(resultList[1][1])
				print(resultList[1][2])
				return resultList
			else:
				return -1
		except Exception as e:
			print('Cursor error', e)
			connection.close()
			exit()

	def randomSearch(self):
		return;

def main():
	newData = DataSource()
	newData.listAZSearch()

main()





    