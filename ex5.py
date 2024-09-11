'''
1. Escreva um programa que solicite ao usuário o valor de um produto e exiba na tela as seguintes opções de pagamento:

    1 – Pagamento a vista (5% desconto)
    2 – Pagamento cartão de crédito em 5 parcelas iguais
    3 – Pagamento cartão de crédito em 8 parcelas iguais (acréscimo de 10% no valor total do produto)
    4 – Pagamento cartão de crédito em 12 parcelas iguais (acréscimo de 20% no valor total do produto)

Em seguida, pergunte qual a opção de pagamento, calcule e exiba o (s) valor (es) a ser (em) pago (s).
'''

valor = float(input("Informe o valor do produto: "))

print("[1] – Pagamento a vista (5% desconto)")
print("[2] – Pagamento cartão de crédito em 5 parcelas iguais")
print("[3] – Pagamento cartão de crédito em 8 parcelas iguais (acréscimo de 10% no valor total do produto)")
print("[4] – Pagamento cartão de crédito em 12 parcelas iguais (acréscimo de 20% no valor total do produto)")
opcao = int(input("Escolha a forma de pagamento [1-4]: "))

match opcao:
    case 1:
        print(f"O preço será de R${valor - valor * 0.05}")
    case 2:
        print(f"O preço será de R${valor} em 5 parcelas de R${valor/5}")
    case 3:
        print(f"O preço será de R${valor + valor * 0.1} em 8 parcelas de R${(valor + valor * 0.1)/8}")
    case 4:
        print(f"O preço será de R${valor + valor * 0.2} em 12 parcelas de R${(valor + valor * 0.2)/12}")