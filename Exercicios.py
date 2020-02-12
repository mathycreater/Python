# Exercícios : Python

"""
Faça um programa que 
receba a idade do usuário e diga se ele é 
maior ou menor de idade. 



idade = 17
if idade >= 18:
  print("Usuário é maior de idade")
else:
  print("Usuário é menor de idade")



Faça um programa que receba duas notas digitadas pelo usuário. 
Se a nota for maior ou igual a seis, escreva aprovado, 
senão escreva reprovado.   

#Rapidao tentar aqui
#tem que usar só o que ele passou até agora, pelo menos
#conseguir resolver só com o basicão
# is, or, and, if, else, elif, ==, essas parada
# porra de lógica é essa do python que não to entendendo mano
#so converter pra int nesse caso, alias, tem que ser float
#pq na real o input, de forma geral so recebe string, ai a gnt tem que fazer essa conversão, é o que te digo das desvantagens de uma linguagem nao ser fortemente tipada
#So tentar uma parada aqui
#por que o float funfa e o int não?
#o int funfa sim, sq o float vc pode botar valores quebrados, ex.: 6.8...
# to falando merda, nota é quebrada
# saquei agora 
# se liga, caso vc queira tratar a principio quando o cara botar um a string tem que ser um try catch mesmo
#except?


#ele nao emeio que trata a exceção sem parar a aplicação, é como se fosse o catch do c# (dei uma pesquisada aqui), tipo, eu acho que deve existir alguma forma melhor de tratar isso

#Oq eu fiz ai, antes de entrar no try excerpt, eu coloquei o algorítimo da nota em uma função, então no try eu so tento executar a função, caso de algum erro ele cai no exerpt, exibe a mensagem e chama a função denovo.

#show mlk
"""

def inserirNota():
  nota = input("Digite a nota do aluno:")
  if float(nota) < 6:
      print ("Aluno reprovado")
  else:
      print ("Aluno aprovado")

try:
  inserirNota()
except:
  print('Favor inserir um número')
  inserirNota()


# malz, tinha caido a net la no trabalho... dedepois olha o wtsp la wue expliquei as paradas por audio... tu é meu orgulho mesmo, ta puto ai no python hahaha vlw

#ja é, vo olhar lá, to quebrando a cabeça aqui hfuahfaf

# AX² + BX + C 
"""
a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

def delta(a,b,c):
  delta = (b**2) - (4*a*c)
  return {"delta":delta}
def raizes(a,b,c,delta):
  x1 = (-b + delta**(1.0/2.0)) / (2*a) 
  x2 = (-b - delta**(1.0/2.0)) / (2*a)
  return {"x1":x1, "x2":x2}

delta = delta(a,b,c)
raizes = raizes(a,b,c,delta['delta'])

print(delta)
print(raizes)

#resultado = b * a - 1 * c * c
#print(resultado)


# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
"""
"""
import math

def operação():

  a = int(input("digite o primeiro valor: "))
  b = int(input("digite o segundo valor "))

  sinal = input("digite S para soma, N para subtração, M para multiplicação e D para divisão: ")

  if sinal == "S":
    soma = a + b
    print(soma)
  elif sinal == "N":
    sub = a - b
    print(sub)
  elif sinal == "M":
    mul = a * b
    print(mul)
    print("resultado é: ") + (mul)
  elif sinal == "D":
    div = a / b
    print(div)
    print("resultado é: ") + (div)
  else: ("Não foi possível reconhecer o comando")

try:
   operação()
except:
  print('Favor inserir um dos comandos válidos')
  operação()
"""