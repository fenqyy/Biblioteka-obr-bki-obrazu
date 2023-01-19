from Image import *

x = Image('lena.jpg')
y = Image('papyka.jpg')
z = Image('duda.jpg')

y.to_sepia()
y.show_img()
tozsamosc = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
filtrgorny = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) #wyostrzenie obrazu
filtrdolny = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) #prefix 1/9, rozmycie obrazu
tabgauss3x3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) #prefix 1/16
tabgauss5x5 = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]]) #prefix 1/256
w0 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
w45 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
w90 = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
w135 = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
