"""
1.Crie
um programa que solicite ao usuário uma nota entre zero e dez. Se o valor
informado for inválido, exiba uma mensagem de erro e continue solicitando uma
nota válida até que o usuário a forneça.

2.Desenvolva
um programa que calcule e exiba a média aritmética de N notas fornecidas pelo
usuário.

3.Desenvolva um programa que calcule a média de
alunos por turma. Para isso, siga os passos abaixo:
Solicite
ao usuário a quantidade de turmas;
Para
cada turma, peça que o usuário informe a quantidade de alunos;
Certifique-se
de que o número de alunos por turma não ultrapasse 40;
"""

# #1
while True:
    nota = float(input("Digie uma nota de 1 a 10: "))
    if nota >= 1 and nota <= 10:
        print(f"sua nota é {nota}")
        break
    else:
        print("nota invalida")
    
#2
count = 0
soma_notas = 0
while True:
    nota = float(input("Digite a sua nota: (e -1 para sair) "))
    
    if nota == -1 :
        break
    if nota > 0:
        soma_notas += nota
        count += 1
    else:
        print("nota invalida, digite uma nota ou -1 para sair")

if count > 0:
    media = soma_notas / count
    print(f"sua media é {media}")
else:
    print("nenhuma nota foi informada.")

#3
turmas = int(input("Digite a quantidade de turmas: "))

contador = 0
total_alunos = 0

while contador < turmas:
    alunos = int(input(f"Digite a quantidade de alunos da turma {contador + 1}: "))
    
    # validação (máximo 40 alunos)
    if alunos > 40:
        print("Erro: uma turma não pode ter mais de 40 alunos.")
    else:
        total_alunos += alunos
        contador += 1

media_alunos = total_alunos / turmas

print(f"Média de alunos por turma: {media_alunos:.2f}")