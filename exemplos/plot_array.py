# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((100,100))

xc = 50
yc = 50
r = 40

for circ in xrange(360):
    theta = np.radians(circ)
    x = xc + r*np.cos(theta)
    y = yc + r*np.sin(theta)
    img[x,y] = 255
    
plt.imshow(img, cmap=plt.cm.Greys_r)
plt.show()
