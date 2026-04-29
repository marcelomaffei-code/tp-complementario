import csv


def lanzar_error_duplicado(codigo):
    raise Exception(f"Error: Satélite Duplicado - El código {codigo} ya existe.")

def lanzar_error_no_encontrado(codigo):
    raise Exception(f"Error: Satélite No Encontrado - El código {codigo} no existe.")

def agregar_satelite(lista_datos, satelite):
    codigo_nuevo = satelite['codigo']
    existe = False
    i = 0
    while i < len(lista_datos) and not existe: 
        if lista_datos[i]['codigo'] == codigo_nuevo:
            existe = True
        i += 1
    
    if existe:
        lanzar_error_duplicado(codigo_nuevo) 
    
    lista_datos.append(satelite)

def buscar_por_codigo(lista_datos, codigo):
    resultado = None
    i = 0
    encontrado = False
    while i < len(lista_datos) and not encontrado:
        if lista_datos[i]['codigo'] == codigo:
            resultado = lista_datos[i]
            encontrado = True
        i += 1
    
    if not encontrado:
        lanzar_error_no_encontrado(codigo)
    return resultado

def eliminar_satelite(lista_datos, codigo):
    i = 0
    encontrado = False
    while i < len(lista_datos) and not encontrado:
        if lista_datos[i]['codigo'] == codigo:
            lista_datos.pop(i)
            encontrado = True
        i += 1
    if not encontrado:
        lanzar_error_no_encontrado(codigo)

def ordenar_por_codigo(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j]['codigo'] > datos[j + 1]['codigo']:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux
    return datos

def exportar_csv(datos, ruta_archivo):
    if len(datos) > 0:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as f: # 
            columnas = []
            for clave in datos[0].keys():
                columnas.append(clave)
            
            escritor = csv.DictWriter(f, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(datos) 

def cargar_desde_csv(ruta_archivo):
    nueva_lista = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as f: # 
        lector = csv.DictReader(f)
        for fila in lector:
            fila['recorrido_km'] = float(fila['recorrido_km'])
            fila['errores_detectados'] = int(fila['errores_detectados'])
            fila['cantidad_sensores'] = int(fila['cantidad_sensores'])
            nueva_lista.append(fila)
    return nueva_lista

def consolidar_archivos(lista_rutas):
    maestro = []
    for ruta in lista_rutas:
        lote = cargar_desde_csv(ruta)
        for sat in lote:
            try:
                agregar_satelite(maestro, sat)
            except Exception:
                pass
    return ordenar_por_codigo(maestro)

def generar_estadisticas(datos):
    stats = {
        'total_satelites': 0,
        'distancia_total': 0.0,
        'errores_totales': 0,
        'sensores_activos': 0,
        'satelites_activos': 0,
        'satelites_inactivos': 0
    }
    
    for s in datos:
        stats['total_satelites'] += 1
        stats['distancia_total'] += s['recorrido_km']
        stats['errores_totales'] += s['errores_detectados']
        stats['sensores_activos'] += s['cantidad_sensores']
        if s['estado'].lower() == 'activo':
            stats['satelites_activos'] += 1
        else:
            stats['satelites_inactivos'] += 1
    return stats