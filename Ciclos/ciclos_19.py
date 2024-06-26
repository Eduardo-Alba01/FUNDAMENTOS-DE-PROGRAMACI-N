#19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
num = int(input("Ingresa un numero entero: "))
for i in range(1, 10+1):
    print(f"{num} x {i} = {num*i}")