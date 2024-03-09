#compra ejercicio
precio = int(input("valor compra "))

balotaRoja = (precio*10) /100
balotaVerde = (precio*15) /100
balotaAzul = (precio*20) /100
balotaAmarilla = (precio*50) /100
balotaNegra = (precio*100) /100

if precio > 50000: 
    balota = input(" que balota saco ")
    if balota == "roja":
        print(f"su descuento es {balotaRoja}")
    elif balota == "verde":
        print(f"su descuento es de {balotaVerde}")
    elif balota == "azul":
        print(f"su descuento es de {balotaAzul}")
    elif balota == "amarilla":
        print(f"su descuento es de {balotaAmarilla}")
    elif balota == "negra":
        print(f"su descuento es de {balotaNegra}")
else: print("no tiene descuento")


