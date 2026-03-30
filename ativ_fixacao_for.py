"""
1. Desenvolva
um programa que funcione da seguinte maneira: Solicite ao usuário que informe a
quantidade total de pessoas em um grupo. Para cada pessoa, peça que o
usuário registre o sexo, utilizando a letra 'm' ou 'M' para masculino. O programa deve contar e, ao final,
exibir o total de pessoas do sexo masculino.

2. Desenvolva
um programa em Python que utilize os comandos aprendidos para identificar e
exibir todos os números pares entre 1 e 100.

3. Crie
um programa que leia 5 números e calcule a soma e a média desses números,
exibindo os resultados.

4. Desenvolva um programa que solicite ao usuário um nome e uma senha,
garantindo que a senha não seja igual ao nome de usuário. Se forem iguais,
exiba uma mensagem de erro e peça as informações novamente.
"""
#1
total = int(input("Informe a quantidade de pessoas: "))
contador_m = 0

for i in range(total):
    sexo = input(f"Informe o sexo da pessoa {i+1} (M/F): ")
    
    if sexo == 'm' or sexo == 'M':
        contador_m += 1

print("Total de pessoas do sexo masculino:", contador_m)

#2
for i in range(1, 101):
    if i % 2 == 0:
        print(i , "é numero par")

#3
soma = 0

for i in range(5):
    num = float(input(f"Digite o {i+1} numero: "))
    soma += num

media = soma / 5

print("Soma:", soma)
print("Media:", media)

#4
while True:
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    
    if senha == nome:
        print("Erro: a senha nao pode ser igual ao nome. Tente novamente.\n")
    else:
        print("Cadastro realizado com sucesso!")
        break
