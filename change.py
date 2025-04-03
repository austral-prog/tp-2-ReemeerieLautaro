def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    
    print(f"{"Ingresar gastos:"} {expense}")
    print(f"{"Dinero recibido:"} {money}")
    print(int(vuelto))
    print(float(vuelto) - int(vuelto))

change()
