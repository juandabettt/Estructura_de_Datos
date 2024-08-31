print (" Ingresa temperatura en celcius ")

def celciustemp (celsuis):
    return (celsuis*9/5)+ 32

celsuis = float(input(" Ingrese la temperatura en celsius "))

resultado= celciustemp (celsuis)
print (" La temperatura en fahrenheit es", resultado )