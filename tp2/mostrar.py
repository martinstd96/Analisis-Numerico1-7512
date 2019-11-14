import matplotlib.pyplot as plt

def mostrar(lista_u, lista_v, lista_t):
    plt.style.use('ggplot')
    plt.title("Grafico x1 (rojo) y x2 (azul) en función de t")
    plt.plot(lista_t, lista_u, 'r-o')
    plt.plot(lista_t, lista_v, 'b-x')
    plt.xlabel("t")
    plt.ylabel("x1 y x2")
    plt.show()
