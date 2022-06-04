peso = float(input())
altura = float(input())

imc = int(peso / (altura ** 2))

if imc < 18.5:
    print(f"{imc}")
    print('Abaixo do peso')

elif 18.5 <= imc < 25:
    print(f"{imc}")
    print('Peso normal')

elif 25 <= imc < 30:
    print(f"{imc}")
    print('Sobrepeso')

elif 30 <= imc < 35:
    print(f"{imc}")
    print('Obeso leve')

elif 35 <= imc < 40:
    print(f"{imc}")
    print('Obeso moderado')

elif imc >= 40:
    print(f"{imc}")
    print('Obeso mórbido')
    
