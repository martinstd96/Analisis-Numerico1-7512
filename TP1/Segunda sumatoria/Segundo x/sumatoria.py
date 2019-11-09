import math
from funciones_en_comun import obtener_sumatoria

def sumatoria():
    x = 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) )
    error = obtener_sumatoria(x, 25) - obtener_sumatoria(x, 26)
    suma = obtener_sumatoria(x, 25)
    print( "El error relativo es: {} y el numero de pasos es: {}".format( math.fabs( error / suma ), 25) )

sumatoria()
