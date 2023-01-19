from GrayScaleTransform import *
from ImageComparison import *
from ImageAligning import *
from ImageFiltration import *
from Thresholding import *
from Histogram import *


class Image(GrayScaleTransform, ImageComparison, ImageAligning, ImageFiltration, Thresholding):

    def __init__(self, path: str) -> None:
        super().__init__(path)
        pass



