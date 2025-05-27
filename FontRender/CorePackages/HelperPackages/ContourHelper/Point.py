import numpy as np

class Point:
	def __init__(self, data, next_node = None):
		self.data = data
		self.next = next_node

	def has_next(self):
		return not(self.next is None)

	def is_on_curve(self):
		return self.data[-1]

	def get_next(self):
		return self.next

	def get_coordinates(self):
		return np.array([[self.data[0]], [self.data[1]]])

	def get_x(self):
		return self.data[0]

	def get_y(self):
		return self.data[1]