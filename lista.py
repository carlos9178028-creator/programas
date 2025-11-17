Total_tareas=[]
while True:
    tareas=[]
    print("Menú de opciones")
    print("---------------------")
    print("1. Agregar tarea y fecha")
    print("2. Eliminar tarea")
    print("3. Ver lista de tareas")
    print("4. Salir")
    try:
        rpta=int(input("Elige una de las 4 opciones:"))
    except ValueError:
        print("Error: Debes ingresar un número del 1 al 4")
        continue
    else:
        if rpta==1:
            print("AGREGAR TAREA")
            deberes=input("Ingrese la actividad programada:")
            tareas.append(deberes)
            hora=input("Agrega la hora de la actividad:")
            tareas.append(hora)        
            Total_tareas.append(tareas)
        elif rpta==2:
             print("\n------------------------")
             print("LISTAS DE TAREAS")
             print("TAREA------->HORA")
             for x in range(len(Total_tareas)):
                print(f"{x+1}.- {Total_tareas[x][0]} ----> {Total_tareas[x][1]}")
             try:
                eliminar=int(input("EScoge que tarea deseas eliminar:"))
             except ValueError:
                    print("Error: Debes ingresar un número válido.")
                    continue
             else: 
                   for y in range(len(Total_tareas)):
                     if y==(eliminar-1):
                       del Total_tareas[y]
             print(Total_tareas)
        elif rpta==3:
             print("-----------------------------------------")
             for x in range(len(Total_tareas)):
                print(f"{x+1}.- {Total_tareas[x][0]} ----> {Total_tareas[x][1]}")
        else:
            break


        
    
    