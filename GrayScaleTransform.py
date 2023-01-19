from BaseImage import *


class GrayScaleTransform(BaseImage):

    def __init__(self, path: str) -> None:
        super().__init__(path)
        pass

    def to_gray(self) -> BaseImage:
        r_layer, g_layer, b_layer = np.squeeze(np.dsplit(self.data, self.data.shape[-1]))
        r = r_layer * 0.2989
        g = g_layer * 0.5870
        b = b_layer * 0.1140
        imggray = r + g + b
        self.data = imggray
        self.color_model = 4
        return self
        pass

    def to_sepia(self, alpha_beta: tuple = (None, None), w: int = None) -> BaseImage:
        gray = self.to_gray()
        if alpha_beta != (None, None):
            x = alpha_beta[0]
            y = alpha_beta[1]
            if x>1 and y<1 and x+y==2:
                l0 = gray.data * x
                l1 = gray.data
                l2 = gray.data * y
        else:
            if w is not None:
                if 20 <= w <= 40:
                    l0 = gray.data + 2 * w
                    l1 = gray.data + w
                    l2 = gray.data
        l0[l0>255] = 255
        l1[l1>255] = 255
        l2[l2>255] = 255
        self.data = np.dstack((l0,l1,l2))
        self.data = self.data/255
        return self
        pass

