import scripts.interpreter.fft as fft
import scripts.interpreter.read_data as read_data
import scripts.interpreter.split_signal as split
import numpy as np


class Interpreter:
    def __init__(self, signal, fs, window_length=1024):
        self.len = window_length
        self.sig = signal
        self.fs = fs

    def split_data(self):
        s = split.Split(self.sig, self.len)
        return s.fill()

    def my_ft(self, signal):
        ft = fft.MyFt(signal, self.fs)
        temp = ft.my_ft()
        return temp[0], temp[1]

    def run(self):
        for i in self.split_data():
            temp = self.my_ft(i)[1]
            yield np.hstack([temp, i])


if __name__ == '__main__':
    read = read_data.ReadData('train_curated', address='/home/golabi/Kaggle_Challenge/data')
    voice = read.wave_files[109]
    voice, fs_ = read.read_wave(voice)
    voice = voice[0]
    # read.show(voice)
    # read.play(voice, fs_)
    inter = Interpreter(signal=voice, fs=fs_, window_length=2048*128)
    # print(len(inter.my_ft(voice[:12345])[0]))
    t = 0
    for i in inter.run():
        # print(len(i))
        t += 1
        print(t)
    print(t)
