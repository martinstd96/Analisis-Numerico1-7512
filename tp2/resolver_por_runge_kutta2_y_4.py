from mostrar import mostrar
from funciones import funcion_uno
from funciones import funcion_dos
import pdb

def resolver_por_runge_kutta2_y_4():
    lista_u = []
    lista_v = []
    lista_t = []
    t = 0
    semilla_u = 1
    semilla_v = 10
    h = 1.6 * ( 10 ** (-5) )
    tol = 1 * ( 10 ** (-4) )

    while t < 1:
        euler_u = semilla_u + ( h * funcion_uno(semilla_v) )
        euler_v = semilla_v + h * ( funcion_dos(semilla_u, semilla_v) )
        r_k_2_u = semilla_u + (h / 2) * ( funcion_uno(semilla_v) + funcion_uno(euler_v) )
        r_k_2_v = semilla_v + (h / 2) * ( funcion_dos(semilla_u, semilla_v) + funcion_dos(euler_u, euler_v) )
        funcion_1_u = funcion_uno(semilla_v)
        funcion_1_v = funcion_dos(semilla_u, semilla_v)
        funcion_2_u = funcion_uno(semilla_v + ( (h / 2) * funcion_1_v) )
        funcion_2_v = funcion_dos(semilla_u + ( (h / 2) * funcion_1_u ), semilla_v + ( (h / 2) * funcion_1_v) )
        funcion_3_u = funcion_uno(semilla_v + ( (h / 2) * funcion_2_v) )
        funcion_3_v = funcion_dos(semilla_u + ( (h / 2) * funcion_2_u ), semilla_v + ( (h / 2) * funcion_2_v) )
        funcion_4_u = funcion_uno(semilla_v + (h * funcion_3_v) )
        funcion_4_v = funcion_dos(semilla_u + (h * funcion_3_u), semilla_v + (h * funcion_3_v) )
        r_k_4_u = semilla_u + (h / 6) * (funcion_1_u + (2 * funcion_2_u) + (2 * funcion_3_u) + funcion_4_u)
        r_k_4_v = semilla_v + (h / 6) * (funcion_1_v + (2 * funcion_2_v) + (2 * funcion_3_v) + funcion_4_v)
        #pdb.set_trace()
        error_local_u = abs(r_k_4_u - r_k_2_u)
        error_local_v = abs(r_k_4_v - r_k_2_v)
        lista_auxiliar = [error_local_u, error_local_v]
        error_local = min(lista_auxiliar)
        #print(h, error_local / h, error_local)

        if (error_local / h) < tol:
            semilla_u = r_k_4_u
            semilla_v = r_k_4_v
            lista_u.append(semilla_u)
            lista_v.append(semilla_v)
            lista_t.append(t)
            t += h
            print(t)

        #pdb.set_trace()
        h_previo = h
        maximo_valor_h = 1.967 * ( 10 ** (-5) )
        minimo_valor_h = 1 * ( 10 ** (-15) )

        if error_local == 0: h /= 2

        else: h = 0.8 * h * (((tol * h) / error_local) ** (1 / 2))
        #print(h, h_previo)

        if h < (h_previo / 2): h = h_previo / 2

        if h > (h_previo * 2): h = h_previo * 2

        if h < minimo_valor_h: h = minimo_valor_h

        if h > maximo_valor_h: h = maximo_valor_h
        #print(h)

    mostrar(lista_u, lista_v, lista_t)

resolver_por_runge_kutta2_y_4()
