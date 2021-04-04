#!/usr/bin/env python
import sys
import os
from random import randint

# Selecionar um numero randomico para saltar

saida = "202001_BF_Amostra.csv"

lin = 0
with open(saida, 'w+') as file:
    for line in sys.stdin:
        # so grava de tantos em tantos registros
        lineTest = line.strip()
        fields = lineTest.split(";") 
        estado = fields[2]
        estado = estado[1:-1]
        
        # Para gerar uma amostra apenas de MG
        if estado == "MG":
            file.write(line)
            lin += 1
            # Quando passar de 1.000.000 registros gravados
            if (lin > 1000000):
                break

print(lin, 'gravadas')
file.close()