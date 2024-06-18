#Trabajo de Martín Díaz, Benjamín González y Vicente Ruiz
import funciones as funcion
import time

trabajadores = []
while True:
    print("\n----- Menú Principal -----")
    print("1) Registrar trabajador")
    print("2) Listar todos los trabajadores")
    print("3) Imprimir planilla de sueldos")
    print("4) Salir del programa")
        
    opcion = input("Seleccione una opción: ")
        
    if opcion == '1':
        funcion.registrar_trabajador()
    elif opcion == '2':
        funcion.listar_trabajadores()
    elif opcion == '3':
        funcion.imprimir_planilla()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor seleccione una opción del menú.")
