"""
1. Crie um programa em python que aponte a idade da pessoa e diga se ela é criança (0-12 anos), adolescente (13-17 anos), adulto jr (18-25), adulto (26-35), adulto sr (36-60), idoso (61+).

2.  Crie um programa em python que aponte o signo da pessoa referente ao dia e mês de nascimento.

"""

"""
Áries: 21 de março – 19 de abril
Touro: 20 de abril – 20 de maio
Gêmeos: 21 de maio – 20 de junho
Câncer: 21 de junho – 22 de julho
Leão: 23 de julho – 22 de agosto
Virgem: 23 de agosto – 22 de setembro
Libra: 23 de setembro – 22 de outubro
Escorpião: 23 de outubro – 21 de novembro
Sagitário: 22 de novembro – 21 de dezembro
Capricórnio: 22 de dezembro – 19 de janeiro
Aquário: 20 de janeiro – 18 de fevereiro
Peixes: 19 de fevereiro – 20 de março
"""

#1
age = int(input("👉 Digite a sua idade: "))

if age >= 0 and age <= 12:
    print("Voce é uma crianca.")
elif age >= 13 and age <= 17:
    print("Voce é adolescente.")
elif age >= 26 and age <= 35:
    print("Voce é uma adulto junior.")
elif age >= 36 and age <= 60:
    print("Voce é um adulto senior.")
else:  
    print("Voce é idoso.")

#2
day = int(input("Digite o dia: "))
month = int(input("Digite o mes (1-12): "))

# Validacao da data
if (month == 2 and day <= 28) or (month in (4, 6, 9, 11) and day <= 30) or (month in (1, 3, 5, 7, 8, 10, 12) and day <= 31):

    if (day >= 21 and month == 3) or (day <= 19 and month == 4):
        print("Você é signo de Áries")
    elif (day >= 20 and month == 4) or (day <= 20 and month == 5):
        print("Você é signo de Touro")
    elif (day >= 21 and month == 5) or (day <= 20 and month == 6):
        print("Você é signo de Gêmeos")
    elif (day >= 21 and month == 6) or (day <= 22 and month == 7):
        print("Você é signo de Câncer")
    elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
        print("Você é signo de Leão")
    elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
        print("Você é signo de Virgem")
    elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
        print("Você é signo de Libra")
    elif (day >= 23 and month == 10) or (day <= 21 and month == 11):
        print("Você é signo de Escorpião")
    elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
        print("Você é signo de Sagitário")
    elif (day >= 22 and month == 12) or (day <= 19 and month == 1):
        print("Você é signo de Capricórnio")
    elif (day >= 20 and month == 1) or (day <= 18 and month == 2):
        print("Você é signo de Aquário")
    elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
        print("Você é signo de Peixes")

else:
    print("Data inválida!")