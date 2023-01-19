import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread, imsave
from matplotlib.pyplot import imshow
from enum import Enum


class ColorModel(Enum):
    rgb = 0
    hsv = 1
    hsi = 2
    hsl = 3
    gray = 4  # obraz 2d


class BaseImage:
    data: np.ndarray  # tensor przechowujacy piksele obrazu
    color_model: ColorModel  # atrybut przechowujacy biezacy model barw obrazu

    def __init__(self, path: str) -> None:
        self.data = imread(path)
        self.color_model = ColorModel.rgb
        pass

    def save_img(self, path: str) -> None:
        imsave(path, self.data)
        pass

    def show_img(self) -> None:
        if self.color_model == 4:
            imshow(self.data, cmap='gray')
            plt.show()
        else:
            imshow(self.data)
            plt.show()
        pass

    def get_layer(self, layer_id: int) -> 'BaseImage':
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        if layer_id == 0:
            return r_layer
        if layer_id == 1:
            return g_layer
        if layer_id == 2:
            return b_layer
        pass

    def to_hsv(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsv
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        r = np.float32(self.get_layer(0))
        g = np.float32(self.get_layer(1))
        b = np.float32(self.get_layer(2))
        V = np.zeros((self.data.shape[0], self.data.shape[1]))
        S = np.zeros((self.data.shape[0], self.data.shape[1]))
        H = np.zeros((self.data.shape[0], self.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                R = r[i, j]
                G = g[i, j]
                B = b[i, j]
                maximum = max(R, G, B)
                minimum = min(R, G, B)
                V[i, j] = int(maximum/255)
                if maximum > 0:
                    S[i, j] = int((1 - minimum) / maximum)
                else:
                    S[i, j] = 0
                if G >= B:
                    H[i, j] = math.acos((int(R) - (1 / 2 * int(G)) - (1 / 2 * int(B))) / math.sqrt(
                        int(R) ** 2 + int(G) ** 2 + int(B) ** 2 - int(R) * int(G) - int(R) * int(B) - int(G) * int(
                            B))) * 180 / math.pi
                else:
                    H[i, j] = 360 - math.acos((int(R) - (1 / 2 * int(G)) - (1 / 2 * int(B))) / math.sqrt(
                        int(R) ** 2 + int(G) ** 2 + int(B) ** 2 - int(R) * int(G) - int(R) * int(B) - int(G) * int(
                            B))) * 180 / math.pi

        x = np.dstack((H, S, V))
        self.data = x
        self.color_model = 1
        return self
        pass

    def to_hsi(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsi
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        r = np.float32(self.get_layer(0))
        g = np.float32(self.get_layer(1))
        b = np.float32(self.get_layer(2))
        I = np.zeros((self.data.shape[0], self.data.shape[1]))
        S = np.zeros((self.data.shape[0], self.data.shape[1]))
        H = np.zeros((self.data.shape[0], self.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                R = r[i, j]
                G = g[i, j]
                B = b[i, j]
                minimum = min(R, G, B)
                maximum = max(R, G, B)
                I[i, j] = int((R + G + B)/3)
                if maximum > 0:
                    S[i, j] = int((1 - minimum)/maximum)
                else:
                    S[i, j] = 0
                if G >= B:
                    H[i, j] = math.acos((int(R) - (1 / 2 * int(G)) - (1 / 2 * int(B))) / math.sqrt(int(R) ** 2 + int(G) ** 2 + int(B) ** 2 - int(R) * int(G) - int(R) * int(B) - int(G) * int(B))) * 180 / math.pi
                else:
                    H[i, j] = 360 - math.acos((int(R) - (1 / 2 * int(G)) - (1 / 2 * int(B))) / math.sqrt(int(R) ** 2 + int(G) ** 2 + int(B) ** 2 - int(R) * int(G) - int(R) * int(B) - int(G) * int(B))) * 180 / math.pi

        x = np.dstack((H, S, I)).astype('float32')
        self.data = x
        self.color_model = 2
        return self
        pass

    def to_hsl(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu hsl
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        r = self.get_layer(0)
        g = self.get_layer(1)
        b = self.get_layer(2)
        L = np.zeros((self.data.shape[0], self.data.shape[1]))
        S = np.zeros((self.data.shape[0], self.data.shape[1]))
        H = np.zeros((self.data.shape[0], self.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                R = r[i, j]
                G = g[i, j]
                B = b[i, j]
                maximum = max(R, G, B)
                minimum = min(R, G, B)
                d = (maximum - minimum) / 255
                L[i, j] = (0.5 * (int(maximum) + int(minimum)))/255
                if L[i, j] > 0:
                    S[i, j] = d / (1 - abs(2 * L[i, j] - 1))
                else:
                    S[i, j] = 0
                if G >= B:
                    H[i, j] = math.acos(R - (1 / 2 * (G) - (1 / 2 * B)) / math.sqrt(R **2 + G **2 + B **2 - R * G - R * B - G * B))*180/math.pi
                else:
                    H[i, j] = 360 - math.acos(R - (1/2*G) - (1/2*B))/math.sqrt(R **2 + G **2 + B **2 - R * G - R * B - G * B)*180/math.pi

        x = np.dstack((H, S, L))
        self.data = x
        self.color_model = 3
        return self
        pass

    def to_rgb(self) -> 'BaseImage':
        """
        metoda dokonujaca konwersji obrazu w atrybucie data do modelu rgb
        metoda zwraca nowy obiekt klasy image zawierajacy obraz w docelowym modelu barw
        """
        h = self.get_layer(0)
        s = self.get_layer(1)
        iy = self.get_layer(2)
        l = self.get_layer(2)
        v = self.get_layer(2)
        R = np.zeros((self.data.shape[0], self.data.shape[1]))
        G = np.zeros((self.data.shape[0], self.data.shape[1]))
        B = np.zeros((self.data.shape[0], self.data.shape[1]))
        if self.color_model == 3:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    H = h[i, j]
                    S = s[i, j]
                    L = l[i, j]
                    d = S*(1-abs(2*L-1))
                    m = int(255*(L - 0.5 * d))
                    x = d*(1 - abs(((H/60) % 2)-1))
                    if 0 <= H < 60:
                        R[i, j] = 255 * d + m
                        G[i, j] = 255 * x + m
                        B[i, j] = m
                    if 60 <= H < 120:
                        R[i, j] = 255 * x + m
                        G[i, j] = 255 * x + m
                        B[i, j] = m
                    if 120 <= H < 180:
                        R[i, j] = m
                        G[i, j] = 255 * d + m
                        B[i, j] = 255 * x + m
                    if 180 <= H < 240:
                        R[i, j] = m
                        G[i, j] = 255 * x + m
                        B[i, j] = 255 * d + m
                    if 240 <= H < 300:
                        R[i, j] = 255 * x + m
                        G[i, j] = m
                        B[i, j] = 255 * d + m
                    if 300 <= H < 360:
                        R[i, j] = 255 * d + m
                        G[i, j] = m
                        B[i, j] = 255 * x + m

        if self.color_model == 2:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    H = h[i, j]
                    S = s[i, j]
                    I = iy[i, j]
                    if H == 0:
                        R[i, j] = int(I + (2 * I * S))
                        G[i, j] = int(I - (I * S))
                        B[i, j] = int(I - (I * S))
                    if 0 < H < 120:
                        R[i, j] = int(I + (I * S) * math.cos(H)/math.cos(np.radians(60)-H))
                        G[i, j] = int(I + ((I * S) * ((1 - math.cos(H))/math.cos(np.radians(60)-H))))
                        B[i, j] = int(I - (I * S))
                    if H == 120:
                        R[i, j] = int(I - (I * S))
                        G[i, j] = int(I + (2 * I * S))
                        B[i, j] = int(I - (I * S))
                    if 120 < H < 240:
                        R[i, j] = int(I - (I * S))
                        G[i, j] = int(I + (I * S) * math.cos(H-120) / math.cos(np.radians(180)-H))
                        B[i, j] = int(I + ((I * S) * ((1-math.cos(H-120))/math.cos(np.radians(180)-H))))
                    if H == 240:
                        R[i, j] = int(I - (I * S))
                        G[i, j] = int(I - (I * S))
                        B[i, j] = int(I + (2 * I * S))
                    if 240 < H < 360:
                        R[i, j] = int(I + ((I * S) * ((1-math.cos(H-240))/math.cos(np.radians(300)-H))))
                        G[i, j] = int(I - (I * S))
                        B[i, j] = int(I + (I * S) * math.cos(H - 240)/math.cos(np.radians(300)-H))

        if self.color_model == 2:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    H = h[i, j]
                    S = s[i, j]
                    V = v[i, j]
                    M = int(255 * V)
                    m = int(M*(1-S))
                    z = int((M-m)*(1-abs(((H/60)%2)-1)))
                    if 0 <= H < 60:
                        R[i, j] = M
                        G[i, j] = z + m
                        B[i, j] = m
                    if 60 <= H < 120:
                        R[i, j] = z + m
                        G[i, j] = M
                        B[i, j] = m
                    if 120 <= H < 180:
                        R[i, j] = m
                        G[i, j] = M
                        B[i, j] = z + m
                    if 180 <= H < 240:
                        R[i, j] = m
                        G[i, j] = M
                        B[i, j] = z + m
                    if 240 <= H < 300:
                        R[i, j] = z + m
                        G[i, j] = m
                        B[i, j] = M
                    if 300 <= H < 360:
                        R[i, j] = M
                        G[i, j] = m
                        B[i, j] = z + m

        R[R > 255] = 255
        G[G > 255] = 255
        B[B > 255] = 255
        R[R < 0] = 0
        G[G < 0] = 0
        B[B < 0] = 0
        f = np.dstack((R, G, B)).astype('uint8')
        self.data = f
        self.color_model = 0
        return self
        pass
