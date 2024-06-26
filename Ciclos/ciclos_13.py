#13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
num = int(input("Ingresa un numero entero: "))
for i in range(1, num+1):
  if i %5 == 0:
    print(i)