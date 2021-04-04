#!/usr/bin/python
import sys

# Aqui nosso programa reduce fara a leitura dos dados gerados pela etapa sort (classificados e agrupados)

previous_value = ""
sum = 0.0
for line in sys.stdin: # laco de leitura das linhas
    line = line.strip() # remove os espacos caso houver
    value, count = line.split("\t") # separa os valores
    try:
        count = float(count) # conta quantos dados tem

        if value == previous_value: # Soma os valores da mesma key
            sum += count
        else:
            # key de valor unico
            print("%s\t%s" % (previous_value, sum))
            previous_value = value
            sum = count
            
    except:
        print("")
    
    
print("%s\t%s" % (previous_value, sum))

# BA: 193.00 , 105.00
#   entra aqui e sai
# BA: 298.00