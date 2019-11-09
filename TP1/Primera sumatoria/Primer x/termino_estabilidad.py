from funciones_en_comun import obtener_termino_estabilidad

def termino_estabilidad():
    te, mu_simple = obtener_termino_estabilidad()
    print( "El termino de establidad es: {}".format(te) )

termino_estabilidad()
