import unittest
from FontRender.CorePackages.HelperPackages.ContourHelper.Contour import Contour
import numpy as np

class TestContour(unittest.TestCase):
  tolerance = 0.000000001

  def setUp(self):
    self.contour: Contour = Contour([1,1,2,3,4,3,10,4,1],[0,-2,-7,3,2,1,3,6,6],[1,0,1,0,1,1,0,1,0])

if __name__ == '__main__':
  unittest.main()