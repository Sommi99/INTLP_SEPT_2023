j= float(input("Inserta un número: "))

if(j < 0 and j > -100):
    for i in range (-1,-100,-2):
        print(i)

elif(j > 0 and j < 100):
    k=2
    while(k <= 98):
        print(k)
        k = k + 2

else:
    print("Número invalido")