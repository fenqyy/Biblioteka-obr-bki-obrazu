from Histogram import *
from GrayScaleTransform import *


class ImageAligning(BaseImage):

    def __init__(self, path: str) -> None:
        super().__init__(path)

    def align_image(self, tail_elimination: bool = False) -> 'BaseImage':
        """
        metoda zwracajaca poprawiony obraz metoda wyrownywania histogramow
        """

        if self.data.ndim == 2:
            f = self.data.astype(np.float64)
            if tail_elimination:
                minimum = np.quantile(f, 0.05)
                maximum = np.quantile(f, 0.95)
            else:
                minimum = np.min(f)
                maximum = np.max(f)
            f = ((f - minimum) / (maximum - minimum))*255
            f[f > 255] = 255
            f[f < 0] = 0
            self.data = f.astype('uint8')
            return self
        if self.data.ndim == 3:
            fr = self.data[:, :, 0].astype(np.float64)
            fg = self.data[:, :, 1].astype(np.float64)
            fb = self.data[:, :, 2].astype(np.float64)
            if tail_elimination:
                minimumfr = np.quantile(fr, 0.05)
                maximumfr = np.quantile(fr, 0.95)
                minimumfg = np.quantile(fg, 0.05)
                maximumfg = np.quantile(fg, 0.95)
                minimumfb = np.quantile(fb, 0.05)
                maximumfb = np.quantile(fb, 0.95)
            else:
                minimumfr = np.min(fr)
                minimumfg = np.min(fg)
                minimumfb = np.min(fb)
                maximumfr = np.max(fr)
                maximumfg = np.max(fg)
                maximumfb = np.max(fb)
            fr = ((fr - minimumfr) / (maximumfr - minimumfr)) * 255
            fg = ((fg - minimumfg) / (maximumfg - minimumfg)) * 255
            fb = ((fb - minimumfb) / (maximumfb - minimumfb)) * 255
            fr[fr > 255] = 255
            fr[fr < 0] = 0
            fg[fg > 255] = 255
            fg[fg < 0] = 0
            fb[fb > 255] = 255
            fb[fb < 0] = 0
            f = np.dstack((fr, fg, fb))
            self.data = f.astype('uint8')
            return self

