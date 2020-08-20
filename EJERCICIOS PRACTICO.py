
def ejercicio1():
    print('-----Ejercicio 1-----')
    print()
    print('Nombre Completo: Ariel De Jesus Perez Hernandez')
    print('Telefono : 829-260-3973')
    print('Correo Electronico : 2016-0394@uteco.edu.do')


def ejercicio2():
    print('-----Ejercicio 2-----')
    print()
    print('Sumar 2 numeros')
    print('Ingreso el primero:')
    num1=int(input())
    print('Ingreso el segundo:')
    num2=int(input())
    print('El Resultado de la suma :'+str(num1+num2))


def ejercicio3():
    print('-----Ejercicio 3-----')
    print()
    precio=750
    itbis =(18*750)/100
    print('Itbis : '+str(itbis))
    print('Precio final : '+str(itbis+precio))


def ejercicio4():
    print('-----Ejercicio 4-----')
    print()
    print('Para determinar cual es el mayor:')
    print('Ingrese un numero')
    num1=int(input())
    print('Ingrese otro')
    num2=int(input())
    if num2==num1:
        print('Ambos numeros son iguales')
    else:
        print('El mayor es '+str(max(num1,num2)))


def  ejercicio5():
    print('-----Ejercicio 5-----')
    print()
    print('Ingrese un numero para determinar si esta entre 0 y 25')
    num=int(input())
    if num>=0 and num<=25:
        print('El numero está entre 0 y 25')
    else:
        print('El numero no está entre 0 y 25')

 

def ejercicio6():
    print('-----Ejercicio 6-----')
    print()
    print('Numeros del 1 al 100 con while:')
    i = 1
    while i<=100:
        print(i)
        i+=1

def ejercicio7():
    print('-----Ejercicio 7-----')
    print()
    print('Numeros del 1 al 100 con for:')
    for x in range(100):
        print(x+1)



def ejercicio8():
    print('-----Ejercicio 8-----')
    print()
    texto='Diplomado de BigData'
    print('El String *Diplomado de BigData* tiene '+str(len(texto))+' Caracteres')


def ejercicio9():
    print('-----Ejercicio 9-----')
    print()
    print('Pares entre 1 y 300')
    for x in range(300):
        if (x+1)%2==0:
            print(x+1)

def ejercicio10():
    print('-----Ejercicio 10-----')
    print()
    print('***Calculadora de prestamos***')
    print()
    print('Ingrese Monto del préstamo')
    monto=float(input())
    print('Ingrese la Tasa de Porcentaje Anual %')
    taza_anual=float(input())
    print('Ingrese el Plazo (en meses)')
    plazo_en_meses=int(input())
    print(plazo_en_meses)
    cuota_mensual=(monto*((taza_anual/100)/12))/(1-pow((1+((taza_anual/100)/12)),(plazo_en_meses*-1)))
    print('La cuota mensual a pagar es de :'+str(round(cuota_mensual,2)))


def imprimirOpciones():
    print('#1. Imprimir en pantalla su Nombre Completo, Telefono & Correo Electronico')
    print('#2. Crear dos variables numericas, sumarlas y mostrar el resultado')
    print('#3. Mostrar el precio del ITBIS de un producto con un valor de 750 y su precio final')
    print('#4. De dos números, saber cual es el mayor')
    print('#5. Crear una variable numerica y si esta entre 0 y 25, mostrar un mensaje indicandolo')
    print('#6. Mostrar con un while los numeros del 1 al 100')
    print('#7. Mostrar con un for los numeros del 1 al 100')
    print('#8. Mostrar los caracteres de la cadena “Diplomado de BigData”')
    print('#9. Mostrar los numeros pares entre 1 al 300')
    print('#10. Realice una calculadora de prestamos e indicarle la cuota a pagar')
    print('#11. Salir')
    

def seleccionar():
    print()
    print('--Seleccione el ejercicio a ejecutar ingresando su numero-- :')
    print()
    imprimirOpciones()
    switcher = {
        '1': ejercicio1,
        '2': ejercicio2,
        '3': ejercicio3,
        '4': ejercicio4,
        '5': ejercicio5,
        '6': ejercicio6,
        '7': ejercicio7,
        '8': ejercicio8,
        '9': ejercicio9,
        '10': ejercicio10,
        '11': exit,
    }
    opcion=input()
    switcher.get(opcion)()
    seleccionar()



seleccionar()



