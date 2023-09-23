#Ciclo: Ejecutar una o más tareas/procesos repetidamente/itiradamente

#  FOR (Para)
for i in range(0, 5, 1): # La condición i<5 (No llega hasta 5, es menor)
    print("Hola mundo")

'''Prueba de escritorio
                                Variable        Proceso
                                    i           Imprimir Saludo
                
        Valor inicial               1           Hola mundo
        Valor actual                2           Hola mundo
                                    3           Hola mundo
                                    4           Hola mundo    
        Valor final                 5
    '''
''' range(Inicio, Final, Incremento/Decremento)
        
        El Final, siempre tendra que ser 1 más o 1 menos segun sea el caso''' 

# WHILE (Mientras)
j=1                             #Contador, necesario nombrar la variable para print
while(j <=100):                 #Condición final
    print("Hola mundo")         #Proceso
    j=j+1                       #Incremento j += 2

'''En while en este caso el final si es exacto'''

#Tambien hay ciclos indefinidos, y pueden ser en FOR como en WHILE
respuesta = input("¿Desea continuar? (si/no): ")

while (respuesta =="si"):
    print ("Hola mundo")
    respuesta = input ("¿Desea continuar? (si/no): ")