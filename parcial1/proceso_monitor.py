import apimonitor

def registro_tiene_campo(registro, campo):
    tiene = False
    if campo in registro:
        tiene = True
    return tiene

def validar_registro(registro): #valido daros
    valido = True
    try:
        if type(registro) != dict:
            valido = False
        if valido and not registro_tiene_campo(registro, "name"):
            valido = False
        if valido and not registro_tiene_campo(registro, "cant_request"):
            valido = False
        if valido and not registro_tiene_campo(registro, "cant_down"):
            valido = False
        if valido and not registro_tiene_campo(registro, "sizeof_memory_ocuped"):
            valido = False
        if valido and not registro_tiene_campo(registro, "port_active"):
            valido = False
        if valido and not registro_tiene_campo(registro, "lang_service"):
            valido = False
        if valido and not registro_tiene_campo(registro, "id_service"):
            valido = False
        if valido and type(registro["name"]) != str:
            valido = False
        if valido and type(registro["cant_request"]) != int:
            valido = False
        if valido and type(registro["cant_down"]) != int:
            valido = False
        if valido and type(registro["sizeof_memory_ocuped"]) != int:
            valido = False
        if valido and type(registro["port_active"]) != int:
            valido = False
        if valido and type(registro["lang_service"]) != str:
            valido = False
        if valido and type(registro["id_service"]) != int:
            valido = False
        if valido and registro["name"] == "":
            valido = False
        if valido and registro["lang_service"] == "":
            valido = False
        return valido
    except Exception:
        valido = False

def ordenar_registros_monitor():
    registros_ordenados = []
    apimonitor.begin_record() #permite posicionar al inicio los registros de métricas
    total_registros = apimonitor.get_registros_observabilidad() # devuelve la cantidad total de registros disponiblesddsfg
    contador = 0
    while contador < total_registros:
        registro = apimonitor.next_registro()
        if validar_registro(registro): #evuelve el siguiente registro o None si no hay
            registro_normalizado = copiar_registro_normalizado(registro)
            insertar_ordenado_por_lenguaje(registros_ordenados, registro_normalizado)
        contador = contador + 1
    return registros_ordenados

def copiar_registro_normalizado(registro):
    nuevo_registro = {}
    nuevo_registro["name"] = registro["name"]
    nuevo_registro["cant_request"] = registro["cant_request"]
    nuevo_registro["cant_down"] = registro["cant_down"]
    nuevo_registro["sizeof_memory_ocuped"] = registro["sizeof_memory_ocuped"]
    nuevo_registro["port_active"] = registro["port_active"]
    nuevo_registro["lang_service"] = registro["lang_service"]
    nuevo_registro["id_service"] = registro["id_service"]
    return nuevo_registro

def insertar_ordenado_por_lenguaje(lista_registros, registro):
    posicion = 0
    insertado = False
    while posicion < len(lista_registros) and not insertado:
        if registro["lang_service"] < lista_registros[posicion]["lang_service"]:
            lista_registros.insert(posicion, registro)
            insertado = True
        else:
            posicion = posicion + 1
    if not insertado:
        lista_registros.append(registro)

def escribir_linea_reporte(archivo, texto):
    archivo.write(texto + "\n")

def generar_estadistica_monitor(lista_registros):
    try:
        archivo = open("reporte_monitor.txt", "w", encoding="utf-8")
        escribir_linea_reporte(archivo, "==============================================================")
        escribir_linea_reporte(archivo, "REPORTE DE OBSERVABILIDAD DE SERVICIOS")
        escribir_linea_reporte(archivo, "==============================================================")
        escribir_linea_reporte(archivo, "")
        escribir_linea_reporte(archivo, "1. RESUMEN POR LENGUAJE DE SERVICIO (LANG_SERVICE):")
        escribir_linea_reporte(archivo, "Lenguaje        Servicios      Total Requests      Total Downs")
        escribir_linea_reporte(archivo, "--------------------------------------------------------------")

        if len(lista_registros) > 0:
            mayor_caida = lista_registros[0]
            menor_caida = lista_registros[0]
            posicion = 0
            while posicion < len(lista_registros):
                lenguaje_actual = lista_registros[posicion]["lang_service"]
                cantidad_servicios = 0
                total_requests = 0
                total_downs = 0

                while posicion < len(lista_registros) and lista_registros[posicion]["lang_service"] == lenguaje_actual:
                    registro = lista_registros[posicion]

                    cantidad_servicios = cantidad_servicios + 1
                    total_requests = total_requests + registro["cant_request"]
                    total_downs = total_downs + registro["cant_down"]
                    if registro["cant_down"] > mayor_caida["cant_down"]:
                        mayor_caida = registro
                    if registro["cant_down"] < menor_caida["cant_down"]:
                        menor_caida = registro
                    posicion = posicion + 1
                linea = lenguaje_actual
                linea = linea + " " * (16 - len(lenguaje_actual))
                linea = linea + str(cantidad_servicios)
                linea = linea + " " * (15 - len(str(cantidad_servicios)))
                linea = linea + str(total_requests)
                linea = linea + " " * (20 - len(str(total_requests)))
                linea = linea + str(total_downs)
                escribir_linea_reporte(archivo, linea)
            escribir_linea_reporte(archivo, "")
            escribir_linea_reporte(archivo, "2. SERVICIOS CON MAYOR Y MENOR CAÍDA:")
            escribir_linea_reporte(archivo,"Mayor Caída: " + mayor_caida["name"] + " (" + mayor_caida["lang_service"] + ")")
            escribir_linea_reporte(archivo,"Cantidad de caídas: " + str(mayor_caida["cant_down"]))
            escribir_linea_reporte(archivo,"Menor Caída: " + menor_caida["name"] + " (" + menor_caida["lang_service"] + ")")
            escribir_linea_reporte(archivo,"Cantidad de caídas: " + str(menor_caida["cant_down"]))

            print("Servicio con mayor cantidad de caídas:")
            print(mayor_caida["name"], "-", mayor_caida["lang_service"], "-", mayor_caida["cant_down"])
            print("Servicio con menor cantidad de caídas:")
            print(menor_caida["name"], "-", menor_caida["lang_service"], "-", menor_caida["cant_down"])

        else:
            escribir_linea_reporte(archivo, "No hay registros válidos para procesar.")
            print("No hay registros válidos para procesar.")
        archivo.close()
    except IOError:
        print("Error crítico: No se pudo escribir el archivo de reporte.")