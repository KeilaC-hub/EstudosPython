'''
sintaxe básica lambda
lambda {argumentos}: {expressão}

exemplo:

soma = lambda x, y: x + y
print(soma(2, 3))
'''

# nesse caso acima o resultado está sendo armazenado em uma variável
# mas posso chamá-la diretamente
print((lambda x, y: x + y)(2, 3))

# função normal do exemplo acima
def soma2(x, y):
  return x + y
print(soma2(2, 3))

# lambda com map
lista = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, lista)))

precos = [125, 400, 15, 37]
impostos = list(map(lambda x: x*0.3, precos))
print(impostos)

# lambda com filter
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, lista)))

# lambda com reduce
from functools import reduce
lista = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, lista))

