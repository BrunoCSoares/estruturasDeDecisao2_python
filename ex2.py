'''
1. Uma livraria resolveu fazer uma promoção, com os seguintes critérios:
- Livros com preços até R$ 10,00 - desconto de 8%
- Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%
- Livros com preços acima de R$ 60,00 - desconto de 20%

Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto oferecido, em reais.
'''

valorLivro = float(input("Digite o valor do livro desejado: "))

if (valorLivro < 0):
    print("Inválido")
elif (valorLivro <= 10):
    print("O desconto será de 8%")
elif (valorLivro <= 60):
    print("O desconto será de 10%")
else:
    print("O desconto será de 20%")