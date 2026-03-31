"""
exercicios de lista
"""

# #1
vetor = []

for i in range(5):
    num = int(input("Digite numero: "))
    vetor.append(num)

print(vetor)

#2
vetor = []

for i in range(10):
    num = int(input("Digite um numero: "))
    vetor.append(num)
# ordem inversa
vetor.reverse()

print(f"numeros invertidos: {vetor}")

#3
vetor = []
soma = 0

for i in range(4):

    num = float(input(f"Digite {i + 1} nota: "))
    vetor.append(num)
    soma += num

#len() - tamanho do vetor. length
media = soma / len(vetor)
print(vetor)
print(f"media é : {media}")