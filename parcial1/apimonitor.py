registros = [
    {
        "name": "auth-service",
        "cant_request": 200,
        "cant_down": 5,
        "sizeof_memory_ocuped": 1024,
        "port_active": 8080,
        "lang_service": "Java",
        "id_service": 1
    },
    {
        "name": "payment-service",
        "cant_request": 150,
        "cant_down": 3,
        "sizeof_memory_ocuped": 800,
        "port_active": 5000,
        "lang_service": "Python",
        "id_service": 2
    },
    {
        "name": "report-service",
        "cant_request": 200,
        "cant_down": 20,
        "sizeof_memory_ocuped": 1200,
        "port_active": 8081,
        "lang_service": "Java",
        "id_service": 3
    },
    {
        "name": "gateway-service",
        "cant_request": 450,
        "cant_down": 8,
        "sizeof_memory_ocuped": 900,
        "port_active": 3000,
        "lang_service": "Go",
        "id_service": 4
    },
    {
        "name": "api-service",
        "cant_request": 200,
        "cant_down": 6,
        "sizeof_memory_ocuped": 700,
        "port_active": 5001,
        "lang_service": "Python",
        "id_service": 5
    },
    {
        "name": "cache-service",
        "cant_request": 0,
        "cant_down": 0,
        "sizeof_memory_ocuped": 600,
        "port_active": 9090,
        "lang_service": "Go",
        "id_service": 6
    },
    {
        "name": "registro-invalido",
        "cant_request": "300",
        "cant_down": 4,
        "sizeof_memory_ocuped": 500,
        "port_active": 8082,
        "lang_service": "Java",
        "id_service": 7
    }
]

posicion_actual = 0


def begin_record():
    global posicion_actual
    posicion_actual = 0


def get_registros_observabilidad():
    return len(registros)


def next_registro():
    global posicion_actual

    registro = None

    if posicion_actual < len(registros):
        registro = registros[posicion_actual]
        posicion_actual = posicion_actual + 1

    return registro