import math
Radio = float(input('Ingrese el radio del circulo: '))
Area = round(math.pi*(Radio**2), 2)
Longitud = round(math.pi*(Radio*2), 2)
print(f'El Área del circulo es: {Area}\nLa longitud de la circunferencia es: {Longitud}')