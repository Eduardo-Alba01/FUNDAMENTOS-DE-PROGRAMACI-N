#17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5
numeros = []
while True:
    num = int(input("Ingresa un numero (0 para terminar): "))
    if num == 0:
        break
    if num %10 == 5:
        numeros.append(num)
if numeros:
    print("Los numeros terminados en 5 son:")
    for num in numeros:
        promedio = sum(numeros)/len(numeros)
        print(f"El promedio de los numeros terminados en 5 es: {promedio}")
    else:
        print("No se ingresaron numeros terminados en 5.")