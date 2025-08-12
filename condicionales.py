#if - simple

#if - else 

#civica => si el usuario tieen saldo se le permite ingresar a el sistema
saldo = 5

if saldo > 0:
    print("Bienvenido")
else:
    print("Saldo insuficiente")

#elif

saldo=5000
pasaje=3400

if saldo >= pasaje:
    print("Bienvenido")
    saldo -=  pasaje
elif saldo > 0 and saldo < pasaje:
    print("Bienvenido, saldo pendiente")
    saldo -=  pasaje
    print(f"su nuevo saldo es {saldo}")
else:
    print("Saldo Insuficiente")


#match-case
option = int(input("ingrese una opcion: "))

match option:
    case 1:
        print("viajero frecuente")
    case 2:
        print("viajero ocasional")