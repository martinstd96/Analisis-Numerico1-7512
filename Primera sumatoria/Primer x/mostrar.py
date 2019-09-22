import matplotlib.pyplot as plt

def mostrar(lista_cp_perturbaciones_positivas, lista_cp_perturbaciones_negativas, lista_perturbaciones_positivas, lista_perturbaciones_negativas):
    plt.style.use('ggplot')
    plt.title("Grafico cp para la primera x y la sumatoria (1)")
    plt.plot(lista_perturbaciones_positivas, lista_cp_perturbaciones_positivas, 'r-o')
    plt.plot(lista_cp_perturbaciones_negativas, lista_cp_perturbaciones_negativas, 'b-x')
    plt.xlabel("Perturbaciones")
    plt.ylabel("Cp")
    plt.show()
