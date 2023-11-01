#ej 4.7
#definicion de variables
impuesto:float
total:float
#leo el teclado
hamburguesa=str(input("ingrese el tipo de hamburguesa "))
cantidad=int(input("ingrese la cantidad de hamburguesas "))
pago=str(input("ingrese la forma de pago "))
if hamburguesa=="sencillo":
    precio=20
else:
    if hamburguesa=="doble":
        precio=25
    else:
        precio=28
if pago=="tarjeta":
    impuesto=1.05
else:
    impuesto=1
pago=(cantidad*precio)*impuesto
print("su total a pagar es ",pago)