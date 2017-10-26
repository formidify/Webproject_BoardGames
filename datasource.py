'''
    datasource.py
    James Yang, Vermilion Villarreal
    Modified October 25, 2017
'''

import getpass
import psycopg2
import random

class DataSource:

	def __init__(self):
		# Get the database login info
		self.database = 'yangj2'
		self.user = 'yangj2'
		self.password = getpass.getpass()
		#set up database connection and cursor
		try:
			connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			cursor = connection.cursor()
			self.connection = connection
			self.cursor = cursor
		except Exception as e:
			print('Curcor error', e)
			try:
				self.cursor.close()
				self.cursor = self.conection.cursor()
			except:
				self.connection.close()
				self.connection = connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			self.cursor = self.connection.cursor()

	'''
	Search for results given the genre, mainPlayers and search input and divide into four cases.
	Cursor through each case and pass into findGames() to find the final list.
	Used to provide a list of search results for the search button on our webpage. 
	'''
	def mainSearch(self, genre, minPlayers, searchInput):
		if (genre == -1 and minPlayers != -1):
			self.cursor.execute('SELECT gameName, thumbnailURL, gameCategory, gameMechanic, gameID \
			FROM boardgames WHERE minPlayer >= %s', (minPlayers,))
			if self.cursor:
				resultList = self.cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers == -1):
			self.cursor.execute('SELECT gameName, thumbnailURL, gameCategory, gameMechanic, gameID \
			FROM boardgames')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1

		if (genre == -1 and minPlayers == -1):
			self.cursor.execute('SELECT gameName, thumbnailURL, gameCategory, gameMechanic, gameID \
			FROM boardgames')
			if self.cursor:
				resultList = self.cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers != -1):
			self.cursor.execute('SELECT gameName, thumbnailURL, gameCategory, gameMechanic, gameID \
			FROM boardgames WHERE minPlayer >= %s', (minPlayers,))
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1

		if resultList != -1:
			if searchInput:
				return self.findGames(resultList, searchInput)
			resultDict = self.convertDictFromAll(resultList)
			return resultDict
		return -1

	#helper function to convert the resulting lists from mainSearch and findGames to a dictionary with appropriate keys
	def convertDictFromAll(self, list):
		resultDict = []
		for i in range(len(list)):
			resultDict.append({"name": list[i][0], "thumbURL": list[i][1], "ID": list[i][4]})
		return resultDict

	'''
	Helper function to generate a list where the genre of the game matches the input
	'''
	def findGenres(self, list, genreInput):
		j = 0
		bothEnd = []
		frontEnd = []
		backEnd = []
		neitherEnd = []
		for i in range(len(list)):
			if (" " + genreInput + " ") in list[i][2] or (" " + genreInput + " ") in list[i][3]:
				bothEnd.append(list[i])
				j = j + 1
			elif (" " + genreInput) in list[i][2] or (" " + genreInput) in list[i][3]:
				frontEnd.append(list[i])
				j = j + 1
			elif (genreInput + " ") in list[i][2] or (genreInput + " ") in list[i][3]:
				backEnd.append(list[i])
				j = j + 1
			elif genreInput in list[i][2] or genreInput in list[i][3]:
				neitherEnd.append(list[i])
				j = j + 1
		resultList = bothEnd + frontEnd + backEnd + neitherEnd
		if resultList:
			return resultList
		return -1

	'''
	Helper function to generate a list where the name of the game matches the search input
	'''
	def findGames(self, list, searchInput):
		j = 0
		bothEnd = []
		frontEnd = []
		backEnd = []
		neitherEnd = []
		for i in range(len(list)):
			if (" " + searchInput + " ") in list[i][0]:
				bothEnd.append(list[i])
				j = j + 1
			elif (" " + searchInput) in list[i][0]:
				frontEnd.append(list[i])
			elif (searchInput + " ") in list[i][0]:
				backEnd.append(list[i])
			elif searchInput in list[i][0]:
				neitherEnd.append(list[i])
			j = j + 1
		resultList = bothEnd + frontEnd + backEnd + neitherEnd
		if resultList:
			resultDict = self.convertDictFromAll(resultList)
			return resultDict
		return -1

	'''
	Gives a list of all games sorted alphabetically.
	Used to generate "List A-Z" section on our webpage
	'''
	def listAZSearch(self):
		try:
			self.cursor.execute('SELECT gameName, thumbnailURL, gameID \
			FROM boardgames ORDER BY gameName ASC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultDict = self.convertDictFromSome(resultList)
				return resultDict[0:98] #only display a subset so it won't take too long to load
			else:
				return -1
		except Exception as e:
			print('Curcor error', e)
			try:
				self.cursor.close()
				self.cursor = self.conection.cursor()
			except:
				self.connection.close()
				self.connection = connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			self.cursor = self.connection.cursor()

	'''
	Returns a list of all games sorted by descending years. 
	Used to generate "What's new" section on our webpage
	'''
	def newGamesSearch(self):
		try:
			self.cursor.execute('SELECT gameName, thumbnailURL, gameID FROM boardgames \
			where yearPublished>2000 ORDER BY yearPublished DESC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultDict = self.convertDictFromSome(resultList)
				return resultDict[0:98]
			else:
				return -1
		except Exception as e:
			print('Curcor error', e)
			try:
				self.cursor.close()
				self.cursor = self.conection.cursor()
			except:
				self.connection.close()
				self.connection = connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			self.cursor = self.connection.cursor()

	'''
	Returns a list of 7 games that are selected randomly.
	Used to generate "Recommended" section on our webpage
	'''
	def randomSearch(self):
		resultList = []
		try:
			for i in range(6):
				r = random.randint(1, 90400)
				self.cursor.execute('SELECT gameName, thumbnailURL, gameID FROM boardgames \
				where gameID =%s', (r,))
				resultList.append((self.cursor.fetchall())[0])
			resultDict = self.convertDictFromSome(resultList)
			return resultDict
		except Exception as e:
			print('Curcor error', e)
			try:
				self.cursor.close()
				self.cursor = self.conection.cursor()
			except:
				self.connection.close()
				self.connection = connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			self.cursor = self.connection.cursor()

	'''
	Returns a tuple of attributes given the game name.
	Used to provide all attributes of a game given its name as the input
	'''
	def returnAllAttributes(self, gameID):
		try:
			self.cursor.execute('SELECT * FROM boardgames WHERE gameID=%s', (gameID,))
			resultList = self.cursor.fetchall()
			if not resultList:
				return -1
			#converts the list to a dictionary for all the attributes
			entry = resultList[0]
			resultDict = {"desc": entry[0], "URL": entry[1], "maxPlayer": entry[2], "maxTime":entry[3] 
						, "minAge": entry[4], "minPlayer": entry[5], "minTime": entry[6], "name": entry[7]
						, "thumbURL": entry[8], "year": entry[9], "artist": entry[10]
						, "category": entry[11], "designer": entry[12], "expansion": entry[13]
						, "family": entry[14], "mechanic": entry[15], "publisher": entry[16], "ID": entry[17]}
			return resultDict
		except Exception as e:
			print('Curcor error', e)
			try:
				self.cursor.close()
				self.cursor = self.conection.cursor()
			except:
				self.connection.close()
				self.connection = connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,host = "localhost")
			self.cursor = self.connection.cursor()


	#convert the resulting lists from randomSearch, listAZSearch and newGamesSearch to a dictionary with appropriate keys
	def convertDictFromSome(self, list):
		dict = []
		for i in range(len(list)):
			dict.append({"name": list[i][0], "thumbURL": list[i][1], "ID": list[i][2]})
		return dict

