import re
import datetime

# Diccionario que actúa como una base de datos en memoria
# Guardará los clientes y sus órdenes
base_datos = {}  # Estructura: {id_cliente: {"datos": {...}, "ordenes": [...]}}

'''
Estructura={
    "id_cliente":{
        "datos":{
            id:,
            tel:,
            nombre:,
            email:
        },
        "ordenes":[1,2,3,4] 
    }
}
'''


# Menú de platos disponibles en el restaurante
menu = {
    "1": {
        "nombre": "Bandeja Paisa",
        "descripcion": "Frijoles, arroz, chicharrón, carne, huevo, plátano maduro.",
        "tamaños": {"Personal": 10000, "Compartir": 15000}
    },
    "2": {
        "nombre": "Ajiaco",
        "descripcion": "Sopa con tres papas, pollo, arroz, crema y aguacate.",
        "tamaños": {"Pequeño": 15000, "Grande": 20000}
    },
    "3": {
        "nombre": "Arepa Rellena",
        "descripcion": "Arepa rellena con queso, pollo o carne.",
        "tamaños": {"Sencilla": 25000, "Doble": 30000}
    }
    
}

# === FUNCIONES DE VALIDACIÓN ===

# Valida que el nombre tenga solo letras y espacios
def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+", nombre) #letras de la a-z, mayus y min, incluye tildes y ñ, incluye espacios, uno o mas caracteres 

# Valida que el correo tenga formato correcto
def validar_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)# uno o mas caracteres @ uno o mas caracteres . uno o mas caractes 

# Valida que el teléfono tenga entre 7 y 10 dígitos
def validar_telefono(telefono):
    return re.fullmatch(r"\d{7,10}", telefono)#cualquier numero entre 0 y 9, entre 7 y 10 numeros

# Valida que el documento tenga entre 5 y 15 dígitos
def validar_documento(documento):
    return re.fullmatch(r"\d{5,15}", documento)

# === FUNCIÓN PARA REGISTRAR CLIENTE ===
def registrar_cliente(nuevo_id):
    print("\n--- REGISTRO DE CLIENTE ---")
    while True:
        try:
            nombre = input("Ingrese su nombre completo: ")
            if not validar_nombre(nombre):
                raise ValueError("Nombre inválido.")

            correo = input("Ingrese su correo: ")
            if not validar_email(correo):
                raise ValueError("Correo inválido.")

            telefono = input("Ingrese su teléfono: ")
            if not validar_telefono(telefono):
                raise ValueError("Teléfono inválido.")

            documento = input("Ingrese su número de documento: ")
            if not validar_documento(documento):
                raise ValueError("Documento inválido.")

            # Selección de medio de pago
            print("Seleccione medio de pago:")
            print("1. Débito  2. Crédito  3. Efectivo  4. Bono")
            medio_pago_op = input("Opción: ")

            match medio_pago_op:
                case "1":
                    medio_pago = "Débito"
                case "2":
                    medio_pago = "Crédito"
                case "3":
                    medio_pago = "Efectivo"
                case "4":
                    medio_pago = "Bono"
                case _:
                    raise ValueError("Medio de pago no válido.")

            # Diccionario con los datos del cliente
            cliente = {
                "id": nuevo_id,
                "nombre": nombre,
                "correo": correo,
                "telefono": telefono,
                "documento": documento,
                "medio_pago": medio_pago,
            }

            return cliente  # Devuelve el cliente registrado
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            

# === FUNCIÓN PARA MOSTRAR EL MENÚ ===
def mostrar_menu():
    print("\n--- MENÚ DEL RESTAURANTE ---")
    for key, plato in menu.items():
        print(f"{key}. {plato['nombre']} - {plato['descripcion']}")
        for tam, precio in plato["tamaños"].items():
            print(f"   Tamaño: {tam} - Precio: ${precio}")


# === FUNCIÓN PARA REALIZAR EL PEDIDO ===
def realizar_pedido(cliente):
    pedido = []  # Lista para almacenar los ítems del pedido
    while True:
        mostrar_menu()  # Muestra el menú en cada iteración
        opcion = input("Seleccione el número del plato (o 'fin' para terminar): ")
        if opcion.lower() == "fin": 
            break

        if opcion not in menu:
            print("Opción inválida.")
            continue

        plato = menu[opcion] 
        tamaño_ingresado = input("Ingrese el tamaño exacto: ")

        # Validación case-insensitive del tamaño
        tamanos_disponibles = {k.lower(): k for k in plato["tamaños"]}
        tamaño_clave = tamaño_ingresado.lower() 
        if tamaño_clave not in tamanos_disponibles:
            print("Tamaño no válido.")
            continue

        tamaño = tamanos_disponibles[tamaño_clave]  # Recupera el formato correcto del tamaño

        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                raise ValueError
        except:
            print("Cantidad inválida.")
            continue

        precio_unitario = plato["tamaños"][tamaño]
        subtotal = precio_unitario * cantidad

        # Agrega el ítem al pedido
        pedido.append({
            "plato": plato["nombre"],
            "tamaño": tamaño,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

        print(f"Agregado: {cantidad}x {plato['nombre']} {tamaño}  - precio unitario: ${precio_unitario} - Subtotal: ${subtotal}")

    if not pedido:
        print("No se agregó ningún plato.")
        return None

    total = sum(item["subtotal"] for item in pedido)

    # Crea la orden final
    orden = {
        "nro_orden": len(base_datos[cliente["id"]]["ordenes"]) + 1,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "items": pedido,
        "total": total
    }

    print("\n--- PEDIDO COMPLETADO ---")
    print(f"Número de orden: {orden['nro_orden']}")
    print(f"Total a pagar: ${total}")

    return orden  # Retorna la orden generada

# === FUNCIÓN PARA CONSULTAR UN CLIENTE ===
def consultar_cliente():
    try:
        id_buscar = int(input("Ingrese el ID del cliente: "))
        if id_buscar in base_datos:
            datos = base_datos[id_buscar]["datos"]
            print("\n--- DATOS DEL CLIENTE ---")
            for k, v in datos.items():
                print(f"{k.capitalize()}: {v}")
        else:
            print("Cliente no encontrado.")
    except:
        print("ID inválido.")

# === FUNCIÓN PARA CONSULTAR ÓRDENES DE UN CLIENTE ===
def consultar_orden():
    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
        if id_cliente in base_datos:
            ordenes = base_datos[id_cliente]["ordenes"]
            if not ordenes:
                print("Este cliente no tiene órdenes registradas.")
                return
            print(f"\n--- ÓRDENES DEL CLIENTE {id_cliente} ---")
            for orden in ordenes:
                print(f"\nOrden #{orden['nro_orden']} - Fecha: {orden['fecha']}")
                for item in orden["items"]:
                    print(f"  {item['cantidad']}x {item['plato']} ({item['tamaño']}) - ${item['subtotal']}")
                print(f"  TOTAL: ${orden['total']}")
        else:
            print("Cliente no encontrado.")
    except:
        print("ID inválido.")

# === MENÚ PRINCIPAL DE LA APLICACIÓN ===
def main_menu():
    id_contador = 1  # ID incremental para cada cliente

    while True:
        # Menú principal para seleccionar una opción
        print("\n=== MENÚ DE LA MÁQUINA DESPACHADORA ===")
        print("1. Atender nuevo cliente")
        print("2. Consultar cliente")
        print("3. Consultar orden")
        print("4. Mostrar menú")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente = registrar_cliente(id_contador)
            base_datos[id_contador] = {"datos": cliente, "ordenes": []}
            orden = realizar_pedido(cliente)
            if orden:
                base_datos[id_contador]["ordenes"].append(orden)
            id_contador += 1  # Incrementa el ID para el siguiente cliente

        elif opcion == "2":
            consultar_cliente()

        elif opcion == "3":
            consultar_orden()

        elif opcion == "4":
            mostrar_menu()

        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# === INICIO DEL PROGRAMA ===
main_menu()
