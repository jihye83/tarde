"""
Crie um programa em Python que peça ao usuário quatro notas, calcule a média dessas notas e mostre o resultado na tela. Em seguida, o programa deve informar a situação do aluno com base na média: se for maior ou igual a 7, o aluno está aprovado; se for maior ou igual a 5 e menor que 7, está em recuperação; e se for menor que 5, está reprovado. Para resolver o exercício, utilize as estruturas condicionais if, elif e else
"""
print("📝 Nota da prova")

nota1 = float(input("digite primeira nota: "))
nota2 = float(input("digite segunda nota: "))
nota3 = float(input("digite terceira nota: "))
nota4 = float(input("digite quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and media <= 10:
    print("Voce esta aprovado")
elif media >= 5 and media < 7:
    print("voce esta em recuperacao")
elif media < 5:
    print("Voce esta reprovado")
# else:
#     print("erro na nota")

print(f"Média do aluno: {media}")
