
estudiantes = [
    ("Ana", 85, 90, 78, 92),
    ("Luis", 88, 76, 95),
    ("Carlos", 100, 98),
    ("María", 70, 80, 75, 85, 90)
]

diccionario_estudiante = {}

for estudiante in estudiantes:
    nombre, *calificaciones = estudiante
    promedio = sum(calificaciones) / len(calificaciones)
    diccionario_estudiante[nombre] = {
        "promedio": promedio,
        "max": max(calificaciones),
        "min": min(calificaciones)
    }

mejor_estudiante = max(diccionario_estudiante.items(), key=lambda x: x[1]["promedio"])
nombre_top, datos_top = mejor_estudiante

print(diccionario_estudiante)
print(f"El promedio más alto es de {nombre_top} con {datos_top['promedio']}")

