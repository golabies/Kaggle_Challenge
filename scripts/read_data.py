import sounddevice as sd
from scipy.io import wavfile
import os
import numpy as np
import matplotlib.pyplot as plt


class ReadData:
    def __init__(self, folder_name, address=''):
        if address == '':
            address = '/'.join(os.getcwd().split('/')[:-1])
        os.chdir(address)
        os.chdir(folder_name)
        self.name = 'hello world'
        self.folder_name = folder_name
        self.voice = np.array([])
        self.wave_files = [file for file in os.listdir(os.path.join(address, self.folder_name)) if '.wav' in file]

    @staticmethod
    def play(voice, fs):
        sd.play(voice, fs)
        sd.wait()

    @staticmethod
    def show(voice):
        plt.plot(np.arange(len(voice)), voice)
        plt.show()

    @staticmethod
    def read_wave(name):
        fs, voice = wavfile.read(name)
        voice: np.ndarray
        voice = np.array([voice])
        return voice, fs


if __name__ == '__main__':
    read = ReadData('first_sample')
    for i in read.wave_files:
        voice_out, fs_out = read.read_wave(i)
        read.play(voice_out[0], fs_out)
        read.show(voice_out[0])
