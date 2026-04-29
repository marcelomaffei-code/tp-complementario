from gestion_clientes import buscar_cliente, agregar_cliente,eliminar_cliente,ordenar_por_saldo,generar_reporte

def ejecutar_sistema():

    datos = [[101,"Juan Perez","juan@mail.com", 1500.50,"Activo"],
            [102, "Juan Perez", "juan@mail.com", 1500.50,"Activo"],
            [103, "Ana Lopez", "ana@mail.com", 2300.00,"Activo"],
            [104, "Luis Gomez", "luis@mail.com", 500.25, "Inactivo"]
        ]    
    try:
        print(datos)

        encontrado = buscar_cliente(datos, 102) 
        print(f"Cliente con ID 102 encontrado en posición: {encontrado}")

        agregar_cliente(datos, 105, "Maria Garcia", "maria@mail.com", 3000.00, "Activo")
      
        print(datos)

        eliminar_cliente(datos, 103)

        print(datos)

        ordenar_por_saldo(datos)

        print(datos)

        generar_reporte(datos)

    except Exception as e:
        print(f"Error del sistema: {e}")

if __name__ == "__main__":
    ejecutar_sistema()