precio=int
pagoxcita=int
tratamiento=int
n_cita=int(input("Ingrese el numero de cita:"))
if n_cita<=3:
	precio=200
	tratamiento=n_cita*precio
else:
	if n_cita<=5:
		precio=150
		tratamiento=((n_cita-3)*precio)+600
	else:
		if n_cita<=8:
			precio=100
			tratamiento=((n_cita-5)*precio)+900
if n_cita>8:
	precio=50
	tratamiento=((n_cita-8)*precio)+1200
print("El precio de la cita es de:", precio)
print("El total a pagar es de:", tratamiento)