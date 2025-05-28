import matplotlib.pyplot as plt
import numpy as np

from ..BezierHelper.LinearBezier import LinearBezier
from ..BezierHelper.QuadraticBezier import QuadraticBezier
from ..BezierHelper.Point import Point
from ..BezierHelper.BezierBuilder import BezierBuilder

class Contour:
	def __init__(self, x: list[float], y: list[float], is_on_curve: list[bool], is_closed_curve: bool = True, is_relative_points: bool = True):
		
		current_x = x.pop(0)
		current_y = y.pop(0)
		current_on_curve = is_on_curve.pop(0)
		self.first_node = Point(current_x, current_y, current_on_curve)
		self.is_closed_curve = is_closed_curve
		self.is_relative_points = is_relative_points
		self.is_bezier_curves_generated: bool = False
		self.is_nodes_synced_with_bezier_curves: bool = True
		
		self.add_points(x,y,is_on_curve)
		self.generate_bezier_curves()

	def add_point(self, x: float, y:float, is_on_curve: bool) -> None:
		current_x: float = self.first_node.get_x()
		current_y: float = self.first_node.get_x()
		x_absolute: float = (x + self.is_relative_points * current_x)
		y_absolute: float = (y + self.is_relative_points * current_y)

		self.first_node: Point = Point(x_absolute, y_absolute, is_on_curve, self.first_node)
		self.is_bezier_curves_generated: bool = False

	def add_points(self, x_list: list[float], y_list:list[float], is_on_curve_list: list[bool]) -> None:
		for x,y, is_on_curve in zip(x_list, y_list, is_on_curve_list):
			self.add_point(x,y,is_on_curve)

	def generate_bezier_curves(self) -> None:
		current_node = self.first_node
		previous_node = None

		self.beziers = []
		while current_node.has_next():
			if not(current_node.check_is_on_curve()):
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			next_node = current_node.get_next()

			if next_node.check_is_on_curve():
				self.beziers.append(LinearBezier(current_node, next_node))
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			if not(next_node.get_next().check_is_on_curve()):
				raise Exception("Sorry, invalid data")

			self.beziers.append(QuadraticBezier(current_node, next_node, next_node.get_next()))
			previous_node = current_node
			current_node = current_node.get_next()

		if not(self.is_closed_curve):
			self.is_bezier_curves_generated = True
			return

		if not(current_node.check_is_on_curve()) and not(self.first_node.check_is_on_curve()):
			raise Exception("Sorry, invalid data")

		if not(current_node.check_is_on_curve()):
			self.beziers.append(QuadraticBezier(previous_node, current_node, self.first_node))
			self.is_bezier_curves_generated = True
			return
		
		if not(self.first_node.check_is_on_curve()):
			self.beziers.append(QuadraticBezier(current_node, self.first_node, self.first_node.get_next()))
			self.is_bezier_curves_generated = True
			return

		self.beziers.append(LinearBezier(current_node, self.first_node))
		self.is_bezier_curves_generated = True

	def modify_bezier(self, bezier_index: int, bezier_point_x0, bezier_point_x2, bezier_point_x1 = None) -> None:
		self.beziers[bezier_index].update_x0(bezier_point_x0.get_x(), bezier_point_x0.get_y())
		self.beziers[bezier_index].update_x2(bezier_point_x2.get_x(), bezier_point_x2.get_y())

		if (bezier_point_x1 is None and isinstance(self.beziers[bezier_index], QuadraticBezier)):
			self.beziers[bezier_index] = BezierBuilder.reduce_to_linear_bezier(self.beziers[bezier_index])
			return

		if (bezier_point_x1 is not None and isinstance(self.beziers[bezier_index], LinearBezier)):
			self.beziers[bezier_index] = BezierBuilder.enhance_to_quadratic_bezier(self.beziers[bezier_index], bezier_point_x1)
			return

		if (bezier_point_x1 is not None):
			self.beziers[bezier_index].update_x1(bezier_point_x1.get_x(), bezier_point_x1.get_y())

	def update_nodes_based_on_bezier_curves(self) -> None:
		pass

	def plot_contour(self,t_count: int) -> None:
		for bezier in self.beziers:
			bezier.plot(t_count)
		plt.show()


if __name__ == "__main__":
	my_contour = Contour([1,1,2,3,4,3,10,4,1],[0,-2,-7,3,2,1,3,6,6],[1,0,1,0,1,1,0,1,0])
	my_contour.plot_contour(500)
	
	my_contour.modify_bezier(3, Point(5,3, True), Point(8,1, True))
	my_contour.plot_contour(500)
	my_contour.modify_bezier(3, Point(5,3, True), Point(8,1, True), Point(4,2, True))
	my_contour.plot_contour(500)