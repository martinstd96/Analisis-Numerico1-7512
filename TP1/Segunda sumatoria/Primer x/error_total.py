import math
from funciones_en_comun import obtener_condicion_problema
from funciones_en_comun import obtener_termino_estabilidad
from funciones_en_comun import obtener_sumatoria

def error_total():
    cp = obtener_condicion_problema()
    te, mu = obtener_termino_estabilidad()
    r = 1 * ( 10 ** (-4) )
    x = cp * r
    y = te * mu
    error_relativo = math.fabs(x + y)
    print( "El error total relativo es: {}".format(error_relativo) )
    x = 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) )
    sumatoria = math.fabs( obtener_sumatoria(x, 8) )
    print( "El error total absoluto es: {}".format(sumatoria * error_relativo) )

error_total()
