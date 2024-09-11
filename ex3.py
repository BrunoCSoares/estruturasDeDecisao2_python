'''
3. Desenvolva um programa que recebe o peso e a altura do usuário. Calcule o IMC sabendo que a fórmula do IMC é o peso dividido pela altura ao quadrado. Apresente na tela o valor do IMC e a classificação de acordo com a tabela abaixo:

| **IMC** | **Classificação** | **Recomendações** |
| --- | --- | --- |
| Abaixo de 18,5 | Abaixo do peso | Procure orientação médica |
| Entre 18,5 e 24,9 | Peso ideal | Parabéns, mante-se assim |
| Entre 25 e 29,9 | Levemente acima do peso | Fique alerta com seu peso: Pratique esportes e cuide se sua alimentação |
| Entre 30 e 34,9 | Obesidade grau I | Fique atento com sua saúde |
| Entre 35 e 39,9 | Obesidade grau II (severa) | Procure orientação médica |
| Acima de 40 | Obesidade grau III (mórbida) | Procure orientação médica |
'''

peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso / altura ** 2

if (imc < 18.5):
    print("Abaixo do peso | Procure orientação médica")
elif (imc < 25):
    print("Peso ideal | Parabéns, mantenha assim")
elif (imc < 30):
    print("Levemente acima do peso | Fique alerta com seu peso: Pratique esportes e cuide se sua alimentação")
elif (imc < 35):
    print("Obesidade grau I | Fique atento com sua saúde")
elif (imc < 40):
    print("Obesidade grau II (severa) | Procure orientação médica")
else:
    print("Obesidade grau III (mórbida) | Procure orientação médica")