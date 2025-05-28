import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.BezierBuilder import BezierBuilder
import numpy as np

class TestBezierBuilder(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.beziers = []

    BezierBuilder.insert_linear_bezier(self.beziers,0,3,-4)
    BezierBuilder.insert_quadratic_bezier(self.beziers,1,3,-2)
    BezierBuilder.insert_linear_bezier(self.beziers,2,3,1)

  def test_validate_initial_beziers(self):
    pass
    

if __name__ == '__main__':
  unittest.main()