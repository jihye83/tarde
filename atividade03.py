"""
1) Uso de OR
Crie um programa em Python que peça a idade de uma pessoa e se ela possui autorização dos responsáveis (responda com "sim" ou "não"). O programa deve permitir a entrada no evento caso a pessoa tenha 18 anos ou mais ou tenha autorização. Caso contrário, deve informar que a entrada não é permitida.

2) Uso de OR
Crie um programa que receba a nota final de um aluno e sua frequência (em porcentagem). O aluno será considerado aprovado se tiver nota maior ou igual a 7 ou frequência maior ou igual a 75%. Caso contrário, deverá ser reprovado. O programa deve exibir uma mensagem informando a situação do aluno.

3) Uso de AND
Crie um programa que peça o nome de usuário e a senha. O sistema deve permitir o acesso apenas se o usuário for "admin" e a senha for "1234". Caso contrário, deve exibir uma mensagem de acesso negado.

4) Uso de AND
Crie um programa que receba o salário de um funcionário e seu tempo de empresa (em anos). O funcionário receberá um bônus apenas se tiver salário menor que 3000 e tempo de empresa maior ou igual a 2 anos. Caso contrário, não receberá bônus. O programa deve exibir uma mensagem informando se o bônus foi concedido ou não.
"""

#1
age = int(input("Digite a sua idade: "))
authorization = input("Voce tem autorizacao? Digite S- sim ou N- nao ").upper()

if age >= 18 or authorization == "S":
    print("Voce tem autorizacao p entrar")
else:
    print("Voce nao tem autorizacao p entrar")

#2
final_note = float(input("Digite a sua nota final: "))
fault_frequency = int(input("Digite a sua frequencia de falta: "))

if final_note >= 7 or fault_frequency >= 75:
    print("Voce esta aprovado")
else:
    print("Voce esta reprovado")

#3
name = input("Digite seu nome: ")
password = input("Digite a sua senha: ")

if name == "admin" and password =="1234":
    print("Acesso permitido")
else:
    print("acesso negado!")

#4
salary = float(input("Digite seu salario: "))
years = int(input("Digite o tempo de anos que trabalhou na empresa: "))

if salary < 3000 and years >= 2:
    print("Voce podera receber Bonus")
else:
    print("Voce nao podera receber o Bonus!")