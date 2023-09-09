# Pedir el nivel de agua en metros de una cisterna

nivel = float(input("Ingrese el valor en metros, referente a su valor del nivel de agua: "))

if (nivel >6):
    print("Desbordamiento de agua en la cisterna")
elif (nivel == 6):
    print("Apagar Bomba")
elif (nivel >=4 and nivel <6):
    print("Desacelerar Bomba")
elif (nivel >=2 and nivel <4):
    print("Bomba trabajando!")
elif (nivel >0 and nivel <2):
    print("Acelerar Bomba de Agua")
elif (nivel == 0):
    print("Encender Bomba de Agua")
elif (nivel < 0):
     print("Fuga en cisterna")