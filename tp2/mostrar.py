import matplotlib.pyplot as plt

def mostrar(lista_u, lista_v, lista_t):
    plt.style.use('ggplot')
    plt.title("Grafico x1 (rojo) y x2 (azul) en función de t")
    plt.plot(lista_t, lista_u, 'r-o')
    plt.plot(lista_t, lista_v, 'b-x')
    plt.xlabel("t")
    plt.ylabel("x1 y x2")
    plt.show()

def mostrar_h_en_funcion_numero_iteracion(lista_h, lista_iteraciones):
    plt.style.use('ggplot')
    plt.title("Grafico del tamaño de paso en función del número de iteración")
    plt.plot(lista_iteraciones, lista_h, 'r-o')
    plt.xlabel("Número de iteración")
    plt.ylabel("Tamaño de paso")
    plt.show()
