import random
a = input('Nome: ')
b = input('Nome: ')
c = input('Nome: ')
d = input('Nome: ')
lista = ([ a, b, c, d])
while True:
    random.shuffle(lista)
    print(lista)