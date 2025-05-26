import matplotlib.pyplot as plt
import numpy as np

from ..BezierHelper.LinearBezier import LinearBezier
from ..BezierHelper.QuadraticBezier import QuadraticBezier
from .Point import Point

class Contour:
	def __init__(self, x_relative, y_relative, on_curve, is_closed_curve = True):
		
		current_x = x_relative.pop(0)
		current_y = y_relative.pop(0)
		current_on_curve = on_curve.pop(0)
		current_node = Point([current_x, current_y, current_on_curve])

		for x,y, b_on_curve in zip(x_relative, y_relative, on_curve):
			x_absolute = (x)# + current_x)
			y_absolute = (y)# + current_y)
			current_x = x
			current_y = y
			current_node = Point([x_absolute, y_absolute, b_on_curve], current_node)
			

		self.first_node = current_node
		previous_node = None

		self.beziers = []
		while current_node.has_next():
			if not(current_node.is_on_curve()):
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			next_node = current_node.get_next()

			if next_node.is_on_curve():
				self.beziers.append(LinearBezier(current_node.get_coordinates(), next_node.get_coordinates()))
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			if not(next_node.get_next().is_on_curve()):
				raise Exception("Sorry, invalid data")

			self.beziers.append(QuadraticBezier(current_node.get_coordinates(), next_node.get_coordinates(), next_node.get_next().get_coordinates()))
			previous_node = current_node
			current_node = current_node.get_next()

		if not(is_closed_curve):
			return

		if not(current_node.is_on_curve()) and not(self.first_node.is_on_curve()):
			raise Exception("Sorry, invalid data")

		if not(current_node.is_on_curve()):
			self.beziers.append(QuadraticBezier(previous_node.get_coordinates(), current_node.get_coordinates(), self.first_node.get_coordinates()))
		
		if not(self.first_node.is_on_curve()):
			self.beziers.append(QuadraticBezier(current_node.get_coordinates(), self.first_node.get_coordinates(), self.first_node.get_next().get_coordinates()))

		if current_node.is_on_curve() and self.first_node.is_on_curve():
			self.beziers.append(LinearBezier(current_node.get_coordinates(), self.first_node.get_coordinates()))

	def plot_contour(self,t_count):
		for bezier in self.beziers:
			bezier.plot(t_count)
		plt.show()


my_contour = Contour([1,1,2,3,4,3,10,4,1],[0,-2,-7,3,2,1,3,6,6],[1,0,1,0,1,1,0,1,0])

my_contour.plot_contour(500)