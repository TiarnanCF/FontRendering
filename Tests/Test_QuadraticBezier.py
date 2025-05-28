import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.QuadraticBezier import QuadraticBezier
from FontRender.CorePackages.HelperPackages.BezierHelper.Point import Point
import numpy as np

class TestQuadraticBezier(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.x0 = Point(0,0,True)
    self.x1 = Point(2,1,False)
    self.x2 = Point(3,-1,False)
    self.quadratic_bezier: QuadraticBezier = QuadraticBezier(self.x0, self.x1, self.x2)
    self.new_point = Point(1.2,0.6, True)

  def test_compute_point_single_point(self):
    expected_point = np.array([[2.04],[0.12]])
    point = self.quadratic_bezier.compute_point([0.6])
    self.check_arrays_dimensions(point, expected_point)
    self.check_arrays_equal(point, expected_point)

    point = self.quadratic_bezier.compute_point(0.6)
    self.check_arrays_dimensions(point, expected_point)
    self.check_arrays_equal(point, expected_point)
    
  def test_compute_point_multiple_points(self):
    expected_points = np.array([[1.75, 2.04, 2.56],[0.25, 0.12, -0.32]])
    point = self.quadratic_bezier.compute_point([0.5, 0.6, 0.8])
    self.check_arrays_dimensions(point, expected_points)
    self.check_arrays_equal(point, expected_points)
    
  def test_compute_point_out_of_range(self):
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, -0.2)
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, 1.1)
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, [-0.2])
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, [1.1])
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, [0.1, -0.2, 0.6])
    self.assertRaises(IndexError, self.quadratic_bezier.compute_point, [0.2, 1.1, 0.3])

  def test_update_x0(self):
    self.assertFalse(self.quadratic_bezier.bezier_0.x0 == self.new_point)
    self.quadratic_bezier.update_x0(self.new_point.x, self.new_point.y)
    self.assertTrue(self.quadratic_bezier.bezier_0.x0 == self.new_point)

  def test_update_x1(self):
    self.assertFalse(self.quadratic_bezier.bezier_0.x2 == self.new_point)
    self.assertFalse(self.quadratic_bezier.bezier_1.x0 == self.new_point)
    self.quadratic_bezier.update_x1(self.new_point.x, self.new_point.y)
    self.assertTrue(self.quadratic_bezier.bezier_0.x2 == self.new_point)
    self.assertTrue(self.quadratic_bezier.bezier_1.x0 == self.new_point)

  def test_update_x2(self):
    self.assertFalse(self.quadratic_bezier.bezier_1.x2 == self.new_point)
    self.quadratic_bezier.update_x2(self.new_point.x, self.new_point.y)
    self.assertTrue(self.quadratic_bezier.bezier_1.x2 == self.new_point)

  def check_arrays_dimensions(self, point, expected_point):
    m, n = np.shape(point)
    expected_m, expected_n = np.shape(expected_point)
    self.assertEqual(m, expected_m)
    self.assertEqual(n, expected_n)

  def check_arrays_equal(self, array, expected_array):
    array_difference = array - expected_array
    max_array_difference = np.amax(array_difference)
    mod_max_array_difference = abs(max_array_difference)
    self.assertTrue(mod_max_array_difference < TestQuadraticBezier.tolerance)

  def check_arrays_not_equal(self, array, expected_array):
    array_difference = array - expected_array
    max_array_difference = np.amax(array_difference)
    mod_max_array_difference = abs(max_array_difference)
    self.assertFalse(mod_max_array_difference < TestQuadraticBezier.tolerance)

if __name__ == '__main__':
  unittest.main()