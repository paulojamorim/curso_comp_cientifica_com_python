# -*- coding: UTF-8 -*-

import numpy as np

m = np.array([[10,2,3],[-2, 5, 8],[4, 8,-1]])

print m[0,0]

print m.diagonal()

print m.transpose()

print np.linalg.det(m)
