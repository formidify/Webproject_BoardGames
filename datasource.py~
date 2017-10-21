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
		database = 'yangj2'
		user = 'yangj2'
		password = getpass.getpass()
		#set up database connection and cursor
		try:
			connection = psycopg2.connect(database=database, user=user, password=password)
			cursor = connection.cursor()
			self.connection = connection
			self.cursor = cursor
		except Exception as e:
			print('Connection error: ', e)
			exit()

	'''
	Search for results given the genre, mainPlayers and search input and divide into four cases.
	Cursor through each case and pass into findGames() to find the final list.
	Used to provide a list of search results for the search button on our webpage. 
	'''
	def mainSearch(self, genre, minPlayers, searchInput):

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
		resultList = []
		for i in range(len(list)):
			if searchInput in list[i][7]:
				resultList.append(list[i])
				j = j + 1
		if resultList:
			return resultList
		return -1

	'''
	Gives a list of all games sorted alphabetically.
	Used to generate "List A-Z" section on our webpage
	'''
	def listAZSearch(self):
		try:
			self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL \
			FROM boardgames ORDER BY gameName DESC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				return resultList
			else:
				return -1
		except Exception as e:
			print('Cursor error', e)
			self.connection.close()
			exit()

	'''
	Returns a list of all games sorted by descending years. 
	Used to generate "What's new" section on our webpage
	'''
	def newGamesSearch(self):
		try:
			self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL FROM boardgames \
			where yearPublished>2000 ORDER BY yearPublished DESC')
			if self.cursor:
				resultList = self.cursor.fetchall()
				return resultList
			else:
				return -1
		except Exception as e:
			print('Cursor error', e)
			self.connection.close()
			exit()

	'''
	Returns a list of 7 games that are selected randomly.
	Used to generate "Recommended" section on our webpage
	'''
	def randomSearch(self):
		resultList = []
		try:
			for i in range(7):
				r = random.randint(1, 90400)
				self.cursor.execute('SELECT gameDescription, gameName, thumbnailURL FROM boardgames \
				LIMIT 1 OFFSET %s', (r-1,))
				entry = self.cursor.fetchall()
				resultList.append(entry)
			return resultList
		except Exception as e:
			print('Curcor error', e)
			self.connection.close()
			exit()

	'''
	Returns a tuple of attributes given the game name.
	Used to provide all attributes of a game given its name as the input
	'''
	def returnAllAttributes(self, gameName):
		try:
			resultList = []
			self.cursor.execute('SELECT * FROM boardgames WHERE gameName=%s', (gameName,))
			resultList.append(self.cursor.fetchall())
			if len(resultList[0][0]) > 1:
				return -1
			if resultList[0][0][9] == 0:
				resultList[0][0][9] = "NA"
			return resultList
		except Exception as e:
			print('Curcor error', e)
			self.connection.close()
			exit()
		#change all attributes to appropriate values 

#Tester 
def main():
	newQuery = DataSource()
	#Test mainSearch()
	list1 = newQuery.mainSearch(-1, -1, "love")
	list2 = newQuery.mainSearch(-1, -1, "hate")
	list3 = newQuery.mainSearch(-1, 0, "")
	list4 = newQuery.mainSearch("good", 3, "hfjrwhvijefhvweehgggggivivfbi")
	for i in range(3):
		print(list1[i][7] + " ")
		print(list2[i][7] + " ")
		print(list3[i][7] + " ")
	print()
	print(list4) #should return -1

	print()
	print()

	#Test listAZSearch
	list5 = newQuery.listAZSearch()
	for i in range(20):
		print(list5[i][1] + " ")

	print()
	print()

	#Test newGamesSearch
	list6 = newQuery.newGamesSearch()
	for i in range(20):
		print(list6[i][1] + " ")
	print(len(list6))
	print(len(list6[0]))
	print()
	print()

	#Test randomSearch
	list7 = newQuery.randomSearch()
	print(len(list7))
	print(len(list7[0]))
	for i in range(7):
		print(list7[i][0][1] + " ")

	print()
	print()

	#Test returnAllAttributes
	for i in range(7):
		for j in range(16):
			if newQuery.returnAllAttributes(list7[i][0][1]) != -1:
				print((newQuery.returnAllAttributes(list7[i][0][1]))[0][0][j] + " ")
		print()

main()





    
