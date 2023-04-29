#importando modulo de gerador de pseudo-random numeros
import random

#metodo chr para conventer um integer em um caractere
upper_case = chr(random.randint(65,90))
lower_case = chr(random.randint(97,122))
special_chr = chr(random.randint(33,39))
list = []
password = upper_case , lower_case, special_chr, list



#criando uma lista de até 4 aleatorios
for i in range(4): 
    numbers = random.randrange(9)
    list.append(numbers)

#utilizando shuffle para embaralhar os numeros
random.shuffle(list)

#transformando a variavel "list" em uma string
list = str(list) [1:-1] 
list = list.replace (',','')

print (upper_case,lower_case,special_chr,list) 
