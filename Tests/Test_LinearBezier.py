import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.LinearBezier import LinearBezier
from FontRender.CorePackages.HelperPackages.BezierHelper.Point import Point
import numpy as np

class TestLinearBezier(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.point_x = Point(0,0,True)
    self.point_y = Point(2,1,True)
    self.linear_bezier: LinearBezier = LinearBezier(self.point_x, self.point_y)
    self.new_point = Point(1.2,0.6, True)

    self.assertTrue(self.point_x is self.linear_bezier.x0)
    self.assertFalse(self.point_x is self.linear_bezier.x2)
    self.assertTrue(self.point_y is self.linear_bezier.x2)
    self.assertFalse(self.point_y is self.linear_bezier.x0)

  def test_compute_point_single_point(self):
    expected_point = np.array([[1.2],[0.6]])
    point = self.linear_bezier.compute_point([0.6])
    self.check_arrays_dimensions(point, expected_point)
    self.check_arrays_equal(point, expected_point)

    point = self.linear_bezier.compute_point(0.6)
    self.check_arrays_dimensions(point, expected_point)
    self.check_arrays_equal(point, expected_point)

  def test_compute_point_multiple_points(self):
    expected_points = np.array([[1, 1.2, 1.6],[0.5, 0.6, 0.8]])
    point = self.linear_bezier.compute_point([0.5, 0.6, 0.8])
    self.check_arrays_dimensions(point, expected_points)
    self.check_arrays_equal(point, expected_points)
    
  def test_compute_point_out_of_range(self):
    self.assertRaises(IndexError, self.linear_bezier.compute_point, -0.2)
    self.assertRaises(IndexError, self.linear_bezier.compute_point, 1.1)
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [-0.2])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [1.1])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [0.1, -0.2, 0.6])
    self.assertRaises(IndexError, self.linear_bezier.compute_point, [0.2, 1.1, 0.3])

  def test_update_x0(self):
    self.assertNotEqual(self.linear_bezier.x0, self.new_point)
    self.linear_bezier.update_x0(self.new_point.x, self.new_point.y)
    self.assertEqual(self.linear_bezier.x0, self.new_point)

  def test_update_x2(self):
    self.assertNotEqual(self.linear_bezier.x2, self.new_point)
    self.linear_bezier.update_x2(self.new_point.x, self.new_point.y)
    self.assertEqual(self.linear_bezier.x2, self.new_point)

  def test_overwrite_x0(self):
    self.assertFalse(self.new_point is self.linear_bezier.x0)
    self.linear_bezier.overwrite_x0(self.new_point)
    self.assertTrue(self.new_point is self.linear_bezier.x0)

  def test_overwrite_x2(self):
    self.assertFalse(self.new_point is self.linear_bezier.x2)
    self.linear_bezier.overwrite_x2(self.new_point)
    self.assertTrue(self.new_point is self.linear_bezier.x2)

  def test_get_x0(self):
    self.assertTrue(self.point_x is self.linear_bezier.get_x0())

  def test_get_x1(self):
    self.assertTrue(self.point_y is self.linear_bezier.get_x1())

  def test_get_x2(self):
    self.assertTrue(self.point_y is self.linear_bezier.get_x2())
    
  def test_return_points(self):
    points = self.linear_bezier.return_points()
    self.assertEqual(len(points), 2)
    self.assertTrue(self.point_x is points[0])
    self.assertTrue(self.point_y is points[1])

  def check_arrays_dimensions(self, point, expected_point):
    m, n = np.shape(point)
    expected_m, expected_n = np.shape(expected_point)
    self.assertEqual(m, expected_m)
    self.assertEqual(n, expected_n)

  def check_arrays_equal(self, array, expected_array):
    array_difference = array - expected_array
    max_array_difference = np.amax(array_difference)
    mod_max_array_difference = abs(max_array_difference)
    self.assertTrue(mod_max_array_difference < TestLinearBezier.tolerance)

  def check_arrays_not_equal(self, array, expected_array):
    array_difference = array - expected_array
    max_array_difference = np.amax(array_difference)
    mod_max_array_difference = abs(max_array_difference)
    self.assertFalse(mod_max_array_difference < TestLinearBezier.tolerance)

if __name__ == '__main__':
  unittest.main()