from person import person

class room:
	def __init__(self, xDim, yDim, personName, personType, personX, personY):
		self.window = []
		self.xDim = xDim-1
		self.yDim = yDim-1
		self.person = Person(personName, personType, personX, personY)
		for i in range(0,self.xDim,1):
			row = []
			for k in range(0,self.yDim,1):
				row += [0]
			self.window += [row]

	def update(self):
		if(xDim - person.getX < person.getX)
		window[person.getX][person.getY] = person.bodyArray[0][0]


	def display(self):
