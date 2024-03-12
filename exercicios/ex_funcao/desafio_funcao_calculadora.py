def calcula(num1, num2, operador):
    if (operador == "+"):
        return num1 + num2
    
    elif(operador == "-"):
        return num1 - num2
    
    elif(operador == "*"):
        return num1 * num2
    
    elif(operador == "/"):
        return num1 / num2
    
    else:
        print("Operador não reconhecido. Fim do programa")


print("O resultado do calculo de adição: ", calcula(10,5,"+"))
print("O resultado do calculo de subtração: ",calcula(10,5,"-"))
print("O resultado do calculo de multiplicação: ", calcula(10,5,"*"))
print("O resultado do calculo de divisão: ", calcula(10,5,"/"))