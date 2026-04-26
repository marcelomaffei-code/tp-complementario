from gestion_turnos import registrar_paciente,llamar_siguiente
 #   buscar_paciente,
  #  remover_paciente,
   # pacientes_en_espera,
    #generar_reporte_ordenado,
  #  exportar_reporte,
  #  PacienteDuplicado,
  #  PacienteNoEncontrado,
  #  EsperaVacia


#def mostrar_paciente_llamado(paciente):
#    print("Llamando al siguiente paciente: " + paciente["nombre_completo"] + " (DNI: " + paciente["dni"] + ")")


def main():

    cola_espera = []
    #pacientes_atendidos = []
    print("GESTIÓN DE TURNOS")
    print("\nREGISTRANDO PACIENTES")

    try:
        posicion = registrar_paciente(cola_espera,"28123456","María Pérez","OSDE","C-101","Control general","08:01")
        posicion = registrar_paciente(cola_espera,"30456789","Juan Gómez","Swiss Medical","C-102","Dolor de cabeza","08:05")
        posicion = registrar_paciente(cola_espera,"25789012","Laura Ruiz","PAMI","C-103","Control de presión","08:12")
        posicion = registrar_paciente(cola_espera,"32345678","Carlos Díaz","OSDE","C-104","Consulta clínica","08:20")
        posicion = registrar_paciente(cola_espera,"29876543","Ana Martínez","Galeno","C-105","Dolor abdominal","08:25")
        posicion = registrar_paciente(cola_espera,"35123456","Pedro López","Medifé","C-106","Chequeo","08:30")
        posicion = registrar_paciente(cola_espera,"26543210","Sofía Fernández","PAMI","C-107","Consulta médica","08:35")
 
    except ValueError as error:
        print("Error " + str(error))

    for paciente in cola_espera:
        print(
            "Paciente DNI " + paciente["dni"] +
            ": " + paciente["nombre_completo"] +
            " - Obra Social: " + paciente["obra_social"] +
            " - Consultorio: " + paciente["consultorio"] +
            " - Motivo: " + paciente["motivo_consulta"] +
            " - Estado: " + paciente["estado"] +
            " - Hora de llegada: " + paciente["hora_llega"]
        )

    print("\n[2] ATENDIENDO PACIENTES...")
    try:
        paciente = llamar_siguiente(cola_espera)
        paciente = llamar_siguiente(cola_espera)
    except ValueError as error:
        print("Error: " + str(error))


    for paciente in cola_espera:
        print(
            "Paciente DNI " + paciente["dni"] +
            ": " + paciente["nombre_completo"] +
            " - Obra Social: " + paciente["obra_social"] +
            " - Consultorio: " + paciente["consultorio"] +
            " - Motivo: " + paciente["motivo_consulta"] +
            " - Hora de llegada: " + paciente["hora_llega"]
        )

"""

    print("\n[3] CONSULTA DE ESTADO...")

    try:
        paciente, posicion = buscar_paciente(cola_espera, "32345678")
        print(
            "Paciente DNI 32345678: " +
            paciente["nombre_completo"] +
            " - Estado: " +
            paciente["estado"] +
            " - Posición aproximada: " +
            str(posicion)
        )
    except PacienteNoEncontrado:
        print("Paciente DNI 32345678: No encontrado en espera")

    try:
        paciente, posicion = buscar_paciente(cola_espera, "99999999")
        print(
            "Paciente DNI 99999999: " +
            paciente["nombre_completo"] +
            " - Estado: " +
            paciente["estado"]
        )
    except PacienteNoEncontrado:
        print("Paciente DNI 99999999: No encontrado en espera")

    print("\n[4] PACIENTE ABANDONA LA SALA...")

    try:
        paciente = remover_paciente(cola_espera, "25789012")
        print(paciente["nombre_completo"] + " (DNI: " + paciente["dni"] + ") removido de la espera")
    except PacienteNoEncontrado as error:
        print("Error: " + str(error))

    print("\n[5] CONTINUAR ATENCIÓN...")

    try:
        paciente = llamar_siguiente(cola_espera, pacientes_atendidos)
        mostrar_paciente_llamado(paciente)

        paciente = llamar_siguiente(cola_espera, pacientes_atendidos)
        mostrar_paciente_llamado(paciente)

    except EsperaVacia as error:
        print("Error: " + str(error))

    print("\n[6] GENERANDO REPORTE DIARIO (ordenado por obra social)...")

    reporte = generar_reporte_ordenado(pacientes_atendidos, "obra_social")

    ruta_archivo = "reporte_diario_2026_04_25.csv"
    print("Exportando reporte a: " + ruta_archivo)

    print("- Pacientes atendidos hoy: " + str(len(pacientes_atendidos)))
    print("- Pacientes aún en espera: " + str(pacientes_en_espera(cola_espera)))

    print("\n[7] AL UTILIZAR EL SAVE PERMITE GUARDAR LO DEL DÍA.")

    try:
        exportar_reporte(reporte, ruta_archivo)
        print("Reporte guardado exitosamente.")
    except OSError as error:
        print("No se pudo guardar el reporte: " + str(error))
        
        
        
    """


main()