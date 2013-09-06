# -*- coding: UTF-8 -*-

import scipy.interpolate as i
import numpy as np

x = np.linspace(0, 10, 6)
y = np.sin(x)

f = i.interp1d(x, y, kind='cubic')
xinterp = np.linspace(0, 10, 100)

import matplotlib.pyplot as plt
plt.plot(x,y,"o",xinterp,f(xinterp),"-")
plt.legend(["Dados", u"Cúbica"],loc="best")
plt.show()
