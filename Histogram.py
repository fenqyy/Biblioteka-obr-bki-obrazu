from BaseImage import *

class Histogram:
    values: np.ndarray

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
            plt.plot(bin_edges_g[0:-1], hist_g, color="g")

            plt.subplot(1, 3, 3)
            plt.xlim([0, 256])
            hist_b, bin_edges_b = np.histogram(self.values[:, :, 2], bins=256, range=(0, 256))
            plt.plot(bin_edges_b[0:-1], hist_b, color="b")

            plt.show()

        else:
            plt.xlim([0, 256])
            hist, hist_edge = np.histogram(self.values, bins=256, range=(0, 256))
            plt.plot(hist_edge[0:-1], hist)
            plt.show()
        pass

    def to_cumulated(self) -> 'Histogram':
        hist, hist_edge = np.histogram(self.values, bins=256, range=(0, 256))
        hist_cumulative = np.cumsum(hist)
        plt.plot(hist_edge[0:-1], hist_cumulative, color="blue")
        plt.show()
        pass
