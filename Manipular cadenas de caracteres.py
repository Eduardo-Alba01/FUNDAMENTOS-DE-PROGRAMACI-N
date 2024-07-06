def main():
    texto = input("Ingrese el texto: ")
    while True:
        print("Elige una opcion:")
        print("1.retornar todo el texto en mayusculas")
        print("2.retornar todo el texto en minusculas")
        print("3.retornar los dos primeros caracteres")
        print("4.retornar los dos ultimos caracteres")
        print("5.retornar la cantidad de veces que se repite el ultimo caracter")
        print("6.invertir el texto")
        print("7.salir")

        mayusculas = texto.upper()
        minusculas = texto.lower()
        retornar_2_primeros_char = texto[:2]
        dos_ultimos_char = texto[-2:]
        ultimo_char = texto[-1]
        repeticiones_ultimo = sum(1 for char in texto if char == ultimo_char)
        invertido = texto[::-1]

        opcion = input("Opcion: ")
        if opcion == "1":
            print(mayusculas)
        elif opcion == "2":
            print(minusculas)
        elif opcion == "3":
            print(retornar_2_primeros_char)
        elif opcion == "4":
            print(dos_ultimos_char)
        elif opcion == "5":
            print(repeticiones_ultimo)
        elif opcion == "6":
            print(invertido)
        elif opcion == '7':
            break
        else:
            print("Opcion no valida")
main()
      
