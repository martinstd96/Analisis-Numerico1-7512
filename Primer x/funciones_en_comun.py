import numpy as np
import math

def obtener_sumatoria(x, n):
    suma = 0

    for i in range(1, n + 1):
        y = (-1) ** i
        z = x ** (2 * i)
        u = math.factorial(2 * i)
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
    x = np.float64( 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) ) )
    suma = np.float64(0)

    for i in range(1, 8 + 1):
        y = np.float64( (-1) ** i )
        z = np.float64( x ** (2 * i) )
        u = np.float64( math.factorial(2 * i) )
        v = np.float64( z / u )
        k = np.float64( y * v )
        suma += np.float64(k)

    return suma

def obtener_sumatoria_simple():
    x = np.float32( 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) ) )
    suma = np.float32(0)

    for i in range(1, 8 + 1):
        y = np.float32( (-1) ** i )
        z = np.float32( x ** (2 * i) )
        u = np.float32( math.factorial(2 * i) )
        v = np.float32( z / u )
        k = np.float32( y * v )
        suma += np.float32(k)

    return suma

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
    x = 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) )
    suma = obtener_sumatoria(x, 8)
    perturbacion = 0.000000000000001
    y = x * (1 + (perturbacion) )
    suma_perturbada = obtener_sumatoria(y, 8)
    z = suma_perturbada - suma
    w = perturbacion * suma
    cp = math.fabs( z / (w) )

    return cp
