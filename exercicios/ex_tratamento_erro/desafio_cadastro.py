# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
valorCorreto = False

print("Cadastro")

print("Digite o seu nome completo :")
nome_completo = input()

while valorCorreto ==False:
    print("informe o ano ")
    try:
        ano = input()
        if(ano < 0) or (ano.isdigit()== False):
             raise Exception("Não digitou valor númerico positivo")
        else: 
            idade =            
            print()

falta concluir