def calculadora(num1, num2, operacao):
    if(operacao == 1):
        return num1 + num2
    elif(operacao == 2):
        return num1 - num2
    elif(operacao == 3):
        return num1 * num2
    elif(operacao == 4) and (num2 != 0):
        return num1 / num2
    else:
        res = "erro"
        return res
    
res = calculadora(2, 0, 4)

if( res == "erro"):
    print("Ocorreu um erro")

else:
    print(res)