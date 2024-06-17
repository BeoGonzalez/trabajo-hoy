flag = True

descSalud=70000
descAFP=120000
liquido=descSalud-descAFP
trabajadores = []
titulos=[]
sueldo=[]

cargos = ["CEO","DESARROLLADOR","ANALISTA DE DATOS"]


def agregarTrabajador():
    nombre=input("Ingrese el nombre y apellido de un trabajador: ")
    trabajadores.append(nombre)
    while flag:
        cargo=input("Ingrese el cargo del trabajador: ")
        if cargo.upper() in cargos:
            titulos.append(cargo)
            break
        else:
            print("Error ingrese un cargo existente")
    while flag:
        try:
            bruto=int(input("Ingrese el sueldo bruto del trabajador: "))
        except ValueError:
            print("ERROR, Ingrese un valor valido.")
        else:
            sueldo.append(bruto)
            break

def mostrarTrabajador():
    print(f"Trabajadores: \n{trabajadores}\nCargo: \n{titulos}\nSueldo bruto: \n{sueldo}")

def imprimir():
    with open('Python/archivos/archivo_nuevo.txt', 'w',encoding='utf-8') as arch:
        tabla=f"Trabajadores: \n{trabajadores}\nCargo: \n{titulos}\nSueldo bruto: \n{sueldo}"
        arch.write(tabla)

