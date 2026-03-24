"""
Crie um programa em Python que peça ao usuário a idade. Em seguida, o programa deve informar a situação da idade do usuário, idade maior ou igual a 18, deve imprimir que ele é adulto, idade maior ou igual a 12 deve imprimir que ele é adolescente, qualquer idade menor que 12 deve imprimir que é uma criança. Para resolver o exercício, utilize as estruturas condicionais if, elif e else.
"""

age = int(input("👉 Digite a sua idade: "))

if age >= 18:
    print("Voce é adulto 👨")
elif age < 18 and age >= 12:
    print("Voce é adolescente 🧒")
else:
    print("Voce é uma crianca 👶")
