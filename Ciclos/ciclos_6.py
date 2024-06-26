#6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos
num = input("Ingrese un numero entero de tres digitos: ")
for digit in num:
    for i in range(1, int(digit)+1):
        print(digit)

