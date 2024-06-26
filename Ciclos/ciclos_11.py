#11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.
num = input("Ingrese un numero entero de dos digitos: ")
digit1, digit2 = int(num[0]),int(num[1])
for i in range(digit1,digit2+1):
    print(i)