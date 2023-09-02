# App finanzas
#La aplicación llevara registro de los movimientos indicando el numero de ingresos y egresos

acumIngresos = 0
acumEgresos = 0
saldo = 0
isOn= int(input("Ingrese 1 para inicializar el servicio: \n"))

while isOn != 0:
  opc = int(input("1. Ingreso:\n 2. Egreso \n 3. Salir \n"))

  if opc == 1:
    ingreso = int(input("Registre el ingreso: \n"))
    saldo = saldo + ingreso
    print(f"Su saldo es ${saldo}")
    acumIngresos+=1
    print(acumIngresos)
  elif opc == 2:
    egreso = int(input("Registre el monto a retirar:\n"))

    saldo = saldo - egreso
    if saldo > 0:
      print("Saldo insuficiente")
      saldo = saldo + egreso
      print(saldo)

    else:
      print(f"Su saldo es ${saldo}")