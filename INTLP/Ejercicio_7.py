# Pedir el nivel de agua en metros de una cisterna

nivel = float(input("Ingrese el valor en metros, referente a su valor del nivel de agua: "))

if nivel > 6:
    print("Desbordamiento de agua en la cisterna")
else: 
    if nivel == 6:
        print("Apagar Bomba")
    else:
        if nivel := float(range(4.1,6,1)):
            print("Desacelerar Bomba")
        else:
            if nivel := float(range(2.1,4,1)):
                print("Bomba trabajando!")
            else:
                if nivel := float(range(0.1,2,1)):
                    print("Acelerar Bomba de Agua")
                else:
                    if nivel == 0:
                        print("Encender Bomba de Agua")
                    else:
                        if nivel < 0:
                            print("Fuga en cisterna")