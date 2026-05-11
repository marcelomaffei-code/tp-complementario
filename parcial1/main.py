#Parcial 1 Marcelo Maffei
from proceso_monitor import ordenar_registros_monitor, generar_estadistica_monitor

def main():
    
    try:
        print("Iniciando Sistema de Observabilidad de Microservicios")
        lista_registros = ordenar_registros_monitor()
        generar_estadistica_monitor(lista_registros)
            
    except Exception as e:
        print(f"Error crítico en la ejecución: {e}")

if __name__ == "__main__":
    main()