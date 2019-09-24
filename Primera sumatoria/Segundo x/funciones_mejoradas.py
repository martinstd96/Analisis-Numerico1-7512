import numpy as np
import math

def obtener_sumatoria_mejorada(x, n):
    suma = 0

    for i in range(1, n + 1):
        y = (-1) ** i
        v = factorizar(x, 2 * i, 2 * i)
        k = y * v
        suma += k

    return suma

def obtener_termino_estabilidad_mejorado():
    sumatoria_doble = obtener_sumatoria_doble_mejorada()
    sumatoria_simple = obtener_sumatoria_simple_mejorada()
    digitos_simple = obtener_digitos_simple_decimal()
    mu_simple = 0.5 * ( 10 ** (np.float32(1) - digitos_simple) )
    x = math.fabs( sumatoria_doble - sumatoria_simple )
    y = math.fabs( sumatoria_doble )
    z = y * mu_simple
    te = x / z

    return te, mu_simple

def obtener_sumatoria_doble_mejorada():
    x = np.float64( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    suma = np.float64(0)

    for i in range(1, 26 + 1):
        y = np.float64( (-1) ** i )
        v = np.float64(factorizar_doble(x, 2 * i, np.float64(2 * i)))
        k = np.float64(y * v)
        suma += np.float64(k)

    return suma

def obtener_sumatoria_simple_mejorada():
    x = np.float32( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    suma = np.float32(0)

    for i in range(1, 26 + 1):
        y = np.float32( (-1) ** i )
        v = np.float32(factorizar_simple(x, 2 * i, np.float64(2 * i)))
        k = np.float32(y * v)
        suma += np.float32(k)

    return suma

def factorizar_simple(x, potencia, y):
    cociente = np.float32(1)
    resto = y

    for i in range(potencia):
        z = np.float32(x / resto)
        cociente = np.float32(cociente * z)
        resto -= np.float32(1)

    return cociente

def factorizar_doble(x, potencia, y):
    cociente = np.float64(1)
    resto = y

    for i in range(potencia):
        z = np.float64(x / resto)
        cociente = np.float64(cociente * z)
        resto -= np.float64(1)

    return cociente

def factorizar(x, potencia, y):
    cociente = 1
    resto = y

    for i in range(potencia):
        z = x / resto
        cociente = cociente * z
        resto -= 1

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

def obtener_condicion_problema_mejorada():
    x = 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) )
    perturbacion = 0.1
    lista_cp_perturbaciones_positivas = []
    lista_cp_perturbaciones_negativas = []
    lista_perturbaciones_positivas = []
    lista_perturbaciones_negativas = []

    for i in range(15):
        cp1 = obtener_cp_con_perturbacion_mejorada(x, perturbacion)
        cp2 = obtener_cp_con_perturbacion_mejorada(x, -perturbacion)
        lista_perturbaciones_positivas.append(perturbacion)
        lista_perturbaciones_negativas.append(-perturbacion)
        lista_cp_perturbaciones_positivas.append(cp1)
        lista_cp_perturbaciones_negativas.append(cp2)
        perturbacion /= 10

    #mostrar(lista_cp_perturbaciones_positivas, lista_cp_perturbaciones_negativas, lista_perturbaciones_positivas, lista_perturbaciones_negativas)
    lista_auxiliar = lista_cp_perturbaciones_positivas + lista_cp_perturbaciones_negativas
    lista_auxiliar.sort()
    return lista_auxiliar[0]

def obtener_cp_con_perturbacion_mejorada(x, perturbacion):
    suma = obtener_sumatoria_mejorada(x, 26)
    y = x * (1 + (perturbacion) )
    suma_perturbada = obtener_sumatoria_mejorada(y, 26)
    z = suma_perturbada - suma
    w = perturbacion * suma
    cp = math.fabs( z / (w) )
    return cp
