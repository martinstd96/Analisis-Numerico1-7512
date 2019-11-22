from mostrar import mostrar
from funciones import funcion_uno
from funciones import funcion_dos

def resolver_por_euler():
    lista_u = []
    lista_v = []
    lista_t = []
    semilla_u = 1
    semilla_v = 10
    h = 1.6 * ( 10 ** (-5) )
    contador = 0
    lista_u.append(semilla_u)
    lista_v.append(semilla_v)

    while contador < 62500:
        semilla_u_paso_siguiente = semilla_u + ( h * funcion_uno(semilla_v) )
        semilla_v_paso_siguiente = semilla_v + h * ( funcion_dos(semilla_u, semilla_v) )
        semilla_u = semilla_u_paso_siguiente
        semilla_v = semilla_v_paso_siguiente
        lista_u.append(semilla_u)
        lista_v.append(semilla_v)
        contador += 1

    contador = 0
    t = 0
    lista_t.append(t)

    while contador < 62500:
        t += h
        lista_t.append(t)
        contador += 1

    mostrar(lista_u, lista_v, lista_t)

resolver_por_euler()
