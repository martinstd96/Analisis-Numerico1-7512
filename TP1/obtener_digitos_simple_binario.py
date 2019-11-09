import numpy as np

def obtener_digitos():
    s = np.float32(1)
    t = np.float32(1)
    x = np.float32(2)

    while x > np.float32(1):
        print(x, t)
        t += np.float32(1)
        s /= np.float32(2)
        x = np.float32(1) + s

obtener_digitos()
