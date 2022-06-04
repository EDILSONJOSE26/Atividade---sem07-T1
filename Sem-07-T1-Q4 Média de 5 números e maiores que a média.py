num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
num_5 = int(input())

soma = num_1 + num_2 + num_3 + num_4 + num_5

media = soma/5

result = float("{:.2f}".format(media))

print(result)

if num_1 > media:
    print(float("{:.2f}".format(num_1)))         
if num_2 > media:        
    print(float("{:.2f}".format(num_2)))
if num_3 > media:
    print(float("{:.2f}".format(num_3)))
if num_4 > media:
    print(float("{:.2f}".format(num_4)))
if num_5 > media:
    print(float("{:.2f}".format(num_5)))
