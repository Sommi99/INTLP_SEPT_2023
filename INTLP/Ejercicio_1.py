#Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

Calificacion_1 = float(input("Inserta la primera calificación: "))
Calificacion_2 = float(input("Inserta la segunda calificación: "))
Calificacion_3 = float(input("Inserta la tercer calificación: "))

sumatoria = Calificacion_1 + Calificacion_2 + Calificacion_3
promedio = sumatoria/3

print("El promedio de sus calificaciones es de: ", round(promedio,2))