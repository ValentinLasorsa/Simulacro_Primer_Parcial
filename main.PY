import os
#Ejercicio 3 
facturacionTotal=0
contArt1=0
contFacturaCara=0
factura=int(input("Ingrese el número de factura "))
while factura>0:
    articulo=int(input("Ingrese número de artículo "))
    while articulo<=0 or articulo>3:
        articulo=int(input("Ingrese número de artículo válido (entre 1 y 3) "))
    litros=float(input("Ingrese cantidada de litro (L) "))
    if articulo ==1:
        precio=litros*15000
        contArt1+=1
    elif articulo==2:
        precio=litros*25000
    elif articulo==3:
        precio=litros*35000
    if precio >30000:
        contFacturaCara+=1
    facturacionTotal=facturacionTotal+precio
    print("Su factura es de $"+str(precio))
    factura=int(input("Ingrese el número de factura "))
if facturacionTotal==0:
    print("No se ingresaron datos")
else:
    print("La facturación total fue de $"+str(facturacionTotal))
    print("La cantidad vendida del artículo 1 fue:",contArt1)
    print("Las facturas vendidas mayores de $30.000 fue de:",contFacturaCara)
