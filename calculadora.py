print("🧮 Calculadora simples")

num1 = float(input("Digite o primeiro numero: "))
operacao = input("Escolha a operacao desejada (+, -, *, /, **, %): ")
num2 = float(input("digite o segundo numero: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "**":
    resultado = num1 ** num2
elif operacao == "%":
    resultado = num1 % num2
elif operacao == "/":
    while num2 == 0:
        print("Nao pode dividir por zero")
        num2 = float(input("Digite outro numero: "))
    resultado = num1 / num2

print(f"{num1} {operacao} {num2} =")
print(f"o resultado {resultado}")

#-----------------------------------------------------------------------
# print("🧮 Calculadora simples")

# num1 = float(input("Digite o primeiro numero: "))
# operacao = input("Escolha a operacao desejada (+, -, *, /): ")
# num2 = float(input("digite o segundo numero: "))

# match operacao:
#     case "+":
#         resultado = num1 + num2
#     case "-":
#         resultado = num1 - num2
#     case "*":
#         resultado = num1 * num2
#     case "/":
#         while num2 == 0:
#             print("Nao pode dividir por zero")
#             num2 = float(input("Digite outro numero: "))
#         resultado = num1 / num2

# print(f"{num1} {operacao} {num2} =")
# print(f"o resultado {resultado}")