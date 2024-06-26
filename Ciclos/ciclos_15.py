#15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
suma = sum(i*3 for i in range(1, 20+1))
print(f"la suma es {suma}")