from datetime import date
data_atual = date.today()
ano_atual = int('{}'.format(data_atual.year))
print (type( ano_atual))
ano = int(input())
print(int(ano.isdigit()))