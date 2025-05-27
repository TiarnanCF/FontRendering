import matplotlib.pyplot as plt
import numpy as np
from .LinearBezier import LinearBezier

class QuadraticBezier:
	def __init__(self, x0, x1, x2):
		self.x0 = x0
		self.x1 = x1
		self.x2 = x2
		self.bezier_0 = LinearBezier(x0,x1)
		self.bezier_1 = LinearBezier(x1,x2)

	def compute_point(self, t):
		if type(t) in (float, int):
			t = np.array([[t]], float)
		elif type(t) is list:
			t = np.array([t], float)

		point_on_bezier_0 = self.bezier_0.compute_point(t)
		point_on_bezier_1 = self.bezier_1.compute_point(t)
		t_dimensions = t.shape
		t_extended = np.diag(t[0])#np.diag(np.matmul(np.transpose(t), np.ones(t_dimensions)))
		return np.add(point_on_bezier_0, np.matmul(np.subtract(point_on_bezier_1,point_on_bezier_0), t_extended))

	def plot(self,t_count):
		t_values = np.array([np.linspace(0,1,t_count)])
		coordinates = self.compute_point(t_values)
		plt.plot(coordinates[0],coordinates[1])

	def update_x0(self, x0: list[list[int]]) -> None:
		self.x0 = x0

	def update_x1(self, x1: list[list[int]]) -> None:
		self.x1 = x1

	def update_x2(self, x2: list[list[int]]) -> None:
		self.x2 = x2