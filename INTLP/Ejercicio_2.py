#Calcular el área y perímetro de un circulo

import math

PI = 3.1416
Radio = float(input("Ingresa el radio de tu circulo: "))

Perimetro = 2 * PI * Radio
Cuadrado = pow(Radio, 2)
Area = PI * Cuadrado

print("El perimetro del circulo es de ", round(Perimetro, 4))
print("El área de este es de ", round(Area, 4))
