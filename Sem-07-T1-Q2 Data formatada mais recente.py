dia = int(input())
mes = int(input())
ano = int(input())
q_dia = int(input())
q_mes = int(input())
q_ano = int(input())

if dia > q_dia or mes > q_mes or ano > q_ano:
    print("{}/{}/{}".format(dia,mes,ano))
else:
    print("{}/{}/{}".format(q_dia,q_mes,q_ano))
