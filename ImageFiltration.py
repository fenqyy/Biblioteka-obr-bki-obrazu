from typing import Optional
from BaseImage import *


class ImageFiltration:
    def conv_2d(image: BaseImage, kernel: np.ndarray, prefix: Optional[float] = None) -> BaseImage:
        """
        kernel: filtr w postaci tablicy numpy
        prefix: przedrostek filtra, o ile istnieje; Optional - forma poprawna obiektowo, lub domyslna wartosc = 1 - optymalne arytmetycznie
        metoda zwroci obraz po procesie filtrowania
        """
        f = image.data
        g = np.zeros((f.shape[0], f.shape[1]))
        for i in range(f.shape[0]):
            for j in range(f.shape[1]):
                for k in range(kernel.shape[0]):
                    for l in range(kernel.shape[1]):
                        g[i, j] += kernel[k, l] * f[i - k, j - l]
        if prefix is not None:
            g = g * prefix
        image.data = g.astype('uint8')
        return image
