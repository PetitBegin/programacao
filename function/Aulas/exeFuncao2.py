#implementar uma função que se chama tamanho text

def tamanho(texto: str ) -> int :
    contador = 0 
    for _ in texto:
    contador +=1
    return contador

print (
    tamanho("Bem vindo!"))
