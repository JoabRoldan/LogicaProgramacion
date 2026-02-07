inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]


productos_por_categoria = {}

for item in inventario:
    categoria = item["categoria"]
    producto = item["producto"]
    
    if categoria not in productos_por_categoria:
        productos_por_categoria[categoria] = []
        
    productos_por_categoria[categoria].append(producto)

print("Productos por categoría:")
print(productos_por_categoria)



agotados = set()

for item in inventario:
    if item["stock"] == 0:
        agotados.add(item["producto"])

print("\nProductos agotados:")
print(agotados)


stock_bajo = []

for item in inventario:
    if item["stock"] < 5:
        stock_bajo.append(item["producto"])

stock_bajo = tuple(stock_bajo)

print("\nProductos con stock menor a 5:")
print(stock_bajo)


total_por_categoria = {}

for item in inventario:
    categoria = item["categoria"]
    
    if categoria not in total_por_categoria:
        total_por_categoria[categoria] = 0
        
    total_por_categoria[categoria] += 1

print("\nTotal de productos por categoría:")
print(total_por_categoria)
