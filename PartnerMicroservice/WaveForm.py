import os
import numpy as np
import scipy
from matplotlib import pyplot as plt
import pathlib


def create_wavefile(file_name: str):
    audio_filename = os.path.basename(file_name)
    location = pathlib.Path(file_name).parent.resolve()
    wave_data = os.path.join(location, audio_filename)

    sample_rate, audio_buffer = scipy.io.wavfile.read(wave_data)
    duration = len(audio_buffer) / sample_rate
    time = np.arange(0, duration, 1 / sample_rate)  # time vector

    plt.plot(time, audio_buffer)
    plt.title('Left Channel')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')

    plt.savefig('C:/Users/Kenne/Temp/Images/foo.png', bbox_inches='tight')
    os.remove(file_name)
    return 'C:/Users/Kenne/Temp/Images/foo.png'
