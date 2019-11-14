from mostrar import mostrar

def resolver_por_euler():
    lista_u = []
    lista_v = []
    lista_t = []
    alfa = (100488 + 102889) / 2
    beta = 200.4
    semilla_u = 1
    semilla_v = 10
    h = 1.6 * ( 10 ** (-5) )
    contador = 0
    lista_u.append(semilla_u)
    lista_v.append(semilla_v)

    while contador < 62500:
        semilla_u = semilla_u + (h * semilla_v)
        calculo_auxiliar_1 = -1 * (beta * semilla_u)
        calculo_auxiliar_2 = -1 * (alfa * semilla_v)
        semilla_v = semilla_v + h * (calculo_auxiliar_1 + (calculo_auxiliar_2) + 1)
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
