# -*- coding: UTF-8 -*-

import scipy.misc as misc
import matplotlib.pyplot as plt

img = misc.imread("./img/baboon.tif")
plt.imshow(img, cmap=plt.cm.Greys_r)
plt.show()
