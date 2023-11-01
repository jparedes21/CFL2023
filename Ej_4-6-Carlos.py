# Ejercicio 4-6
COSTO=float
BUS=str(input("TIPO DE AUTOBUS (A, B o c): "))
KM=float(input("CANTIDAD DE KILOMETROS: "))
if BUS=="A":
    COSTO=2.00
else:
    if BUS=="B":
        COSTO=2.50
    else: 
        COSTO=3.00
PASAJEROS=int(input("CANTIDAD DE PASAJEROS: "))
if PASAJEROS>=20:
    TOTAL=float(COSTO*KM)*PASAJEROS
else: 
    TOTAL=(COSTO*KM)*20
VALORXPERS:float=COSTO*KM
print ("COSTO UNITARIO: ", VALORXPERS)
print ("COSTO TOTAL: ", TOTAL)