'''
6. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Morango | R$2,50 por kg até 5kg | R$2,20 por kg acima de 5kg
Maçã | R$1,80 por kg até 5kg | R$1,50 por kg acima de 5kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

pesoMog = float(input("Informe o peso de morangos em quilos: "))
pesoMac = float(input("Informe o peso de maçãs em quilos: "))

if (pesoMog > 5):
    precoMog = pesoMog * 2.2
else:
    precoMog = pesoMog * 2.5

if (pesoMac > 5):
    precoMac = pesoMac * 1.5
else:
    precoMac = pesoMac * 1.8

if (((pesoMog * pesoMac) > 8) or ((precoMog + precoMac) > 25)):
    precoTot = (precoMog + precoMac) * 0.9
    print("O total da conta será R$", precoTot)
else:
    precoTot = (precoMog + precoMac)
    print("O total da conta será R$", precoTot)
