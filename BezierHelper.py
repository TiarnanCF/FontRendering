import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class linear_bezier:
	def __init__(self, x0, x1):
		self.x0 = x0
		self.x1 = x1

	def compute_point(self, t):
		return np.add(self.x0, np.matmul(np.subtract(self.x1,self.x0),t))

class quadratic_bezier:
	def __init__(self, x0, x1, x2):
		self.x0 = x0
		self.x1 = x1
		self.x2 = x2
		self.bezier_0 = linear_bezier(x0,x1)
		self.bezier_1 = linear_bezier(x1,x2)

	def compute_point(self, t):
		point_on_bezier_0 = self.bezier_0.compute_point(t)
		point_on_bezier_1 = self.bezier_1.compute_point(t)
		t_dimensions = t.shape
		t_extended = np.diag(t[0])#np.diag(np.matmul(np.transpose(t), np.ones(t_dimensions)))
		return np.add(point_on_bezier_0, np.matmul(np.subtract(point_on_bezier_1,point_on_bezier_0), t_extended))

class node:
	def __init__(self, data, next_node = None):
		self.data = data
		self.next = next_node

	def has_next(self):
		return self.next is None

	def is_on_curve(self):
		return self.data[-1]

	def get_next(self):
		return self.next

	def get_coordinates(self):
		return [self.data[0], self.data[1]]

class contour:
	def __init__(self, x_relative, y_relative, on_curve):
		
		current_x = x_relative.pop(0)
		current_y = y_relative.pop(0)
		current_on_curve = on_curve.pop(0)
		current_node = node([current_x, current_y, current_on_curve])
		for x,y, b_on_curve in self.x_relative, self.y_relative, self.on_curve:
			x_absolute = (x + current_x)
			y_absolute = (y + current_y)
			current_x = x
			current_y = y
			current_node = node([x_absolute, y_absolute, b_on_curve], current_node)

		self.first_node = current_node

		self.beziers = []
		while current_node.has_next():
			if not(current_node.is_on_curve()):
				current_node = current_node.get_next()
				continue

			next_node = current_node.get_next()

			if next_node.is_on_curve():
				self.beziers.add(linear_bezier(current_node.get_coordinates(), next_node.get_coordinates()))
				current_node = current_node.get_next()
				continue

			if not(next_node.get_next().is_on_curve()):
				raise Exception("Sorry, invalid data")

			self.beziers.add(quadratic_bezier(current_node.get_coordinates(), next_node.get_coordinates(), next_node.get_next().get_coordinates()))
			current_node = current_node.get_next()


#my_bezier = linear_bezier(np.array([[0],[0]]), np.array([[2],[1]]))

#t_values = np.array([np.linspace(0,1,10)])
#print(my_bezier.compute_point(t_values))

#plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])
#plt.show()

my_bezier = quadratic_bezier(np.array([[0],[0]]), np.array([[2],[1]]), np.array([[1],[1]]))

t_values = np.array([np.linspace(0,1,1000)])

print(my_bezier.compute_point(t_values))

plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])
plt.show()
