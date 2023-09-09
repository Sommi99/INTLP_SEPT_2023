#Determinar la edad de una persona conociendo el año actual y el de su nacimiento

A_actual = int(input("Ingresa el año curso: "))
A_nacimiento = int(input("Ingresa tu año de nacimiento: "))

Edad = A_actual - A_nacimiento

print("Cuentas con una edad de: ", round(Edad,2))