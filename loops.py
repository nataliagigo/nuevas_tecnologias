# Queremos que la máquina de consulta funcione 
# para que distintos clientes al ingresar
#  la tarjeta le diga el tipo de viajero que es.

init = int(input("1. iniciar maquina \n0. Apagar\n"))

while init != 0:

    opt = int(input("1. Seleccione  \n2.Validar tipo viajero  \n3. Salir\n")) 

    match opt:
        case 1: 
            print("Validar tipo viajero")
            
            option = int(input("Caso: "))   

            match option:
                case 1:
                    print('Viajero frecuente')
                case 2:
                    print('Viajero Ocasional')
                case 3:
                    print('Estudiante')
                case 4:
                    print('Tercera Edad')
                case 5:
                    print('Viajero Eventual') 
                case _:
                    print('Ingrese un caso válido') 
        case 2: 
            print("Cerrar Sistema")
            init = 0
        case _: 
            print("Ingrese una opción valida")
            init = 0


 #   if option != 0:
   
       
#    else: 
#        print("Cerrando Sitema") 
#        init = 0  









#Es muy imortante la identacion.
#Bug: comportamiento inesperado