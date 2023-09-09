#Con condiciones
Valor = float(input("Ingresa el número de grados: "))
c = input("Tu número se encuentra en grados Celcius: ")

if c == "si":
    f_1 = ((9*Valor)/5) + 32
    k_1 = Valor + 273.15 
    print("Tu valor en grados Kelvin es de: ", round(k_1, 4))
    print("Tu valor en grados Farenheit es de: ", round(f_1, 4))
else:
    f = input("Tu valor se encuentra en grados Fareinheit: ")
    if f == "si":
        c_2 = ((5*(Valor-32))/9)
        k_2 = c_2 + 273.15
        print("Tu valor en grados Celsius es de: ", round(c_2, 4))
        print("Tu valor en grados Kelvin es de: ", round(k_2, 4))
    else:
        c_3 = Valor - 273.15
        f_3 = ((9*(Valor - 273.15))/5)+32
        print("Tu valor en grados Celsius es de: ", round(c_3, 4))
        print("Tu valor en grados Farenheit es de: ", round(f_3, 4))