import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

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
		
		self.add_points(x,y,is_on_curve)
		self.beziers = BezierBuilder.construct_beziers_from_points(self.first_node, self.is_closed_curve)

	def add_point(self, x: float, y:float, is_on_curve: bool) -> None:
		current_x: float = self.first_node.get_x()
		current_y: float = self.first_node.get_x()
		x_absolute: float = (x + self.is_relative_points * current_x)
		y_absolute: float = (y + self.is_relative_points * current_y)

		self.first_node: Point = Point(x_absolute, y_absolute, is_on_curve, self.first_node)

	def add_points(self, x_list: list[float], y_list:list[float], is_on_curve_list: list[bool]) -> None:
		for x,y, is_on_curve in zip(x_list, y_list, is_on_curve_list):
			self.add_point(x,y,is_on_curve)

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

	def plot_contour(self,t_count: int, show_plot: bool = True) -> None:
		for bezier in self.beziers:
			bezier.plot(t_count)

		if not(show_plot):
			return

		plt.show()

class Glyph:
	def __init__(self):
		self.components: list[Glyph|Contour] = []

	def add_component(self, component) -> None:
		self.components.append(component)

	def add_components(self, new_components: list) -> None:
		for component in new_components:
			self.add_component(component)

	def plot_glyph(self,t_count: int, show_plot: bool = True) -> None:
		for component in self.components:
			component.plot(t_count, False)

		if not(show_plot):
			return
		
		plt.show()

class Font:
	def __init__(self, font_name: str = ""):
		self.glyphs: dict[str, Glyph] = {}
		self.font_name = font_name

	def add_glyph(self, glyph: Glyph, character: str) -> None:
		if character in self.glyphs:
			raise KeyError("Character already assigned")

			self.glyphs[character] = glyph

	def add_glyphs(self, glyphs: dict[str, Glyph]) -> None:
		for character, glyph in glyphs:
			self.add_glyph(glyph, character)

	def load_font_file(self, file_path: str) -> None:
		if not(os.path.isfile(file_path)):
			raise OSError("Not a valid file")

		if not(Path(file_path).suffix.lower() == '.ttf'):
			raise OSError("Invalid File Type")

		font_file = open(file_path)
		pass

	def save_font_to_file(self, file_path: str) -> None:
		pass

if __name__ == "__main__":

	font = Font()
	font.load_font_file("[[Font-File]]")

	my_contour = Contour([1,1,2,3,4,3,10,4,1],[0,-2,-7,3,2,1,3,6,6],[1,0,1,0,1,1,0,1,0])
	my_contour.plot_contour(500)
	
	my_contour.modify_bezier(3, Point(5,3, True), Point(8,1, True))
	my_contour.plot_contour(500)
	my_contour.modify_bezier(3, Point(5,3, True), Point(8,1, True), Point(4,2, True))
	my_contour.plot_contour(500)