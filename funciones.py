import variables as va
import funciones as fu
import time

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multip(x, y):
    return x * y

def divid(x, y):
    if y == 0:
        return "No se puede dividir"
    return x / y

def exit():
    return "Agun bai!"


def calculadora():

    while True:

        print(va.msg2)
        time.sleep(1)
        opcion = int(input("Opción: "))

        if opcion == 5:
            print(fu.exit())
            break

        num1 = int(input(va.val1))
        num2 = int(input(va.val2))

        if opcion   == 1:
            resultado = fu.sumar(num1, num2)
            time.sleep(1)
            print(f"El resultado de tu suma es {resultado}")

        elif opcion == 2:
            resultado = fu.restar(num1, num2)
            time.sleep(1)
            print(f"El resultado de tu resta es {resultado}")

        elif opcion == 3:
            resultado = fu.multip(num1, num2)
            time.sleep(1)
            print(f"El resultado de tu multiplicación es {resultado}")
            
        elif opcion == 4:
            resultado = fu.divid(num1, num2)
            time.sleep(1)
            print(f"El resultado de tu división es {resultado}")

        else:
            "Opción no valida."

        
        continue