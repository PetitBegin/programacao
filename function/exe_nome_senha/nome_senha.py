# nome
# senha
# confirmar senha

#login e validar senha
#login -> nome.sobrenome
#8 caracteres
#1 M
#1 m
#1 @
#1 digito
# senha e confirmação de senha tem ser ==
def dados_usuario() -> bool:
    nome: str = input("Digite seu nome completo:")
    print("Sua senha deve ter ao menos um item de cada um dos  listados abaixo e possuir no total 8 caractéres:\n\n" 

        "*uma letra maiúscula,: \n"
        " *uma letra minúscula,:\n"
        "*um número,\n"
        "*um caracter especial,:\n"
        "*um dígito. \n" 
        )
    senha: str = input("Digite sua senha:")
    confirmacao_de_senha: str = input("Confirme sua senha:")
    if confirmacao_de_senha == senha:

       MINUSCULAS: str = "abcdefghijklmnopqrstuvwxyz"
       MAIUSCULAS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       DIGITOS: str = "0123456789"
       CARACTERES_ESPECIAIS: str = "!#$%¨&*()_+=§"

    if len(senha) >= 8 :
        possui_MINUSCULAS = False
        possui_MAIUSCULAS = False
        possui_DIGITOS = False
        possui_CARACTERES_ESPECIAIS = False
        return True

        return True
    def inverter(texto: str):
        resposta: str = ""
        for i in range(len(texto)-1, -1, -1):
            resposta+=texto[i]
            return resposta

       
print("Senhas compatíveis ✅")
   

    

