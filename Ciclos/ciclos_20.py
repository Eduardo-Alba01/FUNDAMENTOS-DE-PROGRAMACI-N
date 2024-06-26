#20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

num = int(input("Ingresa un numero entero: "))
suma_factoriales = sum(factorial(i) for i in range(1, num+1))
print(f"La suma de los factoriales es: {suma_factoriales}")