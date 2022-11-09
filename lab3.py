import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from enum import Enum
from lab2 import BaseImage

values: np.ndarray

class GrayScaleTransform(BaseImage):
    def __init__(self, data: np.ndarray) -> None:
        self.data = data
        pass

    def to_gray(self) -> BaseImage:
        R, G, B = self.data[:, :, 0], self.data[:, :, 1], self.data[:, :, 2]
        imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
        plt.imshow(imgGray, cmap='gray')
        plt.show()
        pass

    def to_sepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        """
        metoda zwracajaca obraz w sepii jako obiekt klasy BaseImage
        sepia tworzona metoda 1 w przypadku przekazania argumentu alpha_beta
        lub metoda 2 w przypadku przekazania argumentu w
        """
        R, G, B = self.data[:, :, 0], self.data[:, :, 1], self.data[:, :, 2]
        imgSepia = 1.5 * R + G + 0.5 * B
        plt.imshow(imgSepia)
        plt.show()
        pass


# class Image(GrayScaleTransform):
#     """
#     klasa stanowiaca glowny interfejs biblioteki
#     w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
#     realizujacych kolejne metody przetwarzania obrazow
#     """
#     def __init__(self, ...) -> None:
#         pass
#


he = GrayScaleTransform(imread('lena.jpg'))
he.to_gray()
he.to_sepia()