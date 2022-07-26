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


		#_________________________GET___________________________

		@staticmethod
		def getID(username):
			[conn, cur]=InteractBDD.beginQuery()
			request = "SELECT id FROM joueur WHERE username='"+str(username)+"';"
			description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
			
			for elem in description:
				id = elem[0]
				InteractBDD.endQuery(conn, cur)
				return id
			InteractBDD.endQuery(conn, cur)
			return None

		@staticmethod
		def getUsername(id):
			[conn, cur]=InteractBDD.beginQuery()
			request = "SELECT username FROM joueur WHERE id='"+str(id)+"';"
			description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
			
			for elem in description:
				username = elem[0]
				InteractBDD.endQuery(conn, cur)
				return username
			InteractBDD.endQuery(conn, cur)
			return "None"





		#____________________________________________________________
		
		@staticmethod
		def connectAndExecuteRequest(request, needCommit, conn, cur):
			#conn = mariadb.connect(**InteractBDD.config)
			#cur = conn.cursor()
			if needCommit:
				try:
					cur.execute(request)
					conn.commit()
				except:
					conn.rollback()
			else:
				cur.execute(request)

			description=cur
			#cur.close()
			#conn.close()
			return description

		@staticmethod
		def beginQuery():
			conn = mariadb.connect(**InteractBDD.config)
			cur = conn.cursor()
			return [conn, cur]

		@staticmethod
		def endQuery(conn, cur):
			cur.close()
			conn.close()
			











































