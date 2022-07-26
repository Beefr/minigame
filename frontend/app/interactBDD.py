imported=False
try:
	import mariadb
	imported=True
except:
	pass


class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class InteractBDD(Static):

	config = {
	    'host': 'mariadb-anog-service',
	    'port': 3306,
	    'user': 'root',
	    'password': 'pwd',
	    'database': 'data'
	}

	if imported:

		#___________________________CREDENTIALS_______________________

		@staticmethod
		def existInDB(username):
			[conn, cur]=InteractBDD.beginQuery()
			request = "SELECT username FROM joueur WHERE username='"+username+"';"
			description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
			
			for elem in description:
				if str(elem[0])==username:
					InteractBDD.endQuery(conn, cur)
					return True
			InteractBDD.endQuery(conn, cur)
			return False


		@staticmethod
		def createUser(username, password):
			[conn, cur]=InteractBDD.beginQuery()
			request = "INSERT INTO `joueur` (`username`, `password`, `currentstep`) VALUES('"+username+"','"+password+"', 1);"
			InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
			InteractBDD.endQuery(conn, cur)
			return None


		@staticmethod
		def checkPassword(username, password):
			[conn, cur]=InteractBDD.beginQuery()
			request = "SELECT password FROM joueur WHERE username='"+username+"';"
			description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)

			for elem in description:
				if str(elem[0])==password:
					InteractBDD.endQuery(conn, cur)
					return True
			InteractBDD.endQuery(conn, cur)
			return False




















































