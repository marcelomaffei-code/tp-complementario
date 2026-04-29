COL_ID = 0
COL_NOMBRE = 1
COL_EMAIL = 2   
COL_SALDO = 3
COL_ESTADO = 4

def buscar_cliente(db, id_cliente):
    dim = len(db)
    pos_i = 0
    pos_encontrada = -1
    while pos_encontrada==-1 and pos_i < dim:
       if (db[pos_i][COL_ID] == id_cliente):
           pos_encontrada = pos_i
       pos_i += 1
    return pos_encontrada       

def agregar_cliente(db, id_cliente, nombre, email, saldo, estado):
    pos = buscar_cliente(db,id_cliente)
    if pos == -1:
        db.append([id_cliente, nombre, email, saldo, estado])
    else:
        raise ValueError("Cliente ya existe")

def eliminar_cliente(db, id_cliente):
    pos = buscar_cliente(db,id_cliente)
    if pos > -1:
        del db[pos]
    else:     
        raise ValueError("Cliente no encontrado")

def ordenar_por_saldo(db):
    dim = len(db)
    for item_i in range(dim):
        for item_j in range(0,dim-item_i-1):
            if db[item_j][COL_SALDO] < db[item_j+1][COL_SALDO]:
               if (db[item_j][COL_SALDO] < db[item_j+1][COL_SALDO]):
                   db[item_j], db[item_j+1] = db[item_j+1], db[item_j]

def generar_reporte(db):
    dim = len(db)
    total_clientes = 0
    total_saldo = 0
    total_activos = 0
    for cliente in db:
       if cliente[COL_ESTADO] == "Activo":
            total_activos += 1
            total_saldo += cliente[COL_SALDO]
    total_clientes = dim
    print(f"Total Clientes: {total_clientes}")
    print(f"Total Saldo: {total_saldo}")    
    print(f"Total Activos: {total_activos}")
