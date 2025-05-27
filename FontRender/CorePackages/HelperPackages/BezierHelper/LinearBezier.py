import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class LinearBezier:
	def __init__(self, x0: list[list[int]], x1: list[list[int]]):
		self.x0 = np.array(x0)
		self.x1 = np.array(x1)

	def compute_point(self, t: list|float|int|npt.NDArray) -> npt.NDArray:
		if type(t) in (float, int):
			t = np.array([[t]], float)
		elif type(t) is list:
			t = np.array([t], float)

		return np.add(self.x0, np.matmul(np.subtract(self.x1,self.x0),t))

	def plot(self,t_count: float) -> None:
		t_values = np.array([np.linspace(0,1,t_count)])
		coordinates = self.compute_point(t_values)
		plt.plot(coordinates[0],coordinates[1])

		
#t_values = np.array([np.linspace(0,1,100)])

#my_bezier = LinearBezier(np.array([[0],[0]]), np.array([[2],[1]]))

#print(my_bezier.compute_point(t_values))

#plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])

#my_bezier = quadratic_bezier(np.array([[0],[0]]), np.array([[2],[1]]), np.array([[1],[1]]))


#print(my_bezier.compute_point(t_values))

#plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])
#plt.show()
