import os
#Ejercicio 1
suma=0
sueldoMayor1500=0
prom=0
for j in range (15):
    ganancia=0
    ganancia=int(input("Ingrese su sueldo "))
    if ganancia>1500:
        sueldoMayor1500+=1
    suma=suma+ganancia
prom=suma/15
print("El promedio de sueldos es:",prom)
print("La cantidad de sueldos mayor a 1500 es:",sueldoMayor1500)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#Ejercicio 2 
contMenor15=0
contMayor50=0
contEntre25y45=0
porcMenores15=0
porcMayores50=0
contTotal=0
num=int(input("Ingrese número "))
while num !=0:
    contTotal+=1
    if num<15:
        contMenor15+=1
    elif num >50:
        contMayor50+=1
    elif num>25 and num<45:
        contEntre25y45+=1
    num=int(input("Ingrese otro número "))
porcMenores15=(contMenor15*100)/contTotal
porcMayores50=(contMayor50*100)/contTotal
print("El porcentaje menor de 15 fue "+str(porcMenores15)+"% El porcentaje mayor a 50 fue "+str(porcMayores50)+"% y la cantidad de número ingresados entre 25 7 45 fue:",contEntre25y45)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

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
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#Ejercicio 4
cantCateg1=0
cantCateg2=0
cantCateg3=0
tSueldoCateg1=0
tSueldoCateg2=0
tSueldoCateg3=0
tSueldo=0
promSueldo=0
for y in range (50):
    sueldo=0
    categoria=int(input("Ingrese su categoría "))
    while categoria <=0 or categoria>3:
        categoria=int(input("Ingrese categoría válida "))
    años=int(input("Ingrese la cantidad de años que lleva en la empresa "))
    while años <0:
        años=int(input("Ingrese la cantidad de años que lleva en la empresa correctamente "))
    if categoria ==1:
            sueldo=200000+años*3000
            cantCateg1+=1
            tSueldoCateg1=tSueldoCateg1+sueldo
            tSueldo=tSueldo+sueldo
            print("Le corresponde $"+str(sueldo))
    elif categoria==2:
            sueldo=250000+años*3000
            cantCateg2+=1
            tSueldoCateg2=tSueldoCateg2+sueldo
            tSueldo=tSueldo+sueldo
            print("Le corresponde $"+str(sueldo))
    elif categoria==3:
            sueldo=300000+años*3000
            cantCateg3+=1
            tSueldoCateg3=tSueldoCateg3+sueldo
            tSueldo=tSueldo+sueldo
            print("Le corresponde $"+str(sueldo))
promSueldo=tSueldo/50
print("Cantidad de empleados: Categoría 1:",cantCateg1,"Empleado/s", "Categoría 2:",cantCateg2,"Empleado/s", "Categoría 3:",cantCateg3,"Empleado/s")
print("Total de sueldo por categoría: Categoría 1:$"+str(tSueldoCateg1), "Categoría 2:$"+str(tSueldoCateg2), "Categoría 3:$"+str(tSueldoCateg3))
print("Sueldo promedio es:",promSueldo)
input("\033[1mPresione enter para finalizar\033[0m")
os.system('cls')
