ventas = [
    ("Cesar", "Enero", "Laptop", 2, 15000),
    ("alejandro", "Enero", "Mouse", 10, 250),
    ("Axel", "Febrero", "Laptop", 1, 15000),
    ("Alma", "Febrero", "Teclado", 5, 800),
    ("Javier", "Enero", "Mouse", 3, 250)
]

ingresos_por_empleado = {}

for empleado, mes, producto, cantidad, precio in ventas:
    total = cantidad * precio
    
    if empleado not in ingresos_por_empleado:
        ingresos_por_empleado[empleado] = 0
        
    ingresos_por_empleado[empleado] += total

print("Ingresos por empleado:")
print(ingresos_por_empleado)

productos_unicos = set()

for venta in ventas:
    productos_unicos.add(venta[2])

print("\nProductos únicos vendidos:")
print(productos_unicos)

ingresos_por_mes = {}

for empleado, mes, producto, cantidad, precio in ventas:
    total = cantidad * precio
    
    if mes not in ingresos_por_mes:
        ingresos_por_mes[mes] = 0
        
    ingresos_por_mes[mes] += total

print("\nIngresos por mes:")
print(ingresos_por_mes)


mayor_empleado = ""
mayor_ingreso = 0

for empleado, ingreso in ingresos_por_empleado.items():
    if ingreso > mayor_ingreso:
        mayor_ingreso = ingreso
        mayor_empleado = empleado

print("\nEmpleado con mayores ingresos:")
print(mayor_empleado, "con", mayor_ingreso)
