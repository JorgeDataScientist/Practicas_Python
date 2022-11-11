# Escribe un programa que determine si un número dado es par o impar.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f'El numero {number} es Par')
else:
    print(f'El numero {number} es Impar')