def calculadora(num1, num2, operacao):
    if(operacao == 1):
        res = num1 + num2
    elif(operacao == 2):
        res = num1 - num2
    elif(operacao == 3):
        res = num1 * num2
    elif(operacao == 4):
        if (num2 != 0):
            res = num1 / num2
        else:
            raise Exception("Divisão por zero não é possivel")
    else:
        raise Exception("operação não existe")
    return res

try:
    res = calculadora(2,"u",1)
    print(res)

except Exception as err:
    print("Ocorreu um erro")
    print(err)