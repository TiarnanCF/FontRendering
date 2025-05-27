import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class LinearBezier:
	def __init__(self, x0: list[list[int]], x2: list[list[int]]):
		self.x0 = np.array(x0)
		self.x2 = np.array(x2)

	def compute_point(self, t: list|float|int|npt.NDArray) -> npt.NDArray:
		if type(t) in (float, int):
			t = np.array([[t]], float)
		elif type(t) is list:
			t = np.array([t], float)

		return np.add(self.x0, np.matmul(np.subtract(self.x2,self.x0),t))

	def plot(self,t_count: float) -> None:
		t_values = np.array([np.linspace(0,1,t_count)])
		coordinates = self.compute_point(t_values)
		plt.plot(coordinates[0],coordinates[1])

	def update_x0(self, x0: list[list[int]]) -> None:
		self.x0 = np.array(x0)

	def update_x2(self, x2: list[list[int]]) -> None:
		self.x2 = np.array(x2)
