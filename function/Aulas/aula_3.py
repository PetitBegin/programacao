"""Construa um programa que :
Pergunte ao usuário qual seu peso?
Informe ao usuário qual o indice de Massa Corporal?(IMC)
DICAS:
O IMC é igual ao peso dividido pelo quadrado da altura.
Para fazer divisão em Python, use o sinal/ (ex: 10/5)
Para fazer multiplicação em Python, use o sinal* (ex: 10*5)"""

peso= float( input("digite seu qual seu peso?"))
altura= float(input("qual a sua altura?"))
imc= peso / (altura*altura)
print(f"seu imc: {imc:.2f}")

