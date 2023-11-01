preciov:float
manobra:float
manobra=1.0
costoprod:float
gastos:float
gastos=0
art=int(input("Ingrese el numero del articulo:"))
mpri=float(input("ingrese el costo de la materia prima:"))
if art==(3,4):
	manobra=mpri*1.75
if art==(1,5):
	manobra=mpri*1.80
if art==(2,6):
	manobra=mpri*1.85
if art==(2,5):
	gastos=mpri*1.30
if art==(3,6):
	gastos=mpri*1.35
if art==(1,4):
	gastos=mpri*1.28
#print(gastos)
#print(mpri)
costoprod=mpri + manobra + gastos
preciov=costoprod*1.45
print("El precio de venta es de:", preciov)
print("El costo de produccion es de:", costoprod)