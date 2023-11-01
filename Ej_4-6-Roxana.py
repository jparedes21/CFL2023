#ejercicio 4.6 de la pizarra 2
total : float
precio: float
autobus = str(input(" Elija autobus (A) , (B) o (c): "))
kilometros = float (input("ingrese cantidad de kilometros:"))
preciopersona: float
if autobus =="A":
    precio = 2.00
else:
    if autobus== "B":
        precio = 2.50
    else: 
        precio = 3.00
personas = int (input("Ingrese cantidad de personas : "))
if personas >=20:
    total = (precio* kilometros) * personas
else: 
    total = (precio * kilometros) * 20
preciopersona = precio* kilometros
print ("el precio por persona es :", preciopersona)
print ("El total es: ", total)
#fin