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
def agregar_tarea():
    tarea=input("Ingrese la tarea: ")
    fecha=input("Ingrese la fecha (DD/MM/AAAA): ")
    Total_tareas.append((tarea,fecha))
    print("Tarea agregada exitosamente.")
def eliminar_tarea():
    for x in range(len(Total_tareas)):
        print(f"{x + 1}. {Total_tareas[x][0]} - {Total_tareas[x][1]}")
    try:
        indice=int(input("Ingrese el número de la tarea que desea eliminar: "))
        if indice < 1 or indice > len(Total_tareas):
            print("Error: Índice inválido.")
            return
        Total_tareas.pop(indice - 1)
        print("Tarea eliminada exitosamente.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
def ver_tareas():
    if not Total_tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for x in range(len(Total_tareas)):
            print(f"{x + 1}. {Total_tareas[x][0]} - {Total_tareas[x][1]}")
while True:
  capturar= menu()
  if capturar==1:
         agregar_tarea()
  elif capturar==2:
        eliminar_tarea()
  elif capturar==3:
        ver_tareas()
  elif capturar==4:
        print("Saliendo del programa. ¡Hasta luego!")
        break  


        
    
    