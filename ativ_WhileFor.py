"""
Crie uma contagem Fibonacci até o número escolhido pelo usuário.

"""

#1
num = int(input("Digite um numero: "))

a = 0
b = 1

while a <= num:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

# usando uma varaivel temp p poder guardar o valor do "a".