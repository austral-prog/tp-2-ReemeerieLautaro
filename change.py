def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    
    print(f"{"Ingresar gastos:"} \n{expense}")
    print(f"{"Dinero recibido:"} \n{money}")
    print ("")
    print ("Vuelto")
    print("")
    print(f"{"Pesos:"} \n{int(vuelto)}")
    print("Centavos:")
    vuelto_centavos = str(vuelto).split(".")[1]
    print(vuelto_centavos)


change()
