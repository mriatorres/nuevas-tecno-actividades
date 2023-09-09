print("=========== Encicla - Rentas de bicicletas =======\n\n")

opciones = int(input("""Digite:
                     1- para registrarse 
                     2 - para salir\n"""))

match opciones:
    case 1: 
        new_name = input("Ingrese su nombre ")
        new_phone = input("Ingrese su numero de celular ")
        new_email = input("Ingrese su Email ")
        new_id = int(input("Ingrese su numero de documento "))
        print("\n El usuario quedo registrado en la plataforma con los siguientes datos: \n", " Nombre: ", new_name, " Celular: ", new_phone, " Email: ", new_email, " Numero de documento ", new_id)
        usuarioRegistrado = []
        usuarioRegistrado.extend([new_name, new_phone, new_email, new_id])
         
        menu =  int(input("""\nDigite:
                          1 - Para rentar una bicicleta
                          2 - Para salir\n"""))
        
        match menu:
            case 1:
                bicicletasDisponibles = ["1 : Bicicleta Roja", "2 : Bicicleta Verde"]
                print()
                validar_id = int(input("Ingrese su numero de documento\n"))
                if validar_id in usuarioRegistrado:
                    print("Bicicletas disponibles  \n")
                    print(*bicicletasDisponibles, sep = "\n")
                    bicicletaARentar = int(input("Digite el numero de la bicicleta que desea rentar\n"))
                    match bicicletaARentar:
                        case 1:
                            bicletaSeleccionada = bicicletasDisponibles[0]
                            print("Para continuar con el proceso de renta suministre la siguiente información: \n")
                            origen = input("Ingrese el destino de origen de la bicicleta: \n")
                            destino = input("Ingrese el destino final de la bicicleta: \n")
                            bicicletaRentada = []
                            bicicletaRentada.extend([validar_id,bicletaSeleccionada, origen, destino])
                            print("La renta fue exitosa y se registro con los siguientes datos: \n")
                            print(*bicicletaRentada, sep = "\n")
                            del bicicletasDisponibles[0]
                            menuFinal = int(input("""Digite:
                                                  1- Para ver sus prestamos
                                                  2 - Para ver bicicletas disponibles
                                                  3 - Para salir \n"""))
                            match  menuFinal:
                                case 1:
                                    print("Sus prestamos: \n")
                                    print(*bicicletaRentada, sep = "\n")
                                    print("Gracias por utilizar nuestros servicios~~ \n")
                                
                                case 2:
                                    print("Las bicicletas disponibles son: \n")
                                    print(*bicicletasDisponibles, sep = "\n")
                                    
                                case 3:
                                    print("Gracias por utilizar nuestros servicios~~ \n")
                        
                        case 2:
                            bicletaSeleccionada = bicicletasDisponibles[1]
                            print("Para continuar con el proceso de renta suministre la siguiente información: \n")
                            origen = input("Ingrese el destino de origen de la bicicleta: \n")
                            destino = input("Ingrese el destino final de la bicicleta: \n")
                            bicicletaRentada = []
                            bicicletaRentada.extend([validar_id,bicletaSeleccionada, origen, destino])
                            print("La renta fue exitosa y se registro con los siguientes datos: \n")
                            print(*bicicletaRentada, sep = "\n")
                            del bicicletasDisponibles[1]
                            menuFinal = int(input("""Digite:
                                                  1- Para ver sus prestamos
                                                  2 - Para ver bicicletas disponibles
                                                  3 - Para salir \n"""))
                            match  menuFinal:
                                case 1:
                                    print("Sus prestamos: \n")
                                    print(*bicicletaRentada, sep = "\n")
                                    print("Gracias por utilizar nuestros servicios~~ \n")
                                
                                case 2:
                                    print("Las bicicletas disponibles son: \n")
                                    print(*bicicletasDisponibles, sep = "\n")
                                    
                                case 3:
                                    print("Gracias por utilizar nuestros servicios~~ \n")

            
            case 2:
                print("Gracias por utilizar nuestros servicios~~ \n")
    
    case 2:
        print("Gracias por utilizar nuestros servicios~~ \n")                  
                            
                            
                            
                            
                    
                    
