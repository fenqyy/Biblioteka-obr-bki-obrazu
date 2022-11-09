import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from enum import Enum
from lab2 import BaseImage


class Histogram:
    """
    klasa reprezentujaca histogram danego obrazu
    """
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        self.values = values
        pass

    def plot(self) -> None:
        if self.values.ndim == 3:


            plt.subplot(1,3,1)
            plt.xlim([0,256])
            hist_r, bin_edges_r = np.histogram(self.values[:, :, 0], bins=256, range=(0,256))
            plt.plot(bin_edges_r[0:-1], hist_r, color="r")

            plt.subplot(1,3,2)
            plt.xlim([0,256])
            hist_g, bin_edges_g = np.histogram(self.values[:, :, 1], bins=256, range=(0, 256))
            plt.plot(bin_edges_r[0:-1], hist_g, color="g")

            plt.subplot(1, 3, 3)
            plt.xlim([0, 256])
            hist_b, bin_edges_b = np.histogram(self.values[:, :, 2], bins=256, range=(0, 256))
            plt.plot(bin_edges_b[0:-1], hist_b, color="b")

            plt.show()
        pass

he = Histogram(imread('lena.jpg'))
he.plot()





# class ImageDiffMethod(Enum):
#     mse = 0
#     rmse = 1
#
#
# class ImageComparison(BaseImage):
#     """
#     Klasa reprezentujaca obraz, jego histogram oraz metody porównania
#     """
#
#     def histogram(self) -> Histogram:
#         """
#         metoda zwracajaca obiekt zawierajacy histogram biezacego obrazu (1- lub wielowarstwowy)
#         """
#         pass
#
#     def compare_to(self, other: Image, method: ImageDiffMethod) -> float:
#         """
#         metoda zwracajaca mse lub rmse dla dwoch obrazow
#         """
#         pass
#
#
# class Image(GrayScaleTransform, ImageComparison):
#     pass