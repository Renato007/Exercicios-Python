# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
from datetime import date
data_atual = date.today()
ano_atual = '{}'.format(data_atual.year)

valorCorreto = False

print("Cadastro")

print("Digite o seu nome completo :")
nome_completo = input()

while valorCorreto ==False:
    print("informe o ano de nascimento")
    try:
        ano = str(input())
        if (ano.isdigit()== ano_atual):
            raise Exception("Por favor digite um valor númerico, ano da data do nascimento")
        elif(ano < 1992) or (ano > data_atual):
            raise Exception("Por favor digite um valor númerico entre 1922 e 2021")
        else: 
           valorCorreto = True
           idade_atual = ano_atual-ano
           print("Sua idade e saida", idade_atual)
    except Exception as erro:
        print(erro)
