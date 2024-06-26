#5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.
num_1 = int(input("Ingresa el primer numero entero: "))
num_2 = int(input("Ingresa el segundo numero entero: "))
for i in range(num_1, num_2 + 1):
    if i % 10 == 4:
        print(i)