# Aula 1 - Introdução ao Python
# Comentário de linha única é feito com o símbolo #
"""
Comentários de múltiplas linhas são feitos com aspas triplas

palavras reservadas no python
False     await     else      import     pass
None      break     except    in         raise
True      class     finally   is         return
and       continue  for       lambda     try
as        def       from      nonlocal   while
assert    del       global    not        with
async     elif      if        or         yield
"""

# A variável é um espaço na memória para armazenar um valor
nome = "Henrique"
print(nome)

nome = "Thais"
nome = "Lais"
nome = "Jessica"
print(nome)
# Variáveis podem armazenar diferentes tipos de dados
idade = 25  # Variável do tipo inteiro
altura = 1.75  # Variável do tipo float
print(f"{idade} anos e {altura} de altura")
# print é uma função que exibe o valor na tela
# Podemos realizar operações matemáticas com variáveis numéricas ou concatenar strings

# Operações matemáticas
soma = 10 + 5
divisao = 10 / 2
subtracao = 10 - 3
multiplicacao = 10 * 4
expoente = 2**3
resto = 10 % 3

# operações com strings
nome_completo = nome + " Silva"  # Concatenando strings

# Operadores de comparação
print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 10)  # True
print(10 != 5)  # True
print(10 >= 10)  # True
print(10 <= 5)  # False


# Aula 1 - introducao ao Python
# import random

# numero_secreto = random.randint(1, 100)
# tentativas = 0

# print("🎯 Jogo de Adivinhação")
# print("Tente adivinhar o número entre 1 e 100!")

# while True:
#     palpite = int(input("Digite seu palpite: "))
#     tentativas += 1

#     if palpite < numero_secreto:
#         print("🔼 O número é MAIOR!")
#     elif palpite > numero_secreto:
#         print("🔽 O número é MENOR!")
#     else:
#         print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
#         break

# import random

# numero_secreto = random.randint(1, 100)
# tentativas = 0
# max_tentativas = 5

# print("🎯 Jogo de Adivinhação")
# print("Você tem apenas 5 tentativas para acertar o número (1 a 100)!")

# while tentativas < max_tentativas:
#     palpite = int(input(f"Tentativa {tentativas + 1}: "))

#     tentativas += 1

#     if palpite < numero_secreto:
#         print("🔼 O número é MAIOR!")
#     elif palpite > numero_secreto:
#         print("🔽 O número é MENOR!")
#     else:
#         print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
#         break
# else:
#     print(f"💀 Fim de jogo! O número era {numero_secreto}")
