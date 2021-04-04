#!/usr/bin/python
import sys

#  o laco for vai percorrer cada linha do arquivo

# basicamente os dados que passar por esse metodo gerara um conjunto de (Key): (Valor). Exemplo-> BA:  105.00

# Logo apos o mapper teremos uma fase sort gerenciado exclusivamente pelo hadoop classificando os dados, e ainda na etapa sort, ele agrupara os valores. 

for line in sys.stdin: # laco de leitura das linhas
    line = line.strip() # remove os espacos caso houver
    fields = line.split(";") # separa as colunas
    estado = fields[2] # pega o estado na coluna 3
    estado = estado[1:-1] # pega o valor do campo
    valor = fields[8] # pega o valor na coluna 9
    valor = valor[1:-1] # pega o valor do campo
    valor = str(valor.replace(",",".")) # se tiver valores com virgula substitui por ponto
    print("%s\t%s" % (estado,valor)) # printa na tela estado e valor