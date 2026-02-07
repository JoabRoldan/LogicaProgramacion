# Datos de entrada
asistencias = [
    ("Matemáticas", "padilla", "2024-09-01"),
    ("Matemáticas", "cesar", "2024-09-01"),
    ("Física", "Axel", "2024-09-01"),
    ("Matemáticas", "Javier", "2024-09-02"),
    ("Física", "Alvarez", "2024-09-02")
]

asignaturas = {}

for asignatura, alumno, fecha in asistencias:
    if asignatura not in asignaturas:
        asignaturas[asignatura] = set()
        
    asignaturas[asignatura].add(alumno)

print("Alumnos por asignatura:")
print(asignaturas)



dias_por_alumno = {}

for asignatura, alumno, fecha in asistencias:
    if alumno not in dias_por_alumno:
        dias_por_alumno[alumno] = set()
        
    dias_por_alumno[alumno].add(fecha)



conteo_dias = {}

for alumno, dias in dias_por_alumno.items():
    conteo_dias[alumno] = len(dias)

print("\nDías distintos de asistencia por alumno:")
print(conteo_dias)

total_asistencias = {}

for asignatura, alumno, fecha in asistencias:
    if alumno not in total_asistencias:
        total_asistencias[alumno] = 0
        
    total_asistencias[alumno] += 1

mayor_alumno = ""
mayor_asistencia = 0

for alumno, total in total_asistencias.items():
    if total > mayor_asistencia:
        mayor_asistencia = total
        mayor_alumno = alumno

print("\nAlumno con mayor número de asistencias:")
print(mayor_alumno, "con", mayor_asistencia, "asistencias")
