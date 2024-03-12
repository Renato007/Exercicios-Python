
opcao = 1

def calcula(num1, num2, operador):
    if (operador == 1):
        return num1 + num2
    
    elif(operador == 2):
        return num1 - num2
    
    elif(operador == 3):
        return num1 * num2
    
    elif(operador == 4):
        return num1 / num2
    
    else:
        return "Operador não reconhecida. Fim do programa"

while(opcao != 0):
    print("calculadora com operação de dois números")
    print("digite o numero 01 : ")
    num1 = int(input())
    print("digite o numero 02 : ")
    num2 = int(input())

    print("Escolha a operação:")
    print("1 - adiçãosubtração")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão ")

    print("Aguardando digitar : ")
    operacao = int(input())
    print("resultado :" + str(calcula(num1, num2, operacao)))
    print("Desejá sair digite tecla  0." )
    print("Desejá continuar digite tecla  1" )
    opcao = int(input())
print("Final do programa")




