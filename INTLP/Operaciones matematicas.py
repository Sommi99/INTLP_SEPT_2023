#Ejemplo 2. Operaciones matemáticas

#Importar librerias o bibliotecas o funciones matemáticas
import math #Para identificar las librerias es desde la página de python

#Entrada de datos
#Declarar o crear variables intentando que sean las mas descriptivas posibles
numero_1 = float (input("Ingresa tu primer valor: ")) #int numero_1 = 585
número_2 = float (input("Ingresa tu segundo valor: ")) #float número_2= 49.76

#Declarar o crear constantes
PI = 3.1416 #Se utilizan mayúsculas

#Procesos (Cálculo u operaciones matemáticas y/o logicas)
suma = numero_1 + número_2
resta = numero_1 - número_2
multiplicación = numero_1*número_2
división = numero_1/número_2

potencia_1 = numero_1 ** número_2
potencia_2 = pow(numero_1,número_2)
cuadrado = numero_1**2
cubo = pow(número_2,3)

raíz_cuadrada_1 = math.sqrt (9)
raíz_cuadrada_1 = pow(9,1/2)
raíz_cúbica = pow(27,1/3)

modulo_residuo = numero_1 % número_2

#Salida de datos (Imprimir o mostrar resultados en pantalla)
print("Suma =", round(suma,2))
print("Resta =", round(resta,2))
print("Multiplicación =", round(multiplicación,2))
print("División =", round(división,2))
print("Potencia 1 =", round(potencia_1,2))
print("Potencia_2", round(potencia_2,2))
print("Cuadrado =", round(cuadrado,2))
print("Cubo =", round(cubo,2))
print("Raiz cuadrada =", round(raíz_cuadrada_1,2))
print("Raíz cúbica =", round(raíz_cúbica,2))
print("Módulo/Residuo =", round(modulo_residuo,2))