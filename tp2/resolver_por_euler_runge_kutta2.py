from mostrar import mostrar
from funciones import funcion_uno
from funciones import funcion_dos

def resolver_por_euler_runge_kutta2():
    lista_u = []
    lista_v = []
    lista_t = []
    t = 0
    semilla_u = 1
    semilla_v = 10
    h = 1.6 * ( 10 ** (-5) )
    tol = 1 * ( 10 ** (-6) )

    while t < 1:
        euler_u = semilla_u + ( h * funcion_uno(semilla_v) )
        euler_v = semilla_v + h * ( funcion_dos(semilla_u, semilla_v) )
        r_k_u = semilla_u + (h / 2) * ( funcion_uno(semilla_v) + funcion_uno(euler_v) )
        r_k_v = semilla_v + (h / 2) * ( funcion_dos(semilla_u, semilla_v) + funcion_dos(euler_u, euler_v) )
        error_local_u = abs(r_k_u - euler_u)
        error_local_v = abs(r_k_v - euler_v)
        error_local_u /= h
        error_local_v /= h
        lista_auxiliar = [error_local_u, error_local_v]
        print(error_local_u, error_local_v)
        lista_auxiliar.sort()
        error_local = lista_auxiliar[0]

        if error_local < tol:
            semilla_u = r_k_u
            semilla_v = r_k_v
            lista_u.append(semilla_u)
            lista_v.append(semilla_v)
            lista_t.append(t)
            t += h

        hp = h
        v = 1 * ( 10 ** (-2) )
        u = 1 * ( 10 ** (-15) )
        h = 0.8 * h * ((tol * h) / error_local)

        if (h < hp/2 or h > 2*hp) and (h > v or h < u):
            print(h)

    mostrar(lista_u, lista_v, lista_t)

resolver_por_euler_runge_kutta2()
