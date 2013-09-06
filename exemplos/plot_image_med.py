# -*- coding: UTF-8 -*-

import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.imread("./img/baboon.tif")

img_filt = ndi.median_filter(img,(6,6))

fig = plt.figure()

fig.add_subplot(1,2,1)
plt.title("Original")
plt.imshow(img,cmap=plt.cm.Greys_r)

fig.add_subplot(1,2,2)
plt.title("Filtrada")
plt.imshow(img_filt, cmap=plt.cm.Greys_r)

plt.show()
