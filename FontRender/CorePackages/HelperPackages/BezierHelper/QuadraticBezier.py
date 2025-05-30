import matplotlib.pyplot as plt
import numpy as np
from .LinearBezier import LinearBezier
from .Point import Point

class QuadraticBezier:
	def __init__(self, x0: Point, x1: Point, x2: Point):
		self.bezier_0 = LinearBezier(x0,x1)
		self.bezier_1 = LinearBezier(x1,x2)

	def compute_point(self, t):
		if type(t) in (float, int):
			t = np.array([[t]], float)
		elif type(t) is list:
			t = np.array([t], float)

		if np.amax(t) > 1 or np.amin(t) < 0:
			raise IndexError("t must be in the range [0,1]")

		point_on_bezier_0 = self.bezier_0.compute_point(t)
		point_on_bezier_1 = self.bezier_1.compute_point(t)
		t_dimensions = t.shape
		t_extended = np.diag(t[0])#np.diag(np.matmul(np.transpose(t), np.ones(t_dimensions)))
		return np.add(point_on_bezier_0, np.matmul(np.subtract(point_on_bezier_1,point_on_bezier_0), t_extended))

	def plot(self,t_count):
		t_values = np.array([np.linspace(0,1,t_count)])
		coordinates = self.compute_point(t_values)
		plt.plot(coordinates[0],coordinates[1])

	def overwrite_x0(self, x0: Point) -> None:
		self.bezier_0.overwrite_x0(x0)

	def update_x0(self, x:float, y:float) -> None:
		self.bezier_0.update_x0(x,y)

	def update_x1(self, x:float, y:float) -> None:
		self.bezier_0.update_x2(x,y)

	def update_x2(self, x:float, y:float) -> None:
		self.bezier_1.update_x2(x,y)

	def get_x0(self) -> Point:
		return self.bezier_0.get_x0()

	def get_x1(self) -> Point:
		return self.bezier_0.get_x2()

	def get_x2(self) -> Point:
		return self.bezier_1.get_x2()

	def return_points(self) -> list[Point]:
		return self.bezier_0.return_points() + self.bezier_1.return_points()