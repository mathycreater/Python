# -*- coding: utf=8 -*-
"""
Métodos para escrever em arquivo

r - somente leitura
w - rescreve em cima do arquivo, apaga a informação anterior
a - adiciona a informação escrita a anterior
\n - quebra de linha
r+ - leitura e escrita
w+ - escrita, criando novo arquivo
a+ leitura e escrita para atualização

"""

w = open ("c:/Users/Minecraft/Desktop/arquivo2.txt", "w")
w.write("Esse é meu arquivo")
w.close()