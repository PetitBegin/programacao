"""Escreva um programa que converta um número de minutos em horas e
minutos. O programa deve pedir ao usuário para inserir a quantidade de
minutos e, em seguida, exibir o equivalente em horas e minutos."""

minutos = int(input("Digite a quantidade de mimutos"))
horas = minutos //60
resto = minutos%60
print("Seu resultado é:", horas, "horas e", resto ,"minutos")