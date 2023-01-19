from BaseImage import *


class Thresholding(BaseImage):
    def threshold(self, value: int) -> BaseImage:
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                if self.data[i, j] < value:
                    self.data[i, j] = 0
                if self.data[i, j] >= value:
                    self.data[i, j] = 255
        return self
