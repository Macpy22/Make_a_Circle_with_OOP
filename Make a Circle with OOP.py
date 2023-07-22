from math import pi


class Circle:
	def __init__(self, r):
		self.r = r 

	def getArea(self):
		x = pi * self.r ** 2
		return round(x)

	def getPerimeter(self):
		y = 2 * pi * self.r
		return round(y)


circy = Circle(11)
print(circy.getArea())
circy = Circle(4.44)
print(circy.getPerimeter())

