import numpy as np
import math

def obtener_termino_estabilidad():
    sumatoria_doble = obtener_sumatoria_doble()
    sumatoria_simple = obtener_sumatoria_simple()
    digitos_simple = obtener_digitos_simple_decimal()
    mu_simple = 0.5 * ( 10 ** (np.float32(1) - digitos_simple) )
    x = math.fabs( sumatoria_doble - sumatoria_simple )
    y = math.fabs( sumatoria_doble )
    z = y * mu_simple
    te = x / z
    print( "El termino de estabilidad con una variante del algoritmo es: {}".format(te) )

def obtener_sumatoria_doble():
    x = np.float64( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    lista_auxiliar = []

    for i in range(25, 0, -1):
        y = np.float64( (-1 / 4) ** i )
        v = factorizar_doble(x, i, 2 * i)
        k = np.float64( y * v )
        lista_auxiliar.append( np.float64(k) )

    return obtener_suma_doble(lista_auxiliar)

def obtener_sumatoria_simple():
    x = np.float32( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    lista_auxiliar = []

    for i in range(25, 0, -1):
        y = np.float32( (-1 / 4) ** i )
        v = factorizar_simple( x, i, 2 * i)
        k = np.float32( y * v )
        lista_auxiliar.append( np.float32(k) )

    return obtener_suma_simple(lista_auxiliar)

def obtener_suma_simple(lista):
    if len(lista) < 2:
        return lista[0]

    lista_auxiliar = []

    for i in range(0, len(lista), 2):
        try:
            lista_auxiliar.append( np.float32(lista[i] + lista[i + 1]) )
        except IndexError:
            lista_auxiliar.append( np.float32(lista[i]) )

    return obtener_suma_simple(lista_auxiliar)

def obtener_suma_doble(lista):
    if len(lista) < 2:
        return lista[0]

    lista_auxiliar = []

    for i in range(0, len(lista), 2):
        try:
            lista_auxiliar.append( np.float64(lista[i] + lista[i + 1]) )
        except IndexError:
            lista_auxiliar.append( np.float64(lista[i]) )

    return obtener_suma_doble(lista_auxiliar)

def factorizar_simple(x, y, potencia):
    cociente = np.float32(1)
    i = y
    k = potencia

    while i > 0:
        divisor = np.float32(i ** 2)
        z = np.float32(x / divisor)
        cociente = np.float32(cociente * z)
        i -= 1
        k -= 1

    x = np.float32(x ** k)
    cociente = np.float32(cociente * x)
    return cociente

def factorizar_doble(x, y, potencia):
    cociente = np.float64(1)
    i = y
    k = potencia

    while i > 0:
        divisor = np.float64(i ** 2)
        z = np.float64(x / divisor)
        cociente = np.float64(cociente * z)
        i -= 1
        k -= 1

    x = np.float64(x ** k)
    cociente = np.float64(cociente * x)
    return cociente

def obtener_digitos_simple_decimal():
    s = np.float32(1)
    t = np.float32(1)
    x = np.float32(2)

    while x > np.float32(1):
        t += np.float32(1)
        s /= np.float32(10)
        x = np.float32(1) + s

    return t - np.float32(1)

obtener_termino_estabilidad()
