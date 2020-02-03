# Declaração de lista

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 8.89, False]

# Item definido

print(minha_lista[2])

# Printar todos os itens

for item in minha_lista:
    print(item)

# Adicionar elementos

minha_lista.append("limao")
print(minha_lista)

# printar tamanho da lista

tamanho = len(minha_lista)
print(tamanho)

# Buscar elemento na lista

if 3 in minha_lista_2:
    print("3 esta na lista")

# Remover elementos de uma lista

del minha_lista[2:]
print(minha_lista)

# Apagar lista inteira

del minha_lista[:]
print(minha_lista)

# Ordenar lista (numérica e alfabéticamente)

listinha = [800,70,90,200,45,4242,45,6,7,8,9]
listinha.sort(reverse=True)
print(listinha)

# método direto = lista.reverse()

# Retornar Lista ordenada

listinha = sorted(listinha)
print(listinha)

# Dicionários

meu_dicionario = {"A":"AMEIXA", "B":"BOLA"}
print(meu_dicionario["B"])

# Navegação

for chave in meu_dicionario:
    print(chave+":"+meu_dicionario[chave])

# itens do dicionario

for i in meu_dicionario.items():
    print(i)

# apenas as chaves

for i in meu_dicionario.keys():
    print(i)

# Método aleatório

import random
# dar sempre o mesmo valor: random.seed(1)
numero = random.randint(0, 10)
print(numero)

# Método choice

lista = [6, 45, 9]
number = random.choice(lista)
print(number)

# Exceções 

a = 2
b = 0

try:
    print(a/b)
except:
    print("Não é permitida divisão por zero")

print(a/a)





