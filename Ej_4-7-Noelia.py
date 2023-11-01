# Ej 4-7 Hamburguesas
# Define variables
total_pago: float
impuesto: float
precio:int
# Lee el teclado
tipo_hamb=str(input("Ingrese tipo de hamburguesa, A (simple), B (doble) , C (triple):"))
tipo_pago=int(input("Ingrese tipo de pago, 1 si es crédito, 2 para otro tipo de pago:"))
cant_hamb=int(input("Ingrese cantidad de hamburguesa:"))
# Bloque IF
if tipo_hamb == "A":
    precio = 20
else:
    if tipo_hamb == "B":
        precio = 25
    else:
        precio = 28 
if tipo_pago == 1:
     impuesto = 1.08
else:
    impuesto = 1
# Cálculos
total_pago=(cant_hamb*precio)*impuesto
print ("El pago total es:", total_pago)