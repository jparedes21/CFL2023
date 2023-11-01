CLAVE=int(input("INGRESE CLAVE DE PRODUCTO (1 AL 6): "))
MATPRI=float(input("INGRESE COSTO DE MATERIA PRIMA: "))
if CLAVE=="1":
   MANOBRA=float((MATPRI*80)/100)
   GASFAB=float((MATPRI*28)/100)
else:
    if CLAVE=="2":
       MANOBRA=((MATPRI*85)/100)
       GASFAB=((MATPRI*30)/100)
    else:
        if CLAVE=="3":
           MANOBRA=((MATPRI*75)/100)
           GASFAB=((MATPRI*35)/100)
        else:
            if CLAVE=="4":
                MANOBRA=((MATPRI*75)/100)
                GASFAB=((MATPRI*28)/100)
            else:
                if CLAVE=="5":
                    MANOBRA=((MATPRI*80)/100)
                    GASFAB=((MATPRI*30)/100)
                else:
                    MANOBRA=((MATPRI*85)/100)
                    GASFAB=((MATPRI*35)/100)
COSPROD=float(MATPRI+MANOBRA+GASFAB)
PREVEN=float(COSPROD*1.45)
print ("COSTO DE PRODUCCIÓN: ", COSPROD)
print ("COSTO DE MANO DE OBRA: ", MANOBRA)
print ("GASTOS DE FABRICACIÓN: ", GASFAB)
print ("PRECIO DE VENTA: ", PREVEN)