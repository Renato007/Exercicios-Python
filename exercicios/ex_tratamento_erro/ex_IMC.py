def calcular_imc(peso, altura):
    if(peso< 0) or (altura < 0):
        raise Exception ("Valores preenchidos incorretamente")
    imc = (peso) / (altura * altura)

    return imc


print("Programa IMC")
rodar = True

while(rodar):
    try:
        print("Digite o seu peso")
        peso = float(input())

        print("Digite o seu tamanho")
        tamanho = float(input())

        imc = calcular_imc(peso, tamanho)

        print(imc)

        rodar =False
    except:
        print("Dados incorretos")
print("Finalizando programa")