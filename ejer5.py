partidas = [
    ("Cesar", "Bosque", 120),
    ("Lalenteja", "Desierto", 90),
    ("Ronco", "Bosque", 150),
    ("Javisxs", "Ciudad", 200),
    ("Padilla", "Bosque", 110)
]

puntos_por_jugador = {}

for jugador, mapa, puntos in partidas:
    if jugador not in puntos_por_jugador:
        puntos_por_jugador[jugador] = 0
        
    puntos_por_jugador[jugador] += puntos

print("Total de puntos por jugador:")
print(puntos_por_jugador)


mapas_jugados = set()

for jugador, mapa, puntos in partidas:
    mapas_jugados.add(mapa)

print("\nMapas jugados:")
print(mapas_jugados)



conteo_partidas = {}

for jugador, mapa, puntos in partidas:
    if jugador not in conteo_partidas:
        conteo_partidas[jugador] = 0
        
    conteo_partidas[jugador] += 1



promedio_puntos = {}

for jugador in puntos_por_jugador:
    promedio_puntos[jugador] = puntos_por_jugador[jugador] / conteo_partidas[jugador]

print("\nPromedio de puntos por jugador:")
print(promedio_puntos)




puntos_por_mapa = {}

for jugador, mapa, puntos in partidas:
    if mapa not in puntos_por_mapa:
        puntos_por_mapa[mapa] = 0
        
    puntos_por_mapa[mapa] += puntos

mapa_mayor = ""
mayor_puntaje = 0

for mapa, total in puntos_por_mapa.items():
    if total > mayor_puntaje:
        mayor_puntaje = total
        mapa_mayor = mapa

print("\nMapa con más puntos acumulados:")
print(mapa_mayor, "con", mayor_puntaje, "puntos")
