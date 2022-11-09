import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.pyplot import imshow
from matplotlib.image import imsave
import numpy as np
from enum import Enum

class ColorModel(Enum):
    rgb = 0
    hsv = 1
    hsi = 2
    hsl = 3
    gray = 4

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
        plt.imshow(self.data)
        plt.show()
        pass

    def get_layer(self, layer_id: int) -> 'BaseImage':
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        if(layer_id == 0):
            return r_layer
        elif(layer_id == 1):
            return g_layer
        elif(layer_id == 2):
            return b_layer
        pass

he = BaseImage('lena.jpg')

#he.save_img('lenka.jpg')

x = imread('lenka.jpg')
plt.imshow(x)

plt.hist((512,512,3))
plt.show()