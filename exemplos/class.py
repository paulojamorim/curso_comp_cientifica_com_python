# -*- coding: UTF-8 -*-
class Calculadora:    
    def __init__(self):
        self.pi = 3.14

    def soma(self, n1, n2):
        return n1 + n2

    def get_pi(self):
        return self.pi

c = Calculadora()
print c.soma(2,2)
print c.get_pi()
print c.pi
