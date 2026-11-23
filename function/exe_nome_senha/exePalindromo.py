# fazer uma função para a palavra ficar de trás pra frente
#osso ana 
texto = input("Digite uma frase:")

def palindromo(texto: str) ->bool:
    #return texto == inverter(texto)
    invertido = ""
    for i in range(len(texto)-1, -1, -1):
        invertido+= texto[i]
    if texto == invertido:
       return True
    else:
        return False

print(palindromo(texto)) 

