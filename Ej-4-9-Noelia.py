#Ej. 4.9 Noelia
mano_obra:float
gasto_fabricación:float
costo_producción:float
precio_venta:float
materia_prima=float(input("Ingrese el costo de la materia prima:"))
artículo=int(input("Ingrese el número del artículo:"))
if artículo == 3 or artículo == 4:
    mano_obra = materia_prima * 0.75
else:
    if artículo == 1 or artículo == 5:
        mano_obra = materia_prima * 0.80
    else:
        mano_obra = materia_prima* 0.85 
if artículo == 2 or artículo == 5:
    gasto_fabricación = materia_prima* 0.30
else:
    if artículo == 3 or artículo == 6:
     gasto_fabricación = materia_prima* 0.35
    else:
        gasto_fabricación = materia_prima* 0.28
costo_producción = materia_prima + mano_obra + gasto_fabricación        
precio_venta = costo_producción +(costo_producción *0.45) 
print ("El precio de venta para este artículo es:", precio_venta)
print(materia_prima), print(mano_obra), print(gasto_fabricación), print(costo_producción)