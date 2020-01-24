# -*- coding: utf-8 -*-
print ("Resultado")
# variaveis int
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 ** 3) #exponenciação
print(10 % 3) # resto da operação

"""

comentário de varias linhas

"""
# usando var
# var não pode ter caracteres especiais
# usar = (atribuição)

minha_variavel = "olá mundo!"

print(minha_variavel)
print(minha_variavel)

#var numerica/ bool

var1 = 1 #int
var2 = 1.1 #float
var3 = "Eu sou uma string" #var string
var4 = True #bool
var5 = False

print(var1)
print(var2)
print(var3)

""" 
Operadores relacionais

== igual
!= Diferente
>
<
>=
<= Divisão

"""
x = 2
y = 3

x = y

print(x) #x adquiriu o valor de y

print (x == y) #true, pois x possui o mesmo valor que y
print (x > y) #false
print (x < y) #false
print (x <= y) #true
print (x >= y) #true

soma = x + y 

print (soma) #6
print (soma > x) #true

# and, dois valores precisam ser verdadeiros para dar true, apenas um precisa ser falso

print (x == y and x == soma) #false
print (x == y and x != soma) #true

# or, apenas um dos valores precisa ser verdadeiro para dar true

print (x == y or y != x ) #true

# and e or

print (x == y or y == x and x >= y) #true

# trabalhando com if

if x == y:
    print ("x é igual a y")

#trabalhando com else

if x != y:
    print ("x é diferente de y")
else:
    print ("x não é diferente de y")

# trabalhando com if e else

if x == y:
    if x != 3:
        print ("primeiro if")
    else:
        print ("primeiro else")
else:
    print ("segundo else")

# trabalhando com elif (primeira condição verdadeira que existir)

if x != y:
    print ("primeiro if")
elif x == y:
    print ("elif")
else: 
    print ("else")

# estrutura de repetição While
"""
a = 2

while a < 10:
    print ("x")
    x = x+1 
"""

# lista numérica for


lista = [1,2,3,4,5]
lista2 = ["mathy","creater","!"]
lista3 = [0,"mathy","biscoito"]

for i in lista: 
    print(i)

# lista numérica range

# lista com valor de 9 elementos (0 a 9)
for i in range(10):
    print(i)
# lista com valor de 10 a 19
for c in range(10,20):
    print(c)
# pulando elementos no range (2 em 2)
for d in range(10,20,2):
    print(d)

# usando input (enviar informações para o programa)

# Input básico

#numero = input("digite um número ") 
#print("o número digitado é ")
#print(numero)

# String concatenada com valor de input

#nome = input("digite seu nome ")
#print("Bem vindo "+nome)

# concatenação

Nome1 = "MATHEUS"
Sobrenome = "CORRÊA"

# Obs, usar aspas na concatenação pra definir espaçamento de caracteres

concatenar = Nome1 + " " + Sobrenome
print(concatenar)

# Medir tamanho da string com Len

tamanho = len(concatenar)
print(tamanho)

# Mostrar caractere posicional com colchete
# Valor da máquina começa em 0, então posição 2 será letra t - Matheus (0,1,2...)

print(Nome1[2])

#Sequencia na String

seq = "MATHEUS CORRÊA"
print(seq[0:5])

#Sequencia até o final

seq = "MATHEUS CORRÊA"
print(seq[0:])

# Função lower e upper (Remover caixa alta/ colocar em caixa alta)

print(concatenar.lower())
print(concatenar.upper())

#Definir valor pra string

# concatenar = concatenar.upper()

#Caractere especial para quebra de linha

concatenar = Nome1 + " " + Sobrenome + "\n"

print(concatenar)

# remover cactere especial ou espaços indesejados 

print(concatenar.strip())

# Aleatório, sorteio

seq = range(11)
import random
aleatorio = random.choice(seq)
print(aleatorio)
if aleatorio == 10:
    print ("parabens, você ganhou um milhão de reais")
else:
    print ("você não ganhou")

# split string (Bom uso pra separar nomes)

minha_string = "Matheus Corrêa"
Nomes = minha_string.split(" ")
print ("primeiro nome:", Nomes[0])
print ("Sobrenome:", Nomes[1])

#Split string por letra

minha_string = "Matheus Corrêa"
Nomes = minha_string.split("C")
print (Nomes)

# Busca na string (número da palavra, índice)

Texto = "O rato roeu a roupa do rei de roma"
Busca = input ("Busca palavra: ")
Busca = Texto.find(Busca) # pode usar palavra ao invés de input
if Busca == -1:
    print("Resultado não encontrado")
else:
    print(Busca)

# Mostrar resultado após a posição da pesquisa

print(Texto[Busca:])

# Trocar palavra na string por método replace

Texto = Texto.replace ("o rei", "a rainha")
print(Texto)



























