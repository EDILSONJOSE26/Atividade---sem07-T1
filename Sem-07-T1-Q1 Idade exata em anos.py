dia = int(input())
mes = int(input())
ano = int(input())

data_nas = int(input())
mes_nas = int(input())
ano_nas = int(input())
x = ano - ano_nas

if mes < mes_nas or dia < data_nas:
    x -=1
    print(x)
else:
    print(x)
