print ("escribe dos numeros maximo")

def operaciones_chill (xd1, xd2, operacion): 
    if operacion == "suma":
        return xd1+xd2
    elif operacion == "resta":
        return xd1-xd2
    elif operacion == "multiplicacion":
        return xd1*xd2
    elif operacion == "division":
        if xd2 == 0 :
            return " no se puede dividir por 0 "
        return xd1/xd2
    else : 
        print (" no se puede realizar la operacion ")


xd1= float (input(" ingrese numero :"))
xd2= float (input(" ingrese numero: "))   
operacion= (input(" Operacion a realizar: "))  

resultado = operaciones_chill (xd1, xd2, operacion)

print (" el resultado es", resultado)



