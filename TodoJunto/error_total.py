import math
from funciones_en_comun import obtener_condicion_problema
from funciones_en_comun import obtener_termino_estabilidad
from funciones_en_comun import obtener_sumatoria

def error_total(x, iteraciones):
    cp = obtener_condicion_problema(x,iteraciones)
    te, mu = obtener_termino_estabilidad(x)
    r = 1 * ( 10 ** (-4) )
    x = cp * r
    y = te * mu
    error_relativo = math.fabs(x + y)
    sumatoria = math.fabs( obtener_sumatoria(x, iteraciones) )
    return (sumatoria* error_relativo),error_relativo

def main(error_imprimir,iteraciones):
    primer_x = 100488 * ( 10 ** (-5) ) + 102889 * ( 10 ** (-6) )
    segundo_x = 100488 * ( 10 ** (-4) ) + 102889 * ( 10 ** (-5) )
    if(error_imprimir==1):
        error_abs,error_rel = error_total(primer_x,iteraciones)
    else:
        error_abs,error_rel = error_total(segundo_x,iteraciones)
    print( "El error total relativo es: {}".format(error_rel) )
    print( "El error total absoluto es: {}".format(error_abs) )
main(1 , 8)
main(2,26)