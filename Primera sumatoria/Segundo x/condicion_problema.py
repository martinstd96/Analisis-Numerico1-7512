from funciones_en_comun import obtener_condicion_problema

def condicion_problema(imprimir = True):
    cp = obtener_condicion_problema()
    print( "La condicion del problema es: {}".format(cp) )

condicion_problema()
