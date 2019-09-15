import math
from funciones_en_comun import obtener_sumatoria

def sumatoria():
    x = 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) )
    error = obtener_sumatoria(x, 8) - obtener_sumatoria(x, 9)
    suma = obtener_sumatoria(x, 8)
    print( "El error relativo es {}".format( math.fabs( error / suma ) ) )

sumatoria()
