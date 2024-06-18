# Inicialización de la lista de trabajadores
trabajadores = []
# Definición de los cargos disponibles
cargos = ["CEO", "DESARROLLADOR", "ANALISTA DE DATOS"]
descSalud = 70000
descAFP = 120000

# Función para registrar un trabajador
def registrar_trabajador():
    nombre = input("Ingrese el nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO, DESARROLLADOR, ANALISTA DE DATOS): ").upper()
    while cargo not in cargos:
        print("Cargo ingresado no válido. Los cargos válidos son:", cargos)
        cargo = input("Ingrese el cargo del trabajador: ").upper()
    
    while True:
        try:
            sueldo_bruto = int(input("Ingrese el sueldo bruto del trabajador: "))
            break
        except ValueError:
            print("Error. Ingrese un valor numérico para el sueldo bruto.")

    descuento_salud = descSalud
    descuento_afp = descAFP
    liquido_a_pagar = sueldo_bruto - descuento_salud - descuento_afp
    
    # Agregar los datos a la lista de trabajadores
    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "desc_salud": descuento_salud,
        "desc_afp": descuento_afp,
        "liquido_a_pagar": liquido_a_pagar
    }
    trabajadores.append(trabajador)

# Función para listar todos los trabajadores
def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido a pagar: {trabajador['liquido_a_pagar']}")

# Función para imprimir la planilla de sueldos
def imprimir_planilla():
    if not trabajadores:
        print("No hay trabajadores registrados para imprimir la planilla.")
        return
    
    opcion = input("Seleccione una opción:\n1) Imprimir todos los datos.\n2) Imprimir por cargo.\nIngrese su opción: ")
    while opcion not in ['1', '2']:
        print("Opción no válida.")
        opcion = input("Seleccione una opción:\n1) Imprimir todos los datos.\n2) Imprimir por cargo.\nIngrese su opción: ")
    
    if opcion == '1':
        with open('planilla_completa.txt', 'w', encoding='utf-8') as arch:
            arch.write("Planilla de Sueldos:\n")
            for trabajador in trabajadores:
                arch.write(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido a pagar: {trabajador['liquido_a_pagar']}\n")
    
    elif opcion == '2':
        cargo = input("Seleccione el cargo para imprimir (CEO, DESARROLLADOR, ANALISTA DE DATOS): ").upper()
        while cargo not in cargos:
            print("Cargo ingresado no válido. Los cargos válidos son:", cargos)
            cargo = input("Seleccione el cargo para imprimir: ").upper()
        
        with open(f'planilla_{cargo.lower().replace(" ", "_")}.txt', 'w', encoding='utf-8') as arch:
            arch.write(f"Planilla de Sueldos - Cargo {cargo}:\n")
            for trabajador in trabajadores:
                if trabajador['cargo'] == cargo:
                    arch.write(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['desc_salud']}, Desc. AFP: {trabajador['desc_afp']}, Líquido a pagar: {trabajador['liquido_a_pagar']}\n")



