"""
1. Faça um programa que peça dois números ao usuário e mostre qual o menor número.

2. Faça um programa que receba um número inteiro e diga se ele é par ou ímpar.

3. Faça um programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (casado), "S" (solteiro), "D" (divorciado), "V" (viúvo), ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil. Exemplo:
Usuário digita: C
Seu programa deve responder:
C - Casado
"""

# 1️⃣
num1 = int(input("👉 Digite primeiro numero: "))
num2 = int(input("👉 Digite segunfo numero: "))

if num1 > num2:
    print(f"🔢 o menor numero é o segundo numero {num2}")
elif num1 < num2:
    print(f"🔢 o menor numero é o primeiro numero {num1}")
else:
    print("Os dois numeros digitados sao iguais")


# 2️⃣
num = int(input("👉 Digite um numero: "))

if num % 2 == 1:
    print("O numero é impar")
else:
     print("O numero é par")


# # 3️⃣
# estadoCivil = input("👉 Digite seu estado civil: C- casado(a), S- solteiro(a), D- divorciado, V- viuvo, O- outros:  ")

# if (estadoCivil == "c") or (estadoCivil == "C"):
#     print("C - Casado(a)")
# elif (estadoCivil == "s") or (estadoCivil == "S"):
#     print("S - Solteiro(a)")
# elif (estadoCivil == "d") or (estadoCivil == "D"):
#     print("D - Divorciado(a)")
# elif (estadoCivil == "v") or (estadoCivil == "V"):
#     print("V - Viuvo(a)")
# elif (estadoCivil == "o") or (estadoCivil == "O"):
#     print("O - Outros")
# else:
#     print("Opcao invalida!")

estadoCivil = input("👉 Digite seu estado civil: C- casado(a), S- solteiro(a), D- divorciado, V- viuvo, O- outros:  ").upper()

if (estadoCivil == "C"):
    print("C - Casado(a)")
elif (estadoCivil == "S"):
    print("S - Solteiro(a)")
elif (estadoCivil == "D"):
    print("D - Divorciado(a)")
elif (estadoCivil == "V"):
    print("V - Viuvo(a)")
elif (estadoCivil == "O"):
    print("O - Outros")
else:
    print("Opcao invalida!")