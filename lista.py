Total_tareas=[]
def  menu():
    print("Menú de opciones")
    print("---------------------")
    print("1. Agregar tarea y fecha")
    print("2. Eliminar tarea")
    print("3. Ver lista de tareas")
    print("4. Salir")
    print("---------------------")
    try:
      opcion=int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("Error: Debe ingresar un número entero entre 1 y 4.")
        return menu()
    else:
        if opcion < 1 or opcion > 4:
            print("Error: Opción inválida. Por favor, seleccione una opción entre 1 y 4.")
            return menu()
        return opcion
capturar= menu()




        
    
    