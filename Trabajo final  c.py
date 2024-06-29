from datetime import datetime

# Diccionario para mapear números a materias
materias = {
    '1': 'Física',
    '2': 'Sociales',
    '3': 'Matemáticas',
    '4': 'Español',
    '5': 'Programación',
    '6': 'Contabilidad',
    '7': 'Inglés',
    '8': 'Educación Física'
}

def organizar_tareas(tareas, criterio):
    """
    Organiza las tareas según el criterio especificado.

    Args:
    - tareas (dict): Diccionario de tareas.
    - criterio (str): Criterio de organización ('fecha' o 'prioridad').

    Returns:
    - dict: Diccionario de tareas organizado según el criterio.
    """
    if len(tareas) == 2:
        print("No hay suficientes tareas para organizar.")
        return
    if criterio == 'fecha':
        # Ordenar por fecha
        tareas_organizadas = sorted(tareas.items(), key=lambda x: datetime.strptime(x[1]['fecha'], '%d/%m/%Y'))
        print("\n---- Tareas Ordenadas por Fecha ----")
        for matricula, tarea in tareas_organizadas:
            print(f"Matrícula: {matricula}, Materia: {tarea['materia']}, Fecha: {tarea['fecha']}, Prioridad: {tarea['prioridad']}")
    elif criterio == 'prioridad':
        # Ordenar por prioridad
        tareas_organizadas = sorted(tareas.items(), key=lambda x: x[1]['prioridad'])
        print("\n---- Tareas Ordenadas por Prioridad ----")
        for matricula, tarea in tareas_organizadas:
            print(f"Matrícula: {matricula}, Materia: {tarea['materia']}, Fecha: {tarea['fecha']}, Prioridad: {tarea['prioridad']}")
    else:
        print("Criterio no válido")

def agregar_tarea(tareas):
    """
    Agrega una nueva tarea al diccionario de tareas.

    Args:
    - tareas (dict): Diccionario de tareas.
    """
    print("\nAgregar nueva tarea:")
    while True:
        matricula = input("Matrícula del estudiante (solo 4 números): ")
        if matricula.isdigit() and len(matricula) == 4:
            break
        else:
            print("La matrícula debe contener solo 4 números. Inténtalo de nuevo.")
    while True:
        print("Seleccione la materia:")
        for num, materia in materias.items():
            print(f"{num}. {materia}")
        num_materia = input("Número de la materia: ")
        if num_materia in materias.keys():
            break
        else:
            print("Materia no válida. Inténtalo de nuevo.")
    while True:
        fecha = input("Fecha de la tarea (DD/MM/YYYY): ")
        try:
            fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
            if fecha_dt.year < 2022:
                print("La fecha no puede ser anterior a 2022. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Formato de fecha incorrecto. Inténtalo de nuevo.")
    while True:
        prioridad = input("Prioridad de la tarea (alta, media, baja): ")
        if prioridad.lower() in ['alta', 'media', 'baja']:
            break
        else:
            print("Prioridad no válida. Las opciones válidas son 'alta', 'media' y 'baja'.")
    tareas[matricula] = {'materia': materias[num_materia], 'fecha': fecha, 'prioridad': prioridad}

# Diccionario de tareas inicial
tareas = {}

# Menú de opciones
while True:
    print("\n--- Menú ---")
    print("1. Agregar nueva tarea")
    print("2. Organizar tareas")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        agregar_tarea(tareas)
    elif opcion == '2':
        if len(tareas) == 0:
            print("No hay tareas para organizar.")
        else:
            criterio = input("Selecciona el criterio de organización (fecha, prioridad): ")
            organizar_tareas(tareas, criterio)
    elif opcion == '3':
        print("Programa finalizado")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
