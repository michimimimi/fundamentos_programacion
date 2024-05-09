#menu principal
menu= int(input("Menu principal: \n 1-Pikachu roll $4500 \n 2-Otaku roll $5000 \n 3-Pulpo venenoso roll $5200 \n 4-Anguila electrica roll $4800 \n 0-Salir \n"))
while menu!=0:
        
    if menu==1:
        print("usted lleva un Pikachu roll")
    elif menu== 2:
        print("usted lleva un Otaku roll")
    elif menu ==3:
        print("usted lleva un pulpo venenoso roll")
    elif menu==4:
        print("usted lleva un Anguila electrica roll")
    else:
        print ("ingresa una opcion")
        break
    
op1=str(1)
op2=str(2)
op3=str(3)
op4=str(4)
total_productos=(str(op1 , op2 , op3 , op4))

#volver al menu principal
menu= int(input("Menu principal: \n 1-Pikachu roll $4500 \n 2-Otaku roll $5000 \n 3-Pulpo venenoso roll $5200 \n 4-Anguila electrica roll $4800 \n"))

#codigo descuento
cod=input("Tiene un cupon de descuento?: ")

if cod==("soyotaku"):
    print("usted tiene un 10% de descuento")
else:
    print("codigo no valido")

#volver al menu principal
cod=input("Reingrese el codigo o vuelva al menu presionando X: ")
volver=(str("X"))
menu= int(input("Menu principal: \n 1-Pikachu roll $4500 \n 2-Otaku roll $5000 \n 3-Pulpo venenoso roll $5200 \n 4-Anguila electrica roll $4800 \n 0-Salir \n"))

#detalle del pedido

print(total_productos)




