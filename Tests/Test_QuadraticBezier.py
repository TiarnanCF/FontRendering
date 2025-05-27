import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.QuadraticBezier import QuadraticBezier
import numpy as np

class TestQuadraticBezier(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.linear_bezier: QuadraticBezier = QuadraticBezier([[0], [0]], [[2], [1]], [[3], [-1]])

  def test_compute_point(self):
    expected_point = np.array([[2.04],[0.12]])
    point = self.linear_bezier.compute_point([0.6])
    self.check_points_dimensions(point, expected_point)
    self.check_points_equal(point, expected_point)

    point = self.linear_bezier.compute_point(0.6)
    self.check_points_dimensions(point, expected_point)
    self.check_points_equal(point, expected_point)

  def test_compute_points(self):
    expected_points = np.array([[1.75, 2.04, 2.56],[0.25, 0.12, -0.32]])
    point = self.linear_bezier.compute_point([0.5, 0.6, 0.8])
    self.check_points_dimensions(point, expected_points)
    self.check_points_equal(point, expected_points)

  def check_points_dimensions(self, point, expected_point):
    m, n = np.shape(point)
    expected_m, expected_n = np.shape(expected_point)
    self.assertEqual(m, expected_m)
    self.assertEqual(n, expected_n)

  def check_points_equal(self, point, expected_point):
    point_difference = point - expected_point
    max_point_difference = np.amax(point_difference)
    mod_max_point_difference = abs(max_point_difference)
    self.assertTrue(mod_max_point_difference < TestQuadraticBezier.tolerance)

if __name__ == '__main__':
  unittest.main()