import numpy as np
import math
from mostrar import mostrar

def obtener_sumatoria(x, n):
    suma = 0

    for i in range(1, n + 1):
        y = (-1 / 4) ** i
        z = x ** (2 * i)
        u = ( math.factorial(i) ) ** 2
        v = z / u
        k = y * v
        suma += k

    return suma

def obtener_termino_estabilidad():
    sumatoria_doble = obtener_sumatoria_doble()
    sumatoria_simple = obtener_sumatoria_simple()
    digitos_simple = obtener_digitos_simple_decimal()
    mu_simple = 0.5 * ( 10 ** (np.float32(1) - digitos_simple) )
    x = math.fabs( sumatoria_doble - sumatoria_simple )
    y = math.fabs( sumatoria_doble )
    z = y * mu_simple
    te = x / z

    return te, mu_simple

def obtener_sumatoria_doble():
    x = np.float64( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    suma = np.float64(0)

    for i in range(1, 25 + 1):
        y = np.float64( (-1 / 4) ** i )
        z = np.float64( x ** (2 * i) )
        u = np.float64( ( math.factorial(i) ) ** 2 )
        v = np.float64( z / u )
        k = np.float64( y * v )
        suma += np.float64(k)

    return suma

def obtener_sumatoria_simple():
    x = np.float32( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    suma = np.float32(0)

    for i in range(1, 25 + 1):
        y = np.float32( (-1 / 4) ** i )

        if i > 18: #con i >= 19 explota si no hacemos asi
            v = factorizar(x, i, 2 * i)

        else:
            z = np.float32( x ** (2 * i) )
            u = np.float32( ( math.factorial(i) ) ** 2 )
            v = np.float32( z / u )

        k = np.float32( y * v )
        suma = np.float32(suma + k)

    return suma

def factorizar(x, y, potencia):
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

def obtener_digitos_simple_decimal():
    s = np.float32(1)
    t = np.float32(1)
    x = np.float32(2)

    while x > np.float32(1):
        t += np.float32(1)
        s /= np.float32(10)
        x = np.float32(1) + s

    return t - np.float32(1)

def obtener_condicion_problema():
    x = 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) )
    perturbacion = 0.1
    lista_cp_perturbaciones_positivas = []
    lista_cp_perturbaciones_negativas = []
    lista_perturbaciones_positivas = []
    lista_perturbaciones_negativas = []

    for i in range(15):
        cp1 = obtener_cp_con_perturbacion(x, perturbacion)
        cp2 = obtener_cp_con_perturbacion(x, -perturbacion)
        lista_perturbaciones_positivas.append(perturbacion)
        lista_perturbaciones_negativas.append(-perturbacion)
        lista_cp_perturbaciones_positivas.append(cp1)
        lista_cp_perturbaciones_negativas.append(cp2)
        perturbacion /= 10

    #mostrar(lista_cp_perturbaciones_positivas, lista_cp_perturbaciones_negativas, lista_perturbaciones_positivas, lista_perturbaciones_negativas)
    lista_auxiliar = lista_cp_perturbaciones_positivas + lista_cp_perturbaciones_negativas
    lista_auxiliar.sort()
    return lista_auxiliar[0]

def obtener_cp_con_perturbacion(x, perturbacion):
    suma = obtener_sumatoria(x, 25)
    y = x * (1 + (perturbacion) )
    suma_perturbada = obtener_sumatoria(y, 25)
    z = suma_perturbada - suma
    w = perturbacion * suma
    cp = math.fabs( z / (w) )
    return cp
