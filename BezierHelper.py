import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

class linear_bezier:
	def __init__(self, x0, x1):
		self.x0 = x0
		self.x1 = x1

	def compute_point(self, t):
		return np.add(self.x0, np.matmul(np.subtract(self.x1,self.x0),t))

class quadratic_bezier:
	def __init__(self, x0, x1, x2):
		self.x0 = x0
		self.x1 = x1
		self.x2 = x2
		self.bezier_0 = linear_bezier(x0,x1)
		self.bezier_1 = linear_bezier(x1,x2)

	def compute_point(self, t):
		point_on_bezier_0 = self.bezier_0.compute_point(t)
		point_on_bezier_1 = self.bezier_1.compute_point(t)
		t_dimensions = t.shape
		t_extended = np.diag(t[0])#np.diag(np.matmul(np.transpose(t), np.ones(t_dimensions)))
		return np.add(point_on_bezier_0, np.matmul(np.subtract(point_on_bezier_1,point_on_bezier_0), t_extended))


#my_bezier = linear_bezier(np.array([[0],[0]]), np.array([[2],[1]]))

#t_values = np.array([np.linspace(0,1,10)])
#print(my_bezier.compute_point(t_values))

#plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])
#plt.show()

my_bezier = quadratic_bezier(np.array([[0],[0]]), np.array([[2],[1]]), np.array([[1],[1]]))

t_values = np.array([np.linspace(0,1,100)])

print(my_bezier.compute_point(t_values))

plt.plot(my_bezier.compute_point(t_values)[0],my_bezier.compute_point(t_values)[1])
plt.show()
