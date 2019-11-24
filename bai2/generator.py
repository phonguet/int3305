import math
import wave
import struct

sep = 2**(1./12.) # Can bac 12 cua 2
nla = 440.0
ams = [nla*(sep**i) for i in range(-8, 4)]

sample_rate = 44100.0

def append_sinewave(freq=440.0,duration_ms=500,volume=1.0):
    audio=[]
    num_samples = duration_ms*(sample_rate / 1000.0)
    for x in range(int(num_samples)):
        decv = 1 - math.sqrt(math.sqrt(x+1)/(num_samples))
        audio.append(volume*(decv)*math.sin(2*math.pi*freq*( x/sample_rate )))
    return audio

def save_wav(file_name, audio):
    wav_file=wave.open(file_name,"w")
    nchannels = 1
    sampwidth = 2
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample*32767.0 )))
    wav_file.close()


# from matplotlib import pyplot as plt

# for i in range(2):
for i in range(len(ams)):
    data = append_sinewave(freq=ams[i], duration_ms=500)
    save_wav(str(i) + "_out.wav", data)

#     plt.subplot(1,2, i+1)
#     plt.plot(range(len(data)), data)
# plt.show()

