import math
from funciones_mejoradas import obtener_condicion_problema_mejorada
from funciones_mejoradas import obtener_termino_estabilidad_mejorado
from funciones_mejoradas import obtener_sumatoria_mejorada

def error_total_mejorado():
    cp = obtener_condicion_problema_mejorada()
    te, mu = obtener_termino_estabilidad_mejorado()
    r = 1 * ( 10 ** (-4) )
    x = cp * r
    y = te * mu
    error_relativo = math.fabs(x + y)
    print( "El error total relativo es: {}".format(error_relativo) )
    x = 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) )
    sumatoria = math.fabs( obtener_sumatoria_mejorada(x, 26) )
    print( "El error total absoluto es: {}".format(sumatoria * error_relativo) )

error_total_mejorado()
