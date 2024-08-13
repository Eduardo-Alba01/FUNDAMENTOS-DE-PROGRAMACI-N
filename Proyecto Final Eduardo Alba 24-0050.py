import os
import calendar
import time
from tkinter import filedialog
from datetime import datetime
import csv

# Lista para almacenar las tareas y el historial
tareas = []
historial_tareas = []

#limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# colores
def colorear_texto(texto, color):
    colores = {
        "reset": "\033[0m",
        "negro": "\033[30m",
        "rojo": "\033[31m",
        "verde": "\033[32m",
        "amarillo": "\033[33m",
        "azul": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "blanco": "\033[37m"
    }
    return f"{colores[color]}{texto}{colores['reset']}"

# Función para validar fecha
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Función para validar prioridad
def validar_prioridad(prioridad):
    return prioridad in ["baja", "media", "alta"]

# Función para validar categoría
def validar_categoria(categoria):
    return categoria.strip() != ""

# Función para validar hora
def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False

# Función para validar archivo de texto
def validar_archivo(nombre_archivo):
    return nombre_archivo.endswith(".txt")

# Función para mostrar el menú principal
def mostrar_menu():
    print(colorear_texto("\nSistema de Gestión de Tareas", "azul"))
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Listar tareas")
    print("4. Marcar tarea como completada")
    print("5. Editar tarea")
    print("6. Filtrar tareas")
    print("7. Buscar tarea")
    print("8. Mostrar calendario")
    print("9. Mostrar historial de tareas completadas")
    print("10. Mostrar ayuda")
    print("11. Exportar tareas")
    print("12. Importar tareas")
    print("13. Temporizador")
    print("14. Salir")

# agregar tarea
def agregar_tarea():
    limpiar_pantalla()
    while True:
        try:
            titulo = input("Escribe el título de la nueva tarea: ").strip()
            if not titulo:
                print(colorear_texto("El título no puede estar vacío.", "rojo"))
                continue

            while True:
                try:
                    dia = int(input("Escribe el día de la fecha límite (DD): ").strip())
                    mes = int(input("Escribe el mes de la fecha límite (MM): ").strip())
                    ano = int(input("Escribe el año de la fecha límite (YYYY): ").strip())
                    fecha = f"{ano}-{mes:02d}-{dia:02d}"
                    if validar_fecha(fecha):
                        fecha_limite = datetime.strptime(fecha, "%Y-%m-%d").date()
                        break
                    else:
                        print(colorear_texto("Fecha inválida. Usa un día, mes y año válidos.", "rojo"))
                except ValueError:
                    print(colorear_texto("Entrada inválida. Debe ser un número para el día, mes y año.", "rojo"))

            while True:
                prioridad = input("Escribe la prioridad (baja, media, alta): ").strip().lower()
                if validar_prioridad(prioridad):
                    break
                else:
                    print(colorear_texto("Prioridad inválida. Debe ser 'baja', 'media' o 'alta'.", "rojo"))

            while True:
                categoria = input("Escribe la categoría de la tarea: ").strip()
                if validar_categoria(categoria):
                    break
                else:
                    print(colorear_texto("La categoría no puede estar vacía.", "rojo"))

            while True:
                hora = input("Escribe la hora límite (HH:MM) o deja en blanco si no aplica: ").strip()
                if hora and not validar_hora(hora):
                    print(colorear_texto("Hora inválida. Usa el formato HH:MM.", "rojo"))
                else:
                    break
            tarea = {
                "titulo": titulo,
                "completada": False,
                "fecha_limite": fecha,
                "prioridad": prioridad,
                "categoria": categoria,
                "hora_limite": hora if hora else None
            }
            tareas.append(tarea)
            print(colorear_texto(f"Tarea '{titulo}' agregada en la categoría '{categoria}'.", "magenta"))
            break
        except ValueError:
            print(colorear_texto("Entrada inválida. Intenta de nuevo.", "rojo"))

        input("Presiona Enter para intentar de nuevo...")



# eliminar tarea
def eliminar_tarea():
    limpiar_pantalla()
    listar_tareas()
    while True:
        try:
            indice = input("Escribe el número de la tarea que deseas eliminar o 's' para salir: ").strip()
            if indice.lower() == 's':
                return
            indice = int(indice) - 1
            if 0 <= indice < len(tareas):
                tarea = tareas.pop(indice)
                print(colorear_texto(f"Tarea '{tarea['titulo']}' eliminada.", "magenta"))
                break
            else:
                print(colorear_texto("Índice inválido.", "rojo"))
        except ValueError:
            print(colorear_texto("Entrada inválida. Debe ser un número o 's' para salir.", "rojo"))

        input("Presiona Enter para intentar de nuevo...")

# listar tareas
def listar_tareas(filtro=None, valor=None):
    limpiar_pantalla()
    if not tareas:
        print("No hay tareas.")
    else:
        print("Lista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            if filtro and tarea[filtro] != valor:
                continue

            estado = colorear_texto("Completada", "verde") if tarea["completada"] else colorear_texto("Pendiente", "amarillo")
            prioridad = colorear_texto(tarea["prioridad"], "rojo" if tarea["prioridad"] == "alta" else "amarillo" if tarea["prioridad"] == "media" else "verde")
            print(f"{i}. {colorear_texto(tarea['titulo'], 'blanco')} - {estado} - Fecha límite: {tarea['fecha_limite']} - Prioridad: {prioridad}")

    input("Presiona Enter para regresar al menú principal...")

# marcar una tarea como completada
def marcar_completada():
    limpiar_pantalla()
    listar_tareas()
    while True:
        try:
            indice = input("Escribe el número de la tarea que deseas marcar como completada o 's' para salir: ").strip()
            if indice.lower() == 's':
                return
            indice = int(indice) - 1
            if 0 <= indice < len(tareas):
                tarea = tareas[indice]
                tarea["completada"] = True
                fecha_completada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                historial_tareas.append({"titulo": tarea["titulo"], "fecha_completada": fecha_completada})
                print(colorear_texto(f"Tarea '{tarea['titulo']}' marcada como completada.", "magenta"))
                break
            else:
                print(colorear_texto("Índice inválido.", "rojo"))
        except ValueError:
            print(colorear_texto("Entrada inválida. Debe ser un número o 's' para salir.", "rojo"))

        input("Presiona Enter para intentar de nuevo...")

# editar tarea
def editar_tarea():
    limpiar_pantalla()
    listar_tareas()
    while True:
        try:
            indice = input("Escribe el número de la tarea que deseas editar o 's' para salir: ").strip()
            if indice.lower() == 's':
                return
            indice = int(indice) - 1
            if 0 <= indice < len(tareas):
                tarea = tareas[indice]
                print(f"Editando tarea: {tarea['titulo']}")
                titulo = input(f"Nuevo título (deja en blanco para mantener '{tarea['titulo']}'): ").strip()
                fecha_limite = input(f"Nueva fecha límite (deja en blanco para mantener '{tarea['fecha_limite']}'): ").strip()
                if fecha_limite and not validar_fecha(fecha_limite):
                    print(colorear_texto("Fecha inválida. Usa el formato YYYY-MM-DD.", "rojo"))
                    continue
                prioridad = input(f"Nueva prioridad (deja en blanco para mantener '{tarea['prioridad']}'): ").strip().lower()
                if prioridad and not validar_prioridad(prioridad):
                    print(colorear_texto("Prioridad inválida. Debe ser 'baja', 'media' o 'alta'.", "rojo"))
                    continue
                categoria = input(f"Nueva categoría (deja en blanco para mantener '{tarea['categoria']}'): ").strip()
                if categoria and not validar_categoria(categoria):
                    print(colorear_texto("La categoría no puede estar vacía.", "rojo"))
                    continue
                hora_limite = input(f"Nueva hora límite (deja en blanco para mantener '{tarea.get('hora_limite', '')}'): ").strip()
                if hora_limite and not validar_hora(hora_limite):
                    print(colorear_texto("Hora inválida. Usa el formato HH:MM.", "rojo"))
                    continue

                if titulo:
                    tarea["titulo"] = titulo
                if fecha_limite:
                    tarea["fecha_limite"] = fecha_limite
                if prioridad:
                    tarea["prioridad"] = prioridad
                if categoria:
                    tarea["categoria"] = categoria
                if hora_limite:
                    tarea["hora_limite"] = hora_limite

                print(colorear_texto(f"Tarea '{tarea['titulo']}' actualizada.", "magenta"))
                break
            else:
                print(colorear_texto("Índice inválido.", "rojo"))
        except ValueError:
            print(colorear_texto("Entrada inválida. Debe ser un número o 's' para salir.", "rojo"))

        input("Presiona Enter para intentar de nuevo...")

# filtrar tareas
def filtrar_tareas():
    limpiar_pantalla()
    categorias = set(tarea["categoria"] for tarea in tareas)
    fechas = set(tarea["fecha_limite"] for tarea in tareas)

    print("Categorías disponibles:")
    for categoria in categorias:
        print(f"- {categoria}")

    print("\nFechas disponibles:")
    for fecha in fechas:
        print(f"- {fecha}")

    while True:
        filtro = input("\n¿Filtrar por '1' (fecha) o '2' (categoría)? ").strip()
        if filtro in ["1", "2"]:
            break
        else:
            print("Error: Opción de filtro no válida. Por favor, elige '1' (fecha) o '2' (categoría).")

    if filtro == "1":
        filtro_clave = "fecha_limite"
    elif filtro == "2":
        filtro_clave = "categoria"

    valor = input(f"Escribe el valor para el filtro '{filtro_clave}': ").strip()

    listar_tareas(filtro=filtro_clave, valor=valor)
    
# buscar tarea
def buscar_tarea():
    limpiar_pantalla()
    busqueda = input("Escribe el título o parte del título de la tarea a buscar: ").strip().lower()
    encontrado = False
    for i, tarea in enumerate(tareas, 1):
        if busqueda in tarea["titulo"].lower():
            estado = colorear_texto("Completada", "verde") if tarea["completada"] else colorear_texto("Pendiente", "amarillo")
            prioridad = colorear_texto(tarea["prioridad"], "rojo" if tarea["prioridad"] == "alta" else "amarillo" if tarea["prioridad"] == "media" else "verde")
            print(f"{i}. {colorear_texto(tarea['titulo'], 'blanco')} - {estado} - Fecha límite: {tarea['fecha_limite']} - Prioridad: {prioridad}")
            encontrado = True
    if not encontrado:
        print(colorear_texto("No se encontraron tareas con ese título.", "rojo"))

    input("Presiona Enter para regresar al menú principal...")

# mostrar el historial de tareas completadas
def mostrar_historial():
    limpiar_pantalla()
    if not historial_tareas:
        print("No hay historial de tareas completadas.")
    else:
        print("Historial de Tareas Completadas:")
        for tarea in historial_tareas:
            print(f"Título: {tarea['titulo']} - Fecha de completado: {tarea['fecha_completada']}")

    input("Presiona Enter para regresar al menú principal...")

# mostrar calendario
def mostrar_calendario(ano, mes):
    limpiar_pantalla()
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_str = cal.formatmonth(ano, mes)
    cal_lines = cal_str.split('\n')
    tareas_mes = [tarea for tarea in tareas if tarea["fecha_limite"].startswith(f"{ano}-{str(mes).zfill(2)}")]
    dias_con_tareas = {int(tarea["fecha_limite"].split('-')[2]) for tarea in tareas_mes}
    for i, line in enumerate(cal_lines):
        for dia in dias_con_tareas:
            dia_str = str(dia)
            if dia_str in line.split():
                cal_lines[i] = line.replace(dia_str, colorear_texto(f"{dia_str}*", "cyan"))
    cal_str = '\n'.join(cal_lines)

    print(cal_str)

# navegar por el calendario
def navegar_calendario():
    ano = datetime.now().year
    mes = datetime.now().month

    while True:
        mostrar_calendario(ano, mes)
        print("\nNavegar:")
        print("n - Mes siguiente")
        print("p - Mes anterior")
        print("s - Salir")

        opcion = input("Elige una opción: ").strip().lower()

        if opcion == "n":
            if mes == 12:
                mes = 1
                ano += 1
            else:
                mes += 1
        elif opcion == "p":
            if mes == 1:
                mes = 12
                ano -= 1
            else:
                mes -= 1
        elif opcion == "s":
            break
        else:
            print(colorear_texto("Opción inválida.", "rojo"))

# exportar tareas
def exportar_tareas():
    limpiar_pantalla()
    nombre_archivo = input("Escribe el nombre del archivo para exportar (ejemplo: tareas.csv): ").strip()
    
    if not nombre_archivo.endswith(".csv"):
        print(colorear_texto("El archivo debe tener extensión .csv.", "rojo"))
        input("Presiona Enter para regresar al menú principal...")
        return

    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerow(["Título", "Fecha Límite", "Prioridad", "Categoría", "Estado"])
            for tarea in tareas:
                estado = "Completada" if tarea['completada'] else "Pendiente"
                escritor_csv.writerow([tarea['titulo'], tarea['fecha_limite'], tarea['prioridad'], tarea['categoria'], estado])

        print(colorear_texto(f"Tareas exportadas a {nombre_archivo}.", "magenta"))
    except Exception as e:
        print(colorear_texto(f"Error al exportar las tareas: {str(e)}", "rojo"))

    input("Presiona Enter para regresar al menú principal...")
# importar tareas
def importar_tareas():
    limpiar_pantalla()
    nombre_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if not nombre_archivo:
        print(colorear_texto("No se seleccionó ningún archivo.", "rojo"))
        return

    with open(nombre_archivo, 'r', newline='', encoding='utf-8') as f:
        lector_csv = csv.reader(f)
        for linea in lector_csv:
            if len(linea) == 5:
                titulo, fecha_limite, prioridad, categoria, estado = linea
                tarea = {
                    "titulo": titulo,
                    "fecha_limite": fecha_limite,
                    "prioridad": prioridad,
                    "categoria": categoria,
                    "completada": estado == "Completada",
                    "hora_limite": None
                }
                tareas.append(tarea)
            else:
                print(colorear_texto(f"Linea mal formateada en el archivo: {linea}", "rojo"))

    print(colorear_texto("Tareas importadas exitosamente.", "magenta"))


# temporizador Pomodoro
def temporizador():
    limpiar_pantalla()

    def iniciar_temporizador(duracion, mensaje):
        tiempo_segundos = duracion * 60
        print(f"{mensaje} ({duracion} minutos)")
        while tiempo_segundos:
            mins, secs = divmod(tiempo_segundos, 60)
            print(f"\r{mins:02}:{secs:02}", end="")
            time.sleep(1)
            tiempo_segundos -= 1
        print("\n¡Tiempo terminado!")

    while True:
        try:
            print("Temporizador Pomodoro")
            print("1. Iniciar sesión de trabajo (25 minutos)")
            print("2. Iniciar pausa corta (5 minutos)")
            print("3. Iniciar pausa larga (15 minutos)")
            print("4. Salir")
            
            opcion = input("Elige una opción: ").strip()
            
            if opcion == "1":
                iniciar_temporizador(25, "Sesión de trabajo")
                print("¡Hora de una pausa corta!")
                iniciar_temporizador(5, "Pausa corta")
            elif opcion == "2":
                iniciar_temporizador(5, "Pausa corta")
            elif opcion == "3":
                iniciar_temporizador(15, "Pausa larga")
            elif opcion == "4":
                print("Regresando al menú principal...")
                break
            else:
                print(colorear_texto("Opción inválida. Intenta de nuevo.", "rojo"))
                
        except ValueError:
            print(colorear_texto("Entrada inválida. Intenta de nuevo.", "rojo"))

        input("Presiona Enter para continuar...")

# Función de ayuda
def mostrar_ayuda():
    limpiar_pantalla()
    print(colorear_texto("Ayuda del Sistema de Gestión de Tareas", "azul"))
    print("1. Agregar tarea: Permite añadir una nueva tarea con título, fecha límite, prioridad y categoría.")
    print("2. Eliminar tarea: Permite eliminar una tarea existente.")
    print("3. Listar tareas: Muestra todas las tareas actuales.")
    print("4. Marcar tarea como completada: Marca una tarea como completada.")
    print("5. Editar tarea: Permite editar una tarea existente.")
    print("6. Filtrar tareas: Filtra las tareas por fecha o categoría.")
    print("7. Buscar tarea: Busca una tarea por título o parte del título.")
    print("8. Mostrar calendario: Muestra el calendario del mes actual con tareas marcadas.")
    print("9. Mostrar historial de tareas completadas: Muestra el historial de tareas completadas.")
    print("10. Exportar tareas: Exporta las tareas a un archivo de texto.")
    print("11. Importar tareas: Importa tareas desde un archivo de texto.")
    print("12. Temporizador: Establece un temporizador para una tarea.")
    print("13. Salir: Sale del programa.")
    input("Presiona Enter para regresar al menú principal...")

# Función principal
def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            listar_tareas()
        elif opcion == "4":
            marcar_completada()
        elif opcion == "5":
            editar_tarea()
        elif opcion == "6":
            filtrar_tareas()
        elif opcion == "7":
            buscar_tarea()
        elif opcion == "8":
            navegar_calendario()
        elif opcion == "9":
            mostrar_historial()
        elif opcion == "10":
            mostrar_ayuda()
        elif opcion == "11":
            exportar_tareas()
        elif opcion == "12":
            importar_tareas()
        elif opcion == "13":
            temporizador()
        elif opcion == "14":
            print("Saliendo del programa...")
            break
        else:
            print(colorear_texto("Opción inválida. Intenta de nuevo.", "rojo"))

if __name__ == "__main__":
    main()
