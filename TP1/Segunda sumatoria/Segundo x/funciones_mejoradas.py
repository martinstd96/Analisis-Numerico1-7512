import numpy as np
import math

def obtener_sumatoria_mejorada(x, n):
    suma = 0

    for i in range(1, n + 1):
        y = (-1 / 4) ** i
        v = factorizar(x, i, 2 * i)
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

    for i in range(1, 25 + 1):
        y = (-1 / 4) ** i
        v = factorizar_doble(x, i, 2 * i)
        k = y * v
        suma += k

    return suma

def obtener_sumatoria_simple_mejorada():
    x = np.float32( 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) ) )
    suma = np.float32(0)

    for i in range(1, 25 + 1):
        y = (-1 / 4) ** i
        v = factorizar_simple(x, i, 2 * i)
        k = y * v
        suma += k

    return suma

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

def factorizar(x, y, potencia):
    cociente = 1
    i = y
    k = potencia

    while i > 0:
        divisor = i ** 2
        z = x / divisor
        cociente = cociente * z
        i -= 1
        k -= 1

    x = x ** k
    cociente = cociente * x
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
    suma = obtener_sumatoria_mejorada(x, 25)
    y = x * (1 + (perturbacion) )
    suma_perturbada = obtener_sumatoria_mejorada(y, 25)
    z = suma_perturbada - suma
    w = perturbacion * suma
    cp = math.fabs( z / (w) )
    return cp
