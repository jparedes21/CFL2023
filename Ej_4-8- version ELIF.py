# Ej.4.8-consultorio versión ELIF
precio:int
pagoxcita:int
pagoxtratamiento:int
nro_cita = int(input("Ingrese número de cita:"))
if nro_cita <=3:
    precio=200
    pagoxtratamiento=nro_cita*precio
elif nro_cita <=5:
        precio=150
        pagoxtratamiento=((nro_cita - 3)*precio)+600
elif nro_cita <=8:
        precio = 100
        pagoxtratamiento=((nro_cita - 5)*precio)+900
else:
        precio = 50
        pagoxtratamiento=((nro_cita - 8)*precio)+1200
print ("El pago por cita es:", precio)
print ("El pago del tratamiento es:", pagoxtratamiento)
