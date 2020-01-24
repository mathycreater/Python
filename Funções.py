# -*- coding: utf-8 -*-
"""
 Funções usando Def

 soma 
 
 Usar o return para armazenar valores

"""
def soma(x, y):
    return x+y
s = soma(2, 3)
print(s)

def subtração(x, y):
    return x-y
sub = subtração(4, 4)
print(sub)

def multiplicação(x,y):
    return x*y
m = multiplicação(5,6)
print(m)

# Reaproveitando funções definidas/ Multiplas funções

print(soma(s, m))
print(subtração(s, m))

# Aleatório, sorteio

seq = range(11)
import random
aleatorio = random.choice(seq)
if aleatorio == 10:
    print ("parabens, você ganhou um milhão de reais")
else:
    print ("você não ganhou")




