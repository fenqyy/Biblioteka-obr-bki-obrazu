import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from enum import Enum
from lab2 import BaseImage


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

  import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from enum import Enum
from lab2 import BaseImage


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
    data = np.ndarray

    def __init__(self, data) -> None:
        """
        inicjalizator ...
        """
        self.data = data

    def align_image(self) -> 'BaseImage':
        """
        metoda zwracajaca poprawiony obraz metoda wyrownywania histogramow
        """
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        pop2 = np.dstack((r_layer, g_layer, b_layer))
        plt.imshow(pop2)
        plt.show()
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        r_layer = (r_layer - r_layer.min()) * (255 / (r_layer.max() - r_layer.min()))
        g_layer = (g_layer - g_layer.min()) * (255 / (g_layer.max() - g_layer.min()))
        b_layer = (b_layer - b_layer.min()) * (255 / (b_layer.max() - b_layer.min()))
        pop = np.dstack((r_layer, g_layer, b_layer))
        plt.imshow(pop)
        plt.show()
        pass


hx = ImageAligning(imread('lena.jpg'))
hx.align_image()


# class Image(GrayScaleTransform, ImageComparison, ImageAligning):
#     """
#     interfejs glownej klasy biblioteki c.d.
#     """
#     pass
