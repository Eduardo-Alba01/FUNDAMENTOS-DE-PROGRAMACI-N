#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.
num = int(input("Ingrese un numero entero: "))
suma = sum(range(1, num+1))
print(f"La suma es: {suma}")