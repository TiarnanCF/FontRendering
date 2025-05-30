import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from .Point import Point

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class LinearBezier:
	def __init__(self, x0: Point, x2: Point):
		self.x0 = x0
		self.x2 = x2

	def compute_point(self, t: list|float|int|npt.NDArray) -> npt.NDArray:
		if type(t) in (float, int):
			t = np.array([[t]], float)
		elif type(t) is list:
			t = np.array([t], float)

		if np.amax(t) > 1 or np.amin(t) < 0:
			raise IndexError("t must be in the range [0,1]")

		return np.add(self.x0.get_coordinates(), np.matmul(np.subtract(self.x2.get_coordinates(),self.x0.get_coordinates()),t))

	def plot(self,t_count: float) -> None:
		t_values = np.array([np.linspace(0,1,t_count)])
		coordinates = self.compute_point(t_values)
		plt.plot(coordinates[0],coordinates[1])

	def overwrite_x0(self, x0: Point) -> None:
		self.x0 = x0

	def overwrite_x2(self, x2: Point) -> None:
		self.x2 = x2

	def update_x0(self, x: float, y: float) -> None:
		self.x0.update_x(x)
		self.x0.update_y(y)

	def update_x2(self, x: float, y: float) -> None:
		self.x2.update_x(x)
		self.x2.update_y(y)

	def get_x0(self) -> Point:
		return self.x0

	def get_x1(self) -> Point:
		return self.x2

	def get_x2(self) -> Point:
		return self.x2

	def return_points(self) -> list[Point]:
		return [self.x0, self.x2]