import unittest
from FontRender.CorePackages.HelperPackages.BezierHelper.LinearBezier import LinearBezier
import numpy as np

class TestLinearBezier(unittest.TestCase):
  def setUp(self):
    self.linear_bezier: LinearBezier = LinearBezier(np.array([[0], [0]]), np.array([[2], [1]]))

  def test_module(self):
    self.assertEqual(self.linear_bezier.compute_point(0.5),np.array([1],[0.5]))

if __name__ == '__main__':
  unittest.main()