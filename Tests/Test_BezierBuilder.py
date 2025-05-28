import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.BezierBuilder import BezierBuilder
from FontRender.CorePackages.HelperPackages.BezierHelper.QuadraticBezier import QuadraticBezier
import numpy as np

class TestBezierBuilder(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.beziers = []

    BezierBuilder.insert_linear_bezier(self.beziers,0,3,-4)
    BezierBuilder.insert_quadratic_bezier(self.beziers,1,3,-2)
    BezierBuilder.insert_linear_bezier(self.beziers,2,3,1)

    self.validate_beziers()

  def test_validate_initial_beziers(self):
    pass

  def validate_beziers(self):
    next_point = self.beziers[0].x0
    for bezier in self.beziers:
      self.assertTrue(bezier.x0 is next_point)
      next_point = next_point.get_next()
      if isinstance(bezier, QuadraticBezier):
        self.assertTrue(bezier.x1 is next_point)
        next_point = next_point.get_next()

      self.assertTrue(bezier.x2 is next_point)

    

if __name__ == '__main__':
  unittest.main()