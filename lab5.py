import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from enum import Enum
from lab2 import BaseImage, ColorModel
from lab3 import GrayScaleTransform


class Histogram:
    """
    kontunuacja implementacji klasy
    """
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray) -> None:
        self.values = values
        pass

    def plot(self) -> None:
        if self.values.ndim == 3:
            plt.subplot(1, 3, 1)
            plt.xlim([0, 256])
            hist_r, bin_edges_r = np.histogram(self.values[:, :, 0], bins=256, range=(0, 256))
            plt.plot(bin_edges_r[0:-1], hist_r, color="r")
            plt.subplot(1, 3, 2)
            plt.xlim([0, 256])
            hist_g, bin_edges_g = np.histogram(self.values[:, :, 1], bins=256, range=(0, 256))
            plt.plot(bin_edges_r[0:-1], hist_g, color="g")
            plt.subplot(1, 3, 3)
            plt.xlim([0, 256])
            hist_b, bin_edges_b = np.histogram(self.values[:, :, 2], bins=256, range=(0, 256))
            plt.plot(bin_edges_b[0:-1], hist_b, color="b")
            plt.show()
        pass

    def to_cumulated(self) -> 'Histogram':
        """
        metoda zwracajaca histogram skumulowany na podstawie stanu wewnetrznego obiektu
        """
        hist, hist_edge = np.histogram(self.values, bins=256, range=(0, 256))
        hist_cumulative = np.cumsum(hist)
        plt.plot(hist_edge[0:-1], hist_cumulative, color="blue")
        plt.show()
        pass


# he = Histogram(imread('lena.jpg'))
# he.to_cumulated()


class ImageAligning(BaseImage):
    """
    klasa odpowiadająca za wyrównywanie hostogramu
    """
    values = np.ndarray

    def __init__(self, values) -> None:
        """
        inicjalizator ...
        """
        self.values = values


    def align_image(self) -> 'BaseImage':
        """
        metoda zwracajaca poprawiony obraz metoda wyrownywania histogramow
        """
        hist, hist_edge = np.histogram(self.values, bins=256, range=(0, 256))
        plt.plot(hist_edge[0:-1], hist, color="blue")
        plt.show()
        max = np.max(self.values)
        min = np.min(self.values)
        self.values = (self.values - min) * (255 / (max - min))(np.uint8)
        hist, hist_edge = np.histogram(self.values, bins=256, range=(0, 256))
        plt.plot(hist_edge[0:-1], hist, color="blue")
        plt.show()
        pass


hx = ImageAligning(imread('lena.jpg'))
hx.align_image()

# class Image(GrayScaleTransform, ImageComparison, ImageAligning):
#     """
#     interfejs glownej klasy biblioteki c.d.
#     """
#     pass
