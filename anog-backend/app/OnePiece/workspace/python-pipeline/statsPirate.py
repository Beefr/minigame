

class StatsPirate(object):

	@staticmethod
	def generateStats(level, qualite, fruitpower):
		level=int(level)
		qualite=int(qualite)

		vie=100*level*(5-qualite)
		degats=20*level*(5-qualite)
		defense=10*level*(5-qualite)
		fatigue=100*(5-qualite)
		return [int(vie*(100+6*fruitpower[0])/100), int(degats*(100+6*fruitpower[1])/100), int(defense*(100+6*fruitpower[2])/100), int(fatigue*(100+6*fruitpower[3])/100)]

