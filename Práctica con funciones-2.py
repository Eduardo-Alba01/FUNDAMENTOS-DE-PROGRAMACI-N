def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido a la Práctica con funciones 2"

def suma(a, b):
    return a + b

def area_rectangulo(largo, ancho):
    return largo * ancho

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def maximo_de_tres(a, b, c):
    return max(a, b, c)

def es_palindromo(palabra):
    return palabra == palabra[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def menu():
    print("-------------------")
    print("Menú de opciones:")
    print("-------------------")
    print("1. Suma")
    print("2. Área de un Rectángulo")
    print("3. Número Par o Impar")
    print("4. Conversión de Grados Celsius a Fahrenheit")
    print("5. Máximo de Tres Números")
    print("6. Palíndromo")
    print("7. Factorial")
    print("8. Contar Vocales")
    print("9. Números Primos")
    print("10. Salir")
    print("-------------------")

def main():
    nombre = input("¿Cuál es tu nombre? ")
    if not nombre.strip():
        print("Nombre no válido. Saliendo...")
        return
    print(saludo(nombre))
    
    while True:
        menu()
        opcion = input("Elige una opción (1-10): ")
        
        match opcion:
            case '1':
                try:
                    a = float(input("Ingresa el primer número: "))
                    b = float(input("Ingresa el segundo número: "))
                    print("Suma:", suma(a, b))
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa números válidos.")
            
            case '2':
                try:
                    largo = float(input("Ingresa el largo del rectángulo: "))
                    ancho = float(input("Ingresa el ancho del rectángulo: "))
                    print("Área del rectángulo:", area_rectangulo(largo, ancho))
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa números válidos.")
            
            case '3':
                try:
                    numero = int(input("Ingresa un número: "))
                    print(f"El número {numero} es:", es_par_o_impar(numero))
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")
            
            case '4':
                try:
                    celsius = float(input("Ingresa los grados Celsius: "))
                    print(f"{celsius} grados Celsius son {celsius_a_fahrenheit(celsius)} grados Fahrenheit")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número válido.")
            
            case '5':
                try:
                    a = float(input("Ingresa el primer número: "))
                    b = float(input("Ingresa el segundo número: "))
                    c = float(input("Ingresa el tercer número: "))
                    print("El mayor de los tres números es:", maximo_de_tres(a, b, c))
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa números válidos.")
            
            case '6':
                palabra = input("Ingresa una palabra: ")
                if palabra.strip():
                    if es_palindromo(palabra):
                        print(f"La palabra '{palabra}' es un palíndromo.")
                    else:
                        print(f"La palabra '{palabra}' no es un palíndromo.")
                else:
                    print("Entrada inválida. Por favor, ingresa una palabra válida.")
            
            case '7':
                try:
                    n = int(input("Ingresa un número: "))
                    print(f"El factorial de {n} es {factorial(n)}")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")
            
            case '8':
                cadena = input("Ingresa una cadena de texto: ")
                if cadena.strip():
                    print(f"La cadena '{cadena}' tiene {contar_vocales(cadena)} vocales")
                else:
                    print("Entrada inválida. Por favor, ingresa una cadena de texto válida.")
            
            case '9':
                try:
                    numero = int(input("Ingresa un número: "))
                    if es_primo(numero):
                        print(f"El número {numero} es primo.")
                    else:
                        print(f"El número {numero} no es primo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")
            
            case '10':
                print("Saliendo...")
                break
            
            case _:
                print("Opción no válida, por favor elige una opción del 1 al 10.")
        
        print()  # Imprimir una línea en blanco para separar las ejecuciones

if __name__ == "__main__":
    main()
