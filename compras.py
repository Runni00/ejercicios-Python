#compra ejercicio
import random

precio = int(input("valor compra "))

balotaRoja = (precio*10) /100
balotaVerde = (precio*15) /100
balotaAzul = (precio*20) /100
balotaAmarilla = (precio*50) /100
balotaNegra = (precio*100) /100

aleatorio = random.choice(["roja", "verde", "azul", "amarilla", "negra"])

while precio > 50000: 

    if aleatorio == "roja":
        print(f"su descuento es {balotaRoja}")
        print(f"color de la balota es {aleatorio}")
        print(precio - balotaRoja)
    elif aleatorio == "verde":
        print(f"su descuento es de {balotaVerde}")
        print(f"color de la balota es {aleatorio}")
        print(precio - balotaVerde)
    elif aleatorio == "azul":
        print(f"su descuento es de {balotaAzul}")
        print(f"color de la balota es {aleatorio}")
        print(precio - balotaAzul)
    elif aleatorio == "amarilla":
        print(f"su descuento es de {balotaAmarilla}")
        print(f"color de la balota es {aleatorio}")
        print(precio - balotaAmarilla)
    elif aleatorio == "negra":
        print(f"su descuento es de {balotaNegra}")
        print(f"color de la balota es {aleatorio}")
        print(precio - balotaNegra)

        
    question = input('desea seguir con la app ')
    
    if( question == 'no'):
        break
    
else: print("no tiene descuento")


