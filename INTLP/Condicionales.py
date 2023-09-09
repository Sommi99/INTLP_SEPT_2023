# Condicionales

edad = int(input("Escribe tu edad: "))

if (edad >=18 and edad <=110):  #Rango entre 18 y 110
    print("Mayor de edad")
elif (edad >=0 and edad <18):
    print ("Menor de edad")
else: #elif(edad <0 or edad >110)
    print("Edad inválida") #Edad sea menor que 0 o mayor que 110