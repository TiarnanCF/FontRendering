import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from .LinearBezier import LinearBezier
from .QuadraticBezier import QuadraticBezier
from .Point import Point

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class BezierBuilder:
	def __init__(self, x0, x1, x2):
		self.bezier_0 = LinearBezier(x0,x1)
		self.bezier_1 = LinearBezier(x1,x2)

	def reduce_to_linear_bezier(quadratic_bezier: QuadraticBezier) -> LinearBezier:
		quadratic_bezier.bezier_0.x0.update_next(quadratic_bezier.bezier_1.x2)
		return LinearBezier(quadratic_bezier.bezier_0.x0, quadratic_bezier.bezier_1.x2)

	def enhance_to_quadratic_bezier(linear_bezier: LinearBezier, x1: Point) -> QuadraticBezier:
		new_x1_point = Point(x1.get_x(), x1.get_y(), False, linear_bezier.x2)
		linear_bezier.x0.update_next(new_x1_point)
		return QuadraticBezier(linear_bezier.x0, new_x1_point, linear_bezier.x2)
