import time
import csv
from random import*

trabajadores=[
     ["juan perez"],
     ["maria garcia"],
     ["carlos lopez"],
     ["ana martinez"],
     ["pedro rodriguez"],
     ["laura hernandez"],
     ["miguel sanchez"],
     ["isabel gomez"],
     ["francisco diaz"],
     ["elena fernandez"]
]
def sueldos():
    sueldos=randint(300000,2500000)
    sueldo_individual=sueldos
    return sueldo_individual

def asignar_sueldos():
    for trabajador in trabajadores:
        lista_sueldos=[
     ["juan perez", sueldos()],
     ["maria garcia",sueldos()],
     ["carlos lopez",sueldos()],
     ["ana martinez",sueldos()],
     ["pedro rodriguez",sueldos()],
     ["laura hernandez",sueldos()],
     ["miguel sanchez",sueldos()],
     ["isabel gomez",sueldos()],
     ["francisco diaz",sueldos()],
     ["elena fernandez",sueldos()]
     ]

    print(lista_sueldos)

# problema en el .format
"""def clasificar_sueldos():
    menores800=[trabajador for trabajador in lista_sueldos if trabajador[1]<800000]
    entre800y2mill=[trabajador for trabajador in lista_sueldos if trabajador[1]>800000 or trabajador[1]<2000000]
    superiores=[trabajador for trabajador in lista_sueldos if trabajador[1]>2000000]

    totalmenores=(len/menores800)
    totalentre=(len/entre800y2mill)
    totalsuperior=(len/superiores)

    print(f"sueldos menores a $800000 total{totalmenores}")
    titulos=["nombre", "sueldo"]
    print(f"sueldos menores a $800000 total{totalmenores}")
    titulos=["nombre", "sueldo"]
    print(f"{:<20}{:<10}".format(titulos[0],titulos[1]))
    for trabajador in menores800:
        print(f"{:<20}{:<10}".format(trabajador[0],trabajador[1]))

    print(f"sueldos mayores a $800000 y menores a $2000000 total{totalentre}")
    print(f"{:<20}{:<10}".format(titulos))
    for trabajador in totalentre:
        print(f"{:<20}{:<10}".format(trabajador[0],trabajador[1]))

    print(f"sueldos mayores a $2000000 total{totalsuperior}")
    print(f"{:<20}{:<10}".format(titulos))
    for trabajador in totalsuperior:
        print(f"{:<20}{:<10}".format(trabajador[0],trabajador[1]))
    

    total_sueldos=sum(lista_sueldos)
    print(f" TOTAL SUELDOS: {total_sueldos}")"""


def ver_estadisticas():
    producto=1
    sueldobajo=min(lista_sueldos)
    sueldoalto=max(lista_sueldos)
    promedio=(sum(lista_sueldos))/(len(lista_sueldos))
    
    for valor in lista_sueldos:
         producto*= valor  
         media= producto**(1/len(lista_sueldos))

    print(f" el sueldo mas bajo es de ${sueldobajo}")
    print(f"el sueldo mas alto es de ${sueldoalto}")
    print(f" el promedio total de sueldos es de ${promedio}")
    print(f"la media de todos los sueldos es de ${media}")

"""def reporte_sueldos():
    encabezados=["nombre empleado", "sueldo base", "descuento salud", "descuento AFP", "sueldo liquido"]
    print(f"{:<20}{:<20}{:<20}{:<20}{:<20}".format(*encabezados))
     for trabajador in lista_sueldos:
        sueldo_base= trabajador[1]
        descuento_salud= sueldo base*0.93
        descuento_afp= sueldo_base*0.88
        sueldo_liquido= sueldo_base-(descuento_salud+descuento_afp)"""

def reporte_sueldos():
    print("reporte de sueldos")
    with open ("reporte.csv","r", newline="") as archivo:
        lector_csv=csv.DictReader(archivo)
        contenido=lector_csv.DictReader(archivo)
        print(contenido)




            
"""with open ("reporte.csv","w", newline="") as archivo:
    escritor_csv=csv.writer(archivo)
    escritor_csv.writerow(["nombre empleado", "sueldo base", "descuento salud", "descuento AFP", "sueldo liquido"])
    escritor_csv.writerows(
        ["juan perez", sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["maria garcia",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["carlos lopez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["ana martinez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["pedro rodriguez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["laura hernandez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["miguel sanchez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["isabel gomez",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["francisco diaz",sueldos(),sueldos()*0.93,sueldos()*0.88,],
        ["elena fernandez",sueldos(),sueldos()*0.93,sueldos()*0.88,]
        )"""


def salir():
    print("muchas gracias por usar este programa")
    print("finalizando programa")
    print("desarrollado por victoria castillo pino")
    print("seccion: 008D")
    print(" Rut 21.911.212-2 ")
    validar=False
    return validar

def menu():
   print(" menu trabajadores")
   print("1. Asignar sueldos aleatorios")
   print("2. Clasificar sueldos")
   print("3. Ver estadisticas")
   print("4. Reporte de sueldos")
   print("5. Salir del programa")
   validar=True
   while validar:
    try:
        opc=input("ingrese una opcion: ")
    except ValueError:
        print("ingrese un numero valido")
        continue
    if opc=="1":
        asignar_sueldos()
        time.sleep(1)
    elif opc=="2":
        clasificar_sueldos()
        time.sleep(1)
    elif opc=="3":
        ver_estadisticas()
        time.sleep(1)
    elif opc=="4":
        reporte_sueldos()
    elif opc=="5":
        salir()
        break
    else:
        print("opcion invalida")


menu()
