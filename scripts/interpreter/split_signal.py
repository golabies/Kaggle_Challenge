import numpy as np


class Split:
    def __init__(self, signal, length):
        self.len = length
        self.sig = signal
        self.out = []

    def fill(self):
        for i in range(self.len, len(self.sig)):
            yield np.array(self.sig[i-self.len:i])


if __name__ == '__main__':
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    s = Split(a, 3)
    print(s.fill())
