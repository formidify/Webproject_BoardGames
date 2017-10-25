'''
    datasource.py
    James Yang, Vermilion Villarreal
    Modified October 17, 2017
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
		minPlayers = int(minPlayers)
		if (genre == -1 and minPlayers != -1):
			self.cursor.execute('SELECT * FROM boardgames WHERE minPlayer >= %s', (minPlayers,))
			if self.cursor:
				resultList = self.cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers == -1):
			self.cursor.execute('SELECT * FROM boardgames')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1

		if (genre == -1 and minPlayers == -1):
			self.cursor.execute('SELECT * FROM boardgames')
			if self.cursor:
				resultList = self.cursor.fetchall()
			else:
				return -1

		if (genre != -1 and minPlayers != -1):
			self.cursor.execute('SELECT * FROM boardgames WHERE minPlayer >= %s', (minPlayers,))
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultList = self.findGenres(resultList, genre)
			else:
				return -1

		if resultList != -1:
			if searchInput:
				return self.findGames(resultList, searchInput)
			return resultList
		return -1

	'''
	Helper function to generate a list where the genre of the game matches the input
	'''
	def findGenres(self, list, genreInput):
		j = 0
		resultList = []
		for i in range(len(list)):
			if genreInput in list[i][11] or genreInput in list[i][15]:
				resultList.append(list[i])
				j = j + 1
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
			if (" " + searchInput + " ") in list[i][7]:
				bothEnd.append(list[i])
				j = j + 1
			elif (" " + searchInput) in list[i][7]:
				frontEnd.append(list[i])
			elif (searchInput + " ") in list[i][7]:
				backEnd.append(list[i])
			elif searchInput in list[i][7]:
				neitherEnd.append(list[i])
			j = j + 1
		resultList = bothEnd + frontEnd + backEnd + neitherEnd
		if resultList:
			return resultList
		return -1

	'''
	Gives a list of all games sorted alphabetically.
	Used to generate "List A-Z" section on our webpage
	'''
	def listAZSearch(self):
		try:
			self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL, gameID \
			FROM boardgames ORDER BY gameName ASC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultDict = self.convertDict(resultList)
				return resultDict
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
			self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL, gameID FROM boardgames \
			where yearPublished>2000 ORDER BY yearPublished DESC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				resultDict = self.convertDict(resultList)
				return resultDict
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
				self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL, gameID FROM boardgames \
				where gameID =%s', (r,))
				resultList.append((self.cursor.fetchall())[0])
			resultDict = self.convertDict(resultList)
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
		#change all attributes to appropriate values 

	def convertDict(self, list):
		dict = []
		for i in range(len(list)):
			dict.append({"desc": list[i][0], "name": list[i][1], "thumbURL": list[i][2], "ID": list[i][3]})
		return dict

# def main():
# 	newQuery = DataSource()
# # 	print("Results for new games search. \n")

# 	returnDict = newQuery.returnAllAttributes(23)
# 	print(returnDict)

# 	a = newQuery.randomSearch()
# 	print(a)

# 	b = newQuery.newGamesSearch()
# 	print(b)
	# #Test mainSearch()
	# list1 = newQuery.mainSearch(-1, -1, "war")
	# list2 = newQuery.mainSearch(-1, 4, "war")
	# list3 = newQuery.mainSearch(-1, 0, "")
	# list4 = newQuery.mainSearch("good", 3, "hfjrwhvijefhvweehgggggivivfbi")

	# print()
	# print("Results for main search list1: \n")
	# for i in range(3):
	# 	print(list1[i][7] + " ")


	# print()
	# print("Results for main search list2: \n")
	# for i in range(3):
	# 	print(list2[i][7] + " ")

	# print()
	# print("Results for main search list3: \n")
	# for i in range(3):
	# 	print(list3[i][7] + " ")

	# print()
	# print("Results for main search list4: \n")
	# print(list4) #should return -1

	# print()
	# print()

	# #Test listAZSearch
	# print("Results for games A-Z search. \n")
	# list5 = newQuery.listAZSearch()
	# for i in range(20):
	# 	print(list5[i][1])
	# 	print()

	# print()
	# print()

	# #Test newGamesSearch
	# print("Results for new games search. \n")
	# list6 = newQuery.newGamesSearch()
	# for i in range(20):
	# 	print(list6[i][1])
	# 	print()

	# print()
	# print()

	# #Test randomSearch
	# print("Results for random games search. \n")
	# list7 = newQuery.randomSearch()
	# for i in range(7):
	# 	print(list7[i][1])
	# 	print()

	# print()
	# print()

	# #Test returnAllAttributes
	# print("Results for a particular game. \n")
	# for i in range(7):
	# 	gameAttr = newQuery.returnAllAttributes(list7[i][3])
	# 	print("Attributes for game", (i + 1))
	# 	for j in range(17):
	# 		print(gameAttr[j])
	# 		print()
	# 	print()
#main()





    
