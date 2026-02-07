logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

urls_por_ip = {}

for ip, url, navegador in logs:
    if ip not in urls_por_ip:
        urls_por_ip[ip] = set()
    urls_por_ip[ip].add(url)

print("URLs visitadas por IP:")
print(urls_por_ip)



visitas_url = {}

for ip, url, navegador in logs:
    if url not in visitas_url:
        visitas_url[url] = 0
    visitas_url[url] += 1

print("\nVisitas por URL:")
print(visitas_url)




uso_navegadores = {}

for ip, url, navegador in logs:
    if navegador not in uso_navegadores:
        uso_navegadores[navegador] = 0
    uso_navegadores[navegador] += 1

navegador_mas_usado = ""
mayor_uso = 0

for navegador, total in uso_navegadores.items():
    if total > mayor_uso:
        mayor_uso = total
        navegador_mas_usado = navegador

print("\nNavegador más utilizado:")
print(navegador_mas_usado)



ips_unicas = set()

for ip, url, navegador in logs:
    ips_unicas.add(ip)

lista_ips = sorted(list(ips_unicas))

print("\nLista ordenada de IPs únicas:")
print(lista_ips)
