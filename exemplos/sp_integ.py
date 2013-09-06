# -*- coding: UTF-8 -*-

import scipy.integrate as i

def f(x):
    return x + 2

print i.quad(f,0,10)
