def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    
    print(f"{"Ingresar gastos:"} \n{expense}")
    print(f"{"Dinero recibido:"} \n{money}")
    print ("Vuelto")
    print(f"{"Pesos:"} \n{int(vuelto)}")
    print(f"{"Centavos:"} \n{float(vuelto) - int(vuelto)}")

change()
