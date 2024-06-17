import funciones as funcion
import time


while True:
    print("\nBienvenido a la empresa\n")
    print("1.- Agregar trabajador.")
    print("2.- Mostrar trabajadores.")
    print("3.- Imprimir planilla de sueldos.")
    print("4.- Salir del programa.\n")
    try:
        opcion=int(input("Ingrese una opción: "))
    except ValueError:
        print("\nError, ingrese un numero del 1 al 4.\n")
    else:
        if (opcion==1):
            funcion.agregarTrabajador()
        elif (opcion==2):
            funcion.mostrarTrabajador()
            print("")
        elif (opcion==3):
            funcion.imprimir()
        elif (opcion==4):
            print("Saliendo del programa...")
            time.sleep(2)
            break
        else:
            print("Ingrese un numero valido..")


