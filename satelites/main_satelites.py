from gestion_satelites import (
    agregar_satelite,
    buscar_por_codigo,
    eliminar_satelite,
    ordenar_por_codigo,
    exportar_csv,
    cargar_desde_csv,
    consolidar_archivos,
    generar_estadisticas
)

import os

print("Actualmente estoy parado en:", os.getcwd())

def mostrar_menu():
    print("\n--- SISTEMA DE CONTROL SATELITAL (CCSN) ---")
    print("1. Registrar nuevo satélite")
    print("2. Buscar satélite por código")
    print("3. Eliminar satélite")
    print("4. Listar satélites (ordenados)")
    print("5. Consolidar archivos (.csv)")
    print("6. Generar estadísticas globales")
    print("7. Exportar base de datos actual")
    print("0. Salir")
    return input("Seleccione una opción: ")

flota_satelites = []

ejecutando = True
while ejecutando:
    opcion = mostrar_menu()

    if opcion == "1":
        try:
            print("\n-- Registro de Satélite --")
            sat = {
                'codigo': input("Código (ej: SAT-ARG-001): "),
                'nombre': input("Nombre: "),
                'recorrido_km': float(input("Distancia recorrida (km): ")),
                'fecha_lanzamiento': input("Fecha (YYYY-MM-DD): "),
                'pais_origen': input("País: "),
                'funcion': input("Función: "),
                'tipo_orbita': input("Tipo de órbita: "),
                'imagenes_descargadas': int(input("Imágenes descargadas: ")),
                'errores_detectados': int(input("Errores detectados: ")),
                'cantidad_sensores': int(input("Cantidad de sensores: ")),
                'resolucion_espacial': float(input("Resolución espacial: ")),
                'resolucion_espectral': int(input("Resolución espectral: ")),
                'estado': input("Estado (Activo/Inactivo): ")
            }
            agregar_satelite(flota_satelites, sat)
            print("Satélite registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar: {e}")

    elif opcion == "2":
        codigo = input("Ingrese el código a buscar: ")
        try:
            sat = buscar_por_codigo(flota_satelites, codigo)
            print(f"\nDatos encontrados: {sat}")
        except Exception as e:
            print(e)

    elif opcion == "3":
        codigo = input("Ingrese el código del satélite a eliminar: ")
        try:
            eliminar_satelite(flota_satelites, codigo)
            print("Satélite eliminado correctamente.")
        except Exception as e:
            print(e)

    elif opcion == "4":
        if len(flota_satelites) > 0:
            flota_satelites = ordenar_por_codigo(flota_satelites)
            print("\n--- LISTADO DE FLOTA ---")
            for s in flota_satelites:
                print(f"[{s['codigo']}] {s['nombre']} - Estado: {s['estado']}")
        else:
            print("La flota está vacía.")

    elif opcion == "5":
        print("\nConsolidando archivos de entrada...")
        archivos = ["satelites/datos/satelites_muestra.csv", "satelites/datos/satelites_muestra2.csv"]
        try:
            flota_satelites = consolidar_archivos(archivos)
            print("Consolidación completada y datos cargados en memoria.")
        except Exception as e:
            print(f"Error en consolidación: {e}. Asegúrese de que los archivos existan.")

    elif opcion == "6":
        if len(flota_satelites) > 0:
            stats = generar_estadisticas(flota_satelites)
            print("\n--- ESTADÍSTICAS GLOBALES [cite: 165] ---")
            print(f"Total Satélites: {stats['total_satelites']}")
            print(f"Distancia Total: {stats['distancia_total']} km")
            print(f"Errores Totales: {stats['errores_totales']}")
            print(f"Sensores Activos: {stats['sensores_activos']}")
            print(f"Satélites Activos: {stats['satelites_activos']}")
            print(f"Satélites Inactivos: {stats['satelites_inactivos']}")
        else:
            print("No hay datos para generar estadísticas.")

    elif opcion == "7":
        try:
            exportar_csv(flota_satelites, "archivo_maestro_satelites.csv")
            print("Datos exportados exitosamente a 'archivo_maestro_satelites.csv'.")
        except Exception as e:
            print(f"Error al exportar: {e}")

    elif opcion == "0":
        print("Cerrando sistema...")
        ejecutando = False
    
    else:
        print("Opción no válida.")