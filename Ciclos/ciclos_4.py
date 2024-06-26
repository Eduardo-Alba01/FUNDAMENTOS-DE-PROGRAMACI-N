#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.
num_1 = int(input("Ingresa el primer numero entero: "))
num_2 = int(input("Ingresa el segundo numero entero: "))
for i in range(num_1, num_2 + 1):
    print(i)