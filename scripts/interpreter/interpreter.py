import scripts.interpreter.fft as fft
import scripts.interpreter.read_data as read_data
import scripts.interpreter.split_signal as split


class Interpreter:
    def __init__(self, signal, fs, length=1024):
        self.len = length
        self.sig = signal
        self.fs = fs

    def split_data(self):
        s = split.Split(self.sig, self.len)
        return s.fill()

    def my_ft(self):
        ft = fft.MyFt(self.sig, self.fs)
        return ft.my_ft()
