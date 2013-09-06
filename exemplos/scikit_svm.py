# -*- coding: UTF-8 -*-

import glob
import scipy.misc as misc
import scipy.ndimage as ndi
import sklearn.svm as svm
import skimage.morphology as morp

treinamento = glob.glob("img/treinamento/*.tif")
treinamento.sort()

caract = []
for f in treinamento:
    img_entrada = misc.imread(f)
    rotulos, n_obj = ndi.label(img_entrada)
    objetos = ndi.find_objects(rotulos)
    img_objeto = rotulos[objetos[0]]
    
    img_norm = misc.imresize(img_objeto,(140,70))
    img_eixo = morp.medial_axis(img_norm)
    vetor_caract = img_eixo.reshape(140*70)
    caract.append(vetor_caract)

objetivo = ["1"] * 10 + ["9"]  * 10 

clf = svm.SVC()
clf.fit(caract,objetivo)

img_teste = misc.imread("img/teste/9a.tif")

rotulos, n_obj = ndi.label(img_teste)
objetos = ndi.find_objects(rotulos)
img_objeto = rotulos[objetos[0]]

img_norm = misc.imresize(img_objeto,(140,70))
img_eixo = morp.medial_axis(img_norm)

vetor_caract = img_eixo.reshape(140*70)
pred = clf.predict(vetor_caract)

print "\n\n O numero de entrada é", pred[0]
