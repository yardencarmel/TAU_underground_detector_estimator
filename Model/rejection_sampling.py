import numpy as np
import matplotlib.pyplot as plt

pi = np.pi


class RejectionSampling:
    def __init__(self):
        self.x_len = 1000
        self.sample_size = 0
        self.xs = np.linspace(-pi/3, pi/3, self.x_len)
        self.ys = self.f(self.xs)

    def get_angles(self, sample_size):
        samples = self.batch_sample(self.f, sample_size, self.x_len, min(self.xs), max(self.xs))
        self.print_results(samples)
        return samples

    def print_results(self, samples):
        plt.plot(self.xs, self.ys, label="Function")
        plt.hist(samples, density=True, alpha=0.2, label="Sample distribution")
        plt.hist(samples, 1000, color='b', density=True, alpha=0.1, label="Sample distribution")
        plt.xlim(min(self.xs), max(self.xs)), plt.ylim(0, 1.1), plt.xlabel("x"), plt.ylabel("f(x)"), plt.legend()
        plt.show()

    @staticmethod
    def f(x):
        return (2 / pi) * np.cos(x) ** 2

    @staticmethod
    def batch_sample(function, num_samples, batch, x_min=-0.5 * pi, x_max=0.5 * pi,
                     y_max=2 / pi):
        samples = []
        while len(samples) < num_samples:
            x = np.random.uniform(low=x_min, high=x_max, size=batch)
            y = np.random.uniform(low=0, high=y_max, size=batch)
            samples += x[y < function(x)].tolist()
        return samples[:num_samples]
