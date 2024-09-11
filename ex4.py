'''
4. Escreva um programa que solicite ao usuário o nome e salário bruto de um funcionário. A seguir, calcule o valor do desconto do INSS com base na tabela abaixo:

Alíquota INSS 2021
Salário de contribuição | Alíquotas
Até R$1.100,00 | 7,50
De R$1.100,01 até R$2.203,48 | 9,00
De R$2.203,49 até R$3.305,22 | 12,00
De R$3.305,23 até R$6433,57 | 14,00

OBS: A partir de R$ 6433,5 o desconto é fixo no valor de R$ 751,99 (teto)
'''

nome = input("Informe o nome do funcionário: ")
salarioBruto = float(input("Informe o salário bruto do funcionário: "))

if (salarioBruto <= 1100):
    desconto = salarioBruto/100 * 7.5
    print(f"O desconto de {nome} será de R${desconto}")
elif (salarioBruto < 2203.49):
    desconto = salarioBruto/100 * 9
    print(f"O desconto de {nome} será de R${desconto}")
elif (salarioBruto < 3305.23):
    desconto = salarioBruto/100 * 12
    print(f"O desconto de {nome} será de R${desconto}")
elif (salarioBruto < 6433.58):
    desconto = salarioBruto/100 * 14
    print(f"O desconto de {nome} será de R${desconto}")
else:
    print(f"O desconto de {nome} será de R$751,99")
