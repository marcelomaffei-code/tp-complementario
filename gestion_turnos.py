def validar_campo_no_vacio(valor, nombre_campo):
    if valor is None or str(valor).strip() == "":
        raise ValueError("El campo " + nombre_campo + " no puede estar vacío")

def validar_datos_paciente(dni, nombre_completo, obra_social, consultorio, motivo_consulta, hora_llega):
    validar_campo_no_vacio(dni, "dni")
    validar_campo_no_vacio(nombre_completo, "nombre_completo")
    validar_campo_no_vacio(obra_social, "obra_social")
    validar_campo_no_vacio(consultorio, "consultorio")
    validar_campo_no_vacio(motivo_consulta, "motivo_consulta")
    validar_campo_no_vacio(hora_llega, "hora_llega")

def registrar_paciente(cola_espera, dni, nombre_completo, obra_social, consultorio, motivo_consulta, hora_llega):
    validar_datos_paciente(dni, nombre_completo, obra_social, consultorio, motivo_consulta, hora_llega)
    dni = str(dni)
    existe = False
    dim = len(cola_espera)
    i = 0
    while i < dim and not existe:
        if cola_espera[i]["dni"] == dni:
            existe = True
        i = i + 1
    if existe:
        raise ValueError("Ya existe un paciente esperando con DNI " + dni)
    paciente = crear_paciente(dni, nombre_completo, obra_social, consultorio, motivo_consulta, hora_llega)
    cola_espera.append(paciente)
    return len(cola_espera)

def crear_paciente(dni, nombre_completo, obra_social, consultorio, motivo_consulta, hora_llega):
    paciente = {
        "dni": str(dni),
        "nombre_completo": nombre_completo,
        "obra_social": obra_social,
        "consultorio": consultorio,
        "motivo_consulta": motivo_consulta,
        "hora_llega": hora_llega,
        "estado": "Esperando"
    }
    return paciente

def llamar_siguiente(cola_espera, pacientes_atendidos):
    if len(cola_espera) == 0:
        raise ValueError("No hay pacientes en espera")
    paciente = cola_espera.pop(0)
    paciente["estado"] = "Atendido"
    pacientes_atendidos.append(paciente)
    return paciente



class PacienteNoEncontrado(Exception):
    pass








def buscar_paciente(cola_espera, dni):
    """
    Complejidad: O(n)
    Busca un paciente por DNI dentro de la cola de espera.
    Devuelve el paciente y su posición aproximada.
    """
    dni = str(dni)
    paciente_encontrado = None
    posicion = -1

    i = 0
    while i < len(cola_espera):
        if cola_espera[i]["dni"] == dni and paciente_encontrado is None:
            paciente_encontrado = cola_espera[i]
            posicion = i + 1
        i = i + 1

    if paciente_encontrado is None:
        raise PacienteNoEncontrado("Paciente DNI " + dni + " no encontrado en espera")

    return paciente_encontrado, posicion


def remover_paciente(cola_espera, dni):
    """
    Complejidad: O(n)
    Remueve de la cola un paciente que abandonó la sala.
    """
    dni = str(dni)
    paciente_removido = None
    nueva_cola = []

    i = 0
    while i < len(cola_espera):
        if cola_espera[i]["dni"] == dni and paciente_removido is None:
            paciente_removido = cola_espera[i]
        else:
            nueva_cola.append(cola_espera[i])
        i = i + 1

    if paciente_removido is None:
        raise PacienteNoEncontrado("Paciente DNI " + dni + " no encontrado en espera")

    cola_espera.clear()

    j = 0
    while j < len(nueva_cola):
        cola_espera.append(nueva_cola[j])
        j = j + 1

    return paciente_removido


def pacientes_en_espera(cola_espera):
    """
    Complejidad: O(1)
    Devuelve la cantidad de pacientes esperando.
    """
    return len(cola_espera)


def obtener_campo(paciente, campo):
    """
    Complejidad: O(1)
    Devuelve el valor de un campo.
    """
    if campo not in paciente:
        raise ValueError("El campo " + campo + " no existe en el paciente")

    return paciente[campo]


def generar_reporte_ordenado(pacientes, campo):
    """
    Complejidad: O(n²)
    Genera una nueva lista ordenada por el campo indicado.
    Se implementa insertion sort manual para no usar sorted() ni .sort().
    """
    reporte = []

    i = 0
    while i < len(pacientes):
        paciente_actual = pacientes[i]
        reporte.append(paciente_actual)

        j = len(reporte) - 1
        while j > 0 and obtener_campo(reporte[j - 1], campo) > obtener_campo(reporte[j], campo):
            auxiliar = reporte[j - 1]
            reporte[j - 1] = reporte[j]
            reporte[j] = auxiliar
            j = j - 1

        i = i + 1

    return reporte


def convertir_paciente_a_linea_csv(paciente):
    """
    Complejidad: O(1)
    Convierte un paciente en una línea CSV simple.
    """
    linea = (
        paciente["dni"] + "," +
        paciente["nombre_completo"] + "," +
        paciente["obra_social"] + "," +
        paciente["consultorio"] + "," +
        paciente["motivo_consulta"] + "," +
        paciente["hora_llega"] + "," +
        paciente["estado"]
    )

    return linea


def exportar_reporte(pacientes, ruta_archivo):
    """
    Complejidad: O(n)
    Exporta los pacientes a un archivo CSV usando with.
    """
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("dni,nombre_completo,obra_social,consultorio,motivo_consulta,hora_llega,estado\n")

        i = 0
        while i < len(pacientes):
            linea = convertir_paciente_a_linea_csv(pacientes[i])
            archivo.write(linea + "\n")
            i = i + 1

    return ruta_archivo


def cargar_historial(ruta_archivo):
    """
    Complejidad: O(n)
    Carga pacientes desde un archivo CSV.
    """
    pacientes = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        i = 1
        while i < len(lineas):
            linea = lineas[i].strip()
            datos = linea.split(",")

            if len(datos) == 7:
                paciente = {
                    "dni": datos[0],
                    "nombre_completo": datos[1],
                    "obra_social": datos[2],
                    "consultorio": datos[3],
                    "motivo_consulta": datos[4],
                    "hora_llega": datos[5],
                    "estado": datos[6]
                }

                pacientes.append(paciente)

            i = i + 1

    return pacientes