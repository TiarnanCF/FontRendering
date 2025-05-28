import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.LinearBezier import LinearBezier
import numpy as np

class TestLinearBezier(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.linear_bezier: LinearBezier = LinearBezier([[0], [0]], [[2], [1]])

  def test_compute_point_single_point(self):
    expected_point = np.array([[1.2],[0.6]])
    point = self.linear_bezier.compute_point([0.6])
    self.check_points_dimensions(point, expected_point)
    self.check_points_equal(point, expected_point)

    point = self.linear_bezier.compute_point(0.6)
    self.check_points_dimensions(point, expected_point)
    self.check_points_equal(point, expected_point)

  def test_compute_point_multiple_points(self):
    expected_points = np.array([[1, 1.2, 1.6],[0.5, 0.6, 0.8]])
    point = self.linear_bezier.compute_point([0.5, 0.6, 0.8])
    self.check_points_dimensions(point, expected_points)
    self.check_points_equal(point, expected_points)
    
  def test_compute_point_out_of_range(self):
    self.assertRaises(IndexError, self.linear_bezier.compute_point, -0.2)
    self.assertRaises(IndexError, self.linear_bezier.compute_point, 1.1)
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [-0.2])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [1.1])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [0.1, -0.2, 0.6])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [0.2, 1.1, 0.3])

  def test_update_x0(self):
    new_point = np.array([[1.2],[0.6]])
    self.check_points_not_equal(self.linear_bezier.x0, new_point)
    self.linear_bezier.update_x0(new_point)
    self.check_points_equal(self.linear_bezier.x0, new_point)

  def test_update_x2(self):
    new_point = np.array([[1.2],[0.6]])
    self.check_points_not_equal(self.linear_bezier.x2, new_point)
    self.linear_bezier.update_x2(new_point)
    self.check_points_equal(self.linear_bezier.x2, new_point)

  def check_points_dimensions(self, point, expected_point):
    m, n = np.shape(point)
    expected_m, expected_n = np.shape(expected_point)
    self.assertEqual(m, expected_m)
    self.assertEqual(n, expected_n)

  def check_points_equal(self, point, expected_point):
    point_difference = point - expected_point
    max_point_difference = np.amax(point_difference)
    mod_max_point_difference = abs(max_point_difference)
    self.assertTrue(mod_max_point_difference < TestLinearBezier.tolerance)

  def check_points_not_equal(self, point, expected_point):
    point_difference = point - expected_point
    max_point_difference = np.amax(point_difference)
    mod_max_point_difference = abs(max_point_difference)
    self.assertFalse(mod_max_point_difference < TestLinearBezier.tolerance)

if __name__ == '__main__':
  unittest.main()