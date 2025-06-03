import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.Point import Point
from FontRender.CorePackages.HelperPackages.BezierHelper.Point import Node
import numpy as np

class TestPoint(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.point_x = Point(-1,0.5,True)
    self.point_y = Point(2,1,False, self.point_x)
    self.point_z = Point(2,1,True, self.point_y)

    self.node_x = Node()
    self.node_y = Node(self.node_x)
    self.node_z = Node(self.node_y)

  def test_node_has_next_true(self):
    self.assertTrue(self.node_y.has_next())

  def test_node_has_next_false(self):
    self.assertFalse(self.node_x.has_next())

  def test_node_get_next_node(self):
    self.assertTrue(self.node_y.get_next() is self.node_x)

  def test_node_get_next_none(self):
    self.assertTrue(self.node_x.get_next() is None)

  def test_node_update_next_node(self):
    self.assertFalse(self.node_y.next is self.node_z)
    self.assertFalse(self.node_x.next is self.node_y)
    self.node_y.update_next(self.node_z)
    self.node_x.update_next(self.node_y)
    self.assertTrue(self.node_y.next is self.node_z)
    self.assertTrue(self.node_x.next is self.node_y)

  def test_node_update_next_none(self):
    self.assertFalse(self.node_y.next is None)
    self.node_y.update_next(None)
    self.node_x.update_next(None)
    self.assertTrue(self.node_y.next is None)
    self.assertTrue(self.node_x.next is None)

  def test_point_subtraction(self):
    new_point = self.point_y - self.point_x
    self.assertEqual(new_point.x, 3)
    self.assertEqual(new_point.y, 0.5)

  def test_point_equal(self):
    self.assertEqual(self.point_y, self.point_z)
    self.assertNotEqual(self.point_x, self.point_y)

  def test_point_get_coordinates(self):
    expected_coordinates = np.array([[-1], [0.5]])
    coordinates = self.point_x.get_coordinates()
    self.check_arrays_dimensions(coordinates, expected_coordinates)
    self.check_arrays_equal(coordinates, expected_coordinates)

  def test_point_get_x(self):
    expected_x_value = -1
    self.assertTrue(expected_x_value, self.point_x.get_x())

  def test_point_get_y(self):
    expected_y_value = 0.5
    self.assertTrue(expected_y_value, self.point_x.get_y())

  def test_point_check_is_on_curve(self):
    self.assertTrue(self.point_x.check_is_on_curve())
    self.assertFalse(self.point_y.check_is_on_curve())

  def test_point_update_x(self):
    new_x_value = -2
    self.assertNotEqual(new_x_value, self.point_x.x)
    self.point_x.update_x(new_x_value)
    self.assertEqual(new_x_value, self.point_x.x)

  def test_point_update_y(self):
    new_y_value = 3
    self.assertNotEqual(new_y_value, self.point_x.y)
    self.point_x.update_y(new_y_value)
    self.assertEqual(new_y_value, self.point_x.y)

  def test_point_update_is_on_curve_true(self):
    self.assertTrue(self.point_x.check_is_on_curve())
    self.assertFalse(self.point_y.check_is_on_curve())
    self.point_x.update_is_on_curve(True)
    self.point_y.update_is_on_curve(True)
    self.assertTrue(self.point_x.check_is_on_curve())
    self.assertTrue(self.point_y.check_is_on_curve())

  def test_point_update_is_on_curve_false(self):
    self.assertTrue(self.point_x.check_is_on_curve())
    self.assertFalse(self.point_y.check_is_on_curve())
    self.point_x.update_is_on_curve(False)
    self.point_y.update_is_on_curve(False)
    self.assertFalse(self.point_x.check_is_on_curve())
    self.assertFalse(self.point_y.check_is_on_curve())

  def check_arrays_dimensions(self, point, expected_point):
    m, n = np.shape(point)
    expected_m, expected_n = np.shape(expected_point)
    self.assertEqual(m, expected_m)
    self.assertEqual(n, expected_n)

  def check_arrays_equal(self, array, expected_array):
    array_difference = array - expected_array
    max_array_difference = np.amax(array_difference)
    mod_max_array_difference = abs(max_array_difference)
    self.assertTrue(mod_max_array_difference < TestPoint.tolerance)

if __name__ == '__main__':
  unittest.main()