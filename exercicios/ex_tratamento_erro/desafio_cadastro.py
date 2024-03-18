# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
import datetime
agora = datetime.datetime.now()
idade = 0

ano_atual = agora.year
casoCerto = False
print("Cadastro")
print("Digite o seu nome completo :")
nome_completo = input()

while (casoCerto== False):
    ano_nascimento = input("Digite o ano da sua data de nascimento: ")

    if ano_nascimento.isdigit():
            casoCerto = True
            idade = ano_atual - int(ano_nascimento)
            print("O usuário ", nome_completo, " sua idade é", idade)
    else:
        try:
            ano_nascimento = int(ano_nascimento)
            idade = ano_atual - ano_nascimento
            print("O usuário ", nome_completo, " sua idade é", idade)
            casoCerto = True

        except Exception as err:
            print("Ocorreu um erro")
            print("o o usuário não digite um número o inseriu um valor inválido no campo do ano")
            print(err)
        