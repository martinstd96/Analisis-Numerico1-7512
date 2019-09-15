import numpy as np

def obtener_digitos():
    s = np.float64(1)
    t = np.float64(1)
    x = np.float64(2)

    while x > np.float64(1):
        print(x, t)
        t += np.float64(1)
        s /= np.float64(2)
        x = np.float64(1) + s

obtener_digitos()
