
valor_compra=int(input("ingresar el valor de la compra"))
descuento=0


if valor_compra==0:
    print("no genera pago")
elif valor_compra==50000:
    descuento=valor_compra-(valor_compra*0.07)
    print("el valor de la compra es de $",valor_compra," se le aplica un descuento del ""7%"" dando un total a pagar $",descuento)
elif valor_compra>50000:
    descuento=valor_compra-(valor_compra*0.10)
    print("el valor de la compra es de $",valor_compra,"se le aplica un descuento del ""10%"" dando un total a pagar de $",descuento)
elif valor_compra<50000:
    descuento=valor_compra-(valor_compra*0.05)
    print("el valor de la compra es de $", valor_compra," se le aplica el descuento del ""5%"" dando un total a pagar $",descuento)