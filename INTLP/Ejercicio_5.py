#Obtener valores para a, b y c para la formula general

import math

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

x1 = (-b - math.sqrt((pow(b,2)) - (4*a*c)))/2*a
x2 = (-b + math.sqrt((pow(b,2)) - (4*a*c)))/2*a

print("El valor de X1 es de: ", round(x1, 4))
print("El valor de X2 es de: ", round(x2, 4))