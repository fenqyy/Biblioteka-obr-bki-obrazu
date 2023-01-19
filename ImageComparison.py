from Histogram import *
from Image import *
from GrayScaleTransform import *
import numpy as np


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1


class ImageComparison(BaseImage):

    def histogram(self) -> Histogram:
        return Histogram(self.data)
        pass

    def compare_to(self, other: BaseImage, method: ImageDiffMethod) -> float:
        """
        metoda zwracajaca mse lub rmse dla dwoch obrazow
        """
        x = self.to_gray().histogram().values
        y = other.to_gray().histogram().values
        mse = 0
        for i in range(len(x)):
            mse += pow((x[i] - y[i]),2)
        if method == 0:
            return sum(mse) * (1 / len(x))
        if method == 1:
            return np.sqrt(sum(mse) * (1 / len(x)))
        pass
