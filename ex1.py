'''
1. Desenvolva um programa para calcular a média final:

Solicite ao usuário as notas AP1, AP2 e AP3;

Calcule a média final, sabendo que a primeira nota tem peso 4, a segunda peso 4 e terceira peso 2.

Exiba a média final na tela.

- Se a média final for maior igual a 7 exiba "aprovado";
- Se a média final estiver entre 6 e 7 exiba "substitutiva";
- Se a média final estiver entre 3 e 6 exiba "exame";
- Se a média final abaixo de 3, exiba "reprovado".
'''

AP1 = int(input("Informe a nota da AP1: "))
AP2 = int(input("Informe a nota da AP2: "))
AP3 = int(input("Informe a nota da AP3: "))

media = (AP1 / 10 * 4) + (AP2 / 10 * 4) + (AP3 / 10 * 2)

if (media < 0 or media > 10):
    print("Inválido")
elif (media >= 7):
    print(f"Aprovado com a média {media}")
elif (media >= 6):
    print(f"Substitutiva com a média {media}")
elif (media >= 3):
    print(f"Exame com a média {media}")
else:
    print(f"Reprovado com a média {media}")