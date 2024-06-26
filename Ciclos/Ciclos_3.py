#3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído
num = int(input("Ingresa un numero entero: "))
for i in range(1, num + 1):
    if num %i == 0:
        print(i)