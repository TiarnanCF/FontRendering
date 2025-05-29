import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.BezierBuilder import BezierBuilder
from FontRender.CorePackages.HelperPackages.BezierHelper.QuadraticBezier import QuadraticBezier
from FontRender.CorePackages.HelperPackages.BezierHelper.LinearBezier import LinearBezier
from FontRender.CorePackages.HelperPackages.BezierHelper.Point import Point
import numpy as np

class TestBezierBuilder(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.beziers = []

    BezierBuilder.insert_linear_bezier(self.beziers,0,3,-4)
    BezierBuilder.insert_quadratic_bezier(self.beziers,1,3,-2)
    BezierBuilder.insert_linear_bezier(self.beziers,2,3,1)

    self.validate_beziers()

  def test_reduce_to_linear_bezier(self):
    quadratic_bezier = self.beziers[1]
    linear_bezier = BezierBuilder.reduce_to_linear_bezier(quadratic_bezier)
    self.assertTrue(linear_bezier.get_x0() is quadratic_bezier.get_x0())
    self.assertTrue(linear_bezier.get_x2() is quadratic_bezier.get_x2())
    self.assertTrue(isinstance(linear_bezier, LinearBezier))

    self.beziers[1] = linear_bezier
    self.validate_beziers()

  def test_enhance_to_quadratic_bezier(self):
    linear_bezier = self.beziers[0]
    new_point_x1 = Point(1.3,2,False)
    quadratic_bezier = BezierBuilder.enhance_to_quadratic_bezier(linear_bezier, new_point_x1)
    self.assertTrue(linear_bezier.get_x0() is quadratic_bezier.get_x0())
    self.assertTrue(linear_bezier.get_x2() is quadratic_bezier.get_x2())
    self.assertTrue(isinstance(quadratic_bezier, QuadraticBezier))
    self.assertEqual(new_point_x1, quadratic_bezier.get_x1())

    self.beziers[0] = quadratic_bezier
    self.validate_beziers()

  def validate_beziers(self):
    next_point = self.beziers[0].get_x0()
    for bezier in self.beziers:
      self.assertTrue(bezier.get_x0() is next_point)
      next_point = next_point.get_next()

      if isinstance(bezier, QuadraticBezier):
        self.assertTrue(bezier.get_x1() is next_point)
        next_point = next_point.get_next()

      self.assertTrue(bezier.get_x2() is next_point)

if __name__ == '__main__':
  unittest.main()