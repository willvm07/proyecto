# gestor_estudiantes.py

students = []
materias = []

def agregar_materia(nombre):
    if nombre not in materias:
        materias.append(nombre)
        return True
    return False

def listar_materias():
    return materias

def agregar_estudiante(carnet, nombre, edad, nivel):
    estudiante = {
        "carnet": carnet,
        "nombre": nombre,
        "edad": edad,
        "nivel": nivel,
        "calificaciones": []
    }
    students.append(estudiante)
    return estudiante

def buscar_estudiante(carnet):
    for estudiante in students:
        if estudiante["carnet"] == carnet:
            return estudiante
    return None

def modificar_estudiante(carnet, nombre=None, edad=None, nivel=None):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        if nombre:
            estudiante["nombre"] = nombre
        if edad:
            estudiante["edad"] = edad
        if nivel:
            estudiante["nivel"] = nivel
        return estudiante
    return None

def eliminar_estudiante(carnet):
    global students
    students = [estudiante for estudiante in students if estudiante["carnet"] != carnet]

def agregar_calificacion(carnet, materia, calificacion):
    estudiante = buscar_estudiante(carnet)
    if estudiante:
        estudiante["calificaciones"].append({"materia": materia, "calificacion": calificacion})

def calcular_promedio(carnet):
    estudiante = buscar_estudiante(carnet)
    if estudiante and estudiante["calificaciones"]:
        total = sum([cal["calificacion"] for cal in estudiante["calificaciones"]])
        return total / len(estudiante["calificaciones"])
    return None

def listar_aprobados_reprobados():
    aprobados = []
    reprobados = []
    for estudiante in students:
        promedio = calcular_promedio(estudiante["carnet"])
        if promedio is not None:
            if promedio >= 7:
                aprobados.append(estudiante)
            else:
                reprobados.append(estudiante)
    return aprobados, reprobados





