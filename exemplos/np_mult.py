# -*- coding: UTF-8 -*-

import numpy as np

m = np.array([[10,2,3],[-2, 5, 8],[4, 8,-1]])
n = np.array([[12,2,3],[4,35,6],[8,10,7]])

print np.dot(m,n)

m = np.matrix([[10,2,3],[-2, 5, 8],[4, 8,-1]])
n = np.matrix([[12,2,3],[4,35,6],[8,10,7]])

print m * n
