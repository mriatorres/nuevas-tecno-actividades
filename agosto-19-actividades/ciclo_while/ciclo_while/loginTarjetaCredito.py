##Juego While
#- Si sale cero pierde una vida
#- Si se genera cualquier otro numero dentro de un rango establecido, gana puntos

vidas = 5
puntos = 0

while vidas !=0:
  import random
  num = random.randint(0,9)

  if num != 0:
    puntos+=1
    print("Tienes ", puntos, " puntos")
  else:
    vidas-=5
    print("Te quedan ", vidas, " vidas")

# Pago tarjeta de credito
#- Recibir por consola el valor de una compra
#- Que se pueda recibir el número de cuotas
#- Calcular el valor de la cuota
#- Usamdo while imprimir el plan de pago y se muestre el cupo liberado con cada pago

print ("~ Pago PSE ~")
valor_neto = float(input("Ingresa el valor total de la compra "))
num_cuotas = int(input("Ingresa el numero de cuotas a diferir "))
valor_cuota = valor_neto / num_cuotas
cuota_actual = 1
saldo_restante = valor_neto
intereses = float(0.05 * valor_neto)
valor_total = float(valor_cuota + intereses)
while cuota_actual <= num_cuotas:
  cuota_actual+=1
  saldo_restante-=valor_cuota
  print("El valor a pagar es: ", valor_cuota, " Numero de cuota: ", cuota_actual, " Intereses: ", intereses, " Valor total a pagar: ", valor_total, " Saldo restante: ", saldo_restante)


# Login y pago tarjeta de credito
#- Login con validación de usuario y contraseña
#- Login con captcha

print("~ PSE ~ ? \n")
opciones = int(input("Opciones \n \n Digite: \n 1 - para registrarse \n 2 - para ingresar \n 3 - para salir\n"))

match opciones:
    case 1:
      new_name = input("Ingrese su nombre ")
      new_phone = input("Ingrese su numero de celular ")
      new_email = input("Ingrese su Email ")
      new_userName = input("Ingrese su nombre de usuario ")
      print("\n El usuario quedo registrado en la plataforma con los siguientes datos: \n", " Nombre: ", new_name, " Celular: ", new_phone, " Email: ", new_email, " Nombre de usuario ", new_userName)

    case 2:
      usuario = "login"
      password = "123"
      user_usuario = input("Ingrese su usuario \n")
      user_pwd = input("Ingrese la contraseña \n")
      if user_pwd != password and user_usuario != usuario:
        print("Las credenciales de ingreso no son correctas... Acceso denegado")

      elif user_usuario == usuario and user_pwd != password:
        print("La contraseña no coincide con el usuario... Acceseo denegado")

      elif user_usuario != usuario and user_pwd == password:
        print("El usuario que ingreso no está registrado... Acceseo denegado")

      elif user_usuario == usuario and user_pwd == password:
        print("Bienvenido", usuario, " Realice el uso de nuestros servicios de pago Online \n")
        print("\n ~ Pago PSE ~")
        valor_neto = float(input("Ingresa el valor total de la compra "))
        num_cuotas = int(input("Ingresa el numero de cuotas a diferir "))
        valor_cuota = valor_neto / num_cuotas
        cuota_actual = 1
        saldo_restante = valor_neto
        intereses = float(0.05 * valor_neto)
        valor_total = float(valor_cuota + intereses)
        while cuota_actual <= num_cuotas:
          cuota_actual+=1
          saldo_restante-=valor_cuota
          print("El valor a pagar es: ", valor_cuota, " Numero de cuota: ", cuota_actual, " Intereses: ", intereses, " Valor total a pagar: ", valor_total, " Saldo restante: ", saldo_restante)

      else:
        print("\n Ingrese datos validos... ")

    case 3:
      print("\n Ha salido de la plataforma... Gracias por usar nuestros servicios")


