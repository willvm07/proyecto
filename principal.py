
import gestor_estudiantes as ge

def mostrar_menu():
    print("1. INGRESAR ESTUDIANTE")
    print("2. MODIFICAR ESTUDIANTE")
    print("3. ELIMINAR ESTUDIANTE")
    print("4. INGRESAR MATERIAS")
    print("5. CALIFICAR ESTUDIANTE")
    print("6. REPORTES")
    print("   6.1. ESTUDIANTES APROBADOS")
    print("   6.2. ESTUDIANTES REPROBADOS")
    print("7. SALIR")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            carnet = input("Ingrese el carnet del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = int(input("Ingrese la edad del estudiante: "))
            nivel = input("Ingrese el nivel del estudiante: ")
            ge.agregar_estudiante(carnet, nombre, edad, nivel)
        elif opcion == '2':
            carnet = input("Ingrese el carnet del estudiante: ")
            nombre = input("Ingrese el nuevo nombre (presione Enter para omitir): ") or None
            edad = input("Ingrese la nueva edad (presione Enter para omitir): ")
            edad = int(edad) if edad else None
            nivel = input("Ingrese el nuevo nivel (presione Enter para omitir): ") or None
            ge.modificar_estudiante(carnet, nombre, edad, nivel)
        elif opcion == '3':
            carnet = input("Ingrese el carnet del estudiante: ")
            ge.eliminar_estudiante(carnet)
        elif opcion == '4':
            nombre_materia = input("Ingrese el nombre de la materia: ")
            if ge.agregar_materia(nombre_materia):
                print(f"Materia {nombre_materia} agregada exitosamente")
            else:
                print("La materia ya existe")
        elif opcion == '5':
            carnet = input("Ingrese el carnet del estudiante: ")
            materia = input("Ingrese la materia: ")
            calificacion = float(input("Ingrese la calificación: "))
            ge.agregar_calificacion(carnet, materia, calificacion)
        elif opcion == '6':
            subopcion = input("Seleccione una opción de reporte:\n1. Estudiantes Aprobados\n2. Estudiantes Reprobados\n")
            if subopcion == '1':
                aprobados, _ = ge.listar_aprobados_reprobados()
                print("Estudiantes Aprobados:")
                for estudiante in aprobados:
                    print(estudiante)
            elif subopcion == '2':
                _, reprobados = ge.listar_aprobados_reprobados()
                print("Estudiantes Reprobados:")
                for estudiante in reprobados:
                    print(estudiante)
            else:
                print("Opción no válida")
        elif opcion == '7':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
