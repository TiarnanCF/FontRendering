import numpy as np

class Node:
	def __init__(self, next_node = None):
		self.next = next_node

	def has_next(self):
		return not(self.next is None)

	def get_next(self):
		return self.next

	def update_next(self, new_next_node = None):
		self.next = new_next_node

class Point(Node):
	tolerance = 0.000000001

	def __init__(self, x, y, is_on_curve, next_node = None):
		self.x = x
		self.y = y
		self.is_on_curve = is_on_curve
		super().__init__(next_node)

	def get_coordinates(self):
		return np.array([[self.x], [self.y]])

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def check_is_on_curve(self):
		return self.is_on_curve

	def update_x(self, x):
		self.x = x

	def update_y(self, y):
		self.y = y

	def update_is_on_curve(self, is_on_curve):
		self.is_on_curve = is_on_curve

	def __sub__(self, other_point):
		return Point(self.x - other_point.x, self.y - other_point.y, False)

	def __eq__(self, other_point):
		return abs(self.x - other_point.x) + abs(self.y - other_point.y) < Point.tolerance