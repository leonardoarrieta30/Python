def ejercicio1():
    a=float(input("Digite el valor de a: "))
    b=float(input("Digite el valor de b: "))
    c=float(input("Digite el valor de c: "))


    resultado=(a**3 * (b**2 - 2*a*c))/(2*b)

    print(f"El resultado es: {resultado}")

def ejercicio2():
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    resultado= 3+5*8<3 and (((-6/3)*4)+2)<2 or a>b
    print(f"El resultado es: {resultado}")

def ejercicio3():
    a=int(input("Ingrese el valor de a: "))
    b=int(input("Ingrese el valor de b: "))
    aux=a
    a=b
    b=a
    print(f"El nuevo valor de a es: {a}",f" el nuevo valor de b es: {b}")
    
def ejercicio4():
    import math
    r=float(input("Ingrese el valor del radio: "))
    area=math.pi*r**2
    longitud=2*math.pi*r

    print(f"El area del circulo es: {area:.2f}")
    print(f"La longitud del circulo es: {longitud:.2f}")

def ejercicio5():
    totalDeCompra=float(input("Ingrese el total de su compra: "))
    pagoFinal=totalDeCompra*85/100
    print(f"El precio final co el descuento es: {pagoFinal:.2f}")

def ejercicio6():
    a=int(input("Digite el primer numero: "))
    b=int(input("Digite el segundo numero: "))

    if a%2==0 and b%2==0:
        print("Ambos numeros son pares")
    elif a%2==0 and b%2!=0:
        print(f"Solo {a} es par")
    elif a%2!=0 and b%2==0:
        print(f"Solo {b} es par")
    else:print("Ambos numeros son impares")

def ejercicio7():
    a=float(input("Ingrese el valor del primer numero: "))
    b=float(input("Ingrese el valor del segundo numero: "))
    c=float(input("Ingrese el valor del tercer numero: "))
    if a>=b and a>=c:
        print(f"El mayor es {a}")
    elif b>=a and b>=c:
        print(f"El mayor es {b}")
    elif c>=a and c>=a:
        print(f"El mayor es {c}")

def ejercicio8():
    caracter=input("Digite un caracter: ").lower()
    if caracter[0]=='a' or caracter[0]=='e' or caracter[0]=='i' or caracter[0]=='o' or caracter[0]=='u':
        print("La letra ingresada es una vocal")
    else: print("No es una vocal")

def ejercicio9():
    a=float(input("Ingrese el primer numero: "))
    b=float(input("Ingrese el segundo numero: "))
    letra=input("Ingrese la primera letra de la operacion que desea hacer: ")

    if letra[0]=='s' or letra[0]=='S':
        print(a+b)
    elif letra[0]=='r' or letra[0]=='R':
        if a>b:
         print(a-b)
        else: print(b-a)
    elif letra[0]=='p'or letra[0]=='P' or letra[0]=='m' or letra[0]=='M':
        print(a*b)
    elif letra[0]=='D' or letra[0]=='d':
        print(a/b) 
    else: print("Ingreso una opcion incorrecta")

def ejercicio10():
    saldoInicial=1000


    while(1):

        print("\tMenu de Opciones","\n1Ingresar dinero a la cuenta","\n2Retirar dinero de la cuenta")
        print("3Mostrar dinero disponible","\n4Salir")
        opcion=int(input("Ingrese una opcion: "))


        if opcion==1:
            ingreso=float(input("Cuanto dinero desea ingresar a su cuenta: "))
            saldoInicial+=ingreso
        elif opcion==2:
            retiro=float(input("Cuanto dinero desea retirar de su cuenta: "))
            if retiro>saldoInicial:
                print("La cantidad de dinero que desea retirar excede a la de su inicial")
            else:
                saldoInicial-=retiro
        elif opcion==3:
            print(f"Su saldo disponible es {saldoInicial}")
        elif opcion==4:
            return 

# seguimos maniana jugando con listas,tuplas,conjuntos,diccionarios

