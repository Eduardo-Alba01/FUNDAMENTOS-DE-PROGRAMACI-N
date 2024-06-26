#16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
promedio_2 = sum(i2 for i in range(1, x+1))/x
promedio_5 = sum(i5 for i in range(1, y+1))/y
if promedio_2 > promedio_5:
    print("El promedio de 2 es mayor")
else:
  print("El promedio de 5 es mayor")