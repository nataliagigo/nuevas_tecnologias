#
# #funciones sin retorno, sin argumentos 
def imprimirUsuario():
    listUsuario = ["andres", "juan", "Maria"]
    print(listUsuario)

imprimirUsuario()
print("----------------")
print("----------------")
imprimirUsuario()
print("----------------")
print("----------------")
imprimirUsuario()


#funciones sin retorno, con argumentos 
listSaldoUsuarios = [5000, -3000, 0]

def imprimirSaldosUsuario(listSaldoUsuarios):
    print(listSaldoUsuarios)

imprimirSaldosUsuario(listSaldoUsuarios)


#funciones con retorno, sin rgumentos
def calcularSaldo():
    saldo = 5000
    viaje = 34000
    saldo -=viaje
    return saldo

print(calcularSaldo())
nuevoSaldo = calcularSaldo()
print(nuevoSaldo)


#funciones con retorno, con argumento
saldo = 5000
viaje = 34000

def calcularSaldo(saldo, viaje):
    saldo -= viaje
    return saldo

print(calcularSaldo(saldo,viaje))
nuevoSaldo = calcularSaldo(saldo, viaje)
print(nuevoSaldo)

