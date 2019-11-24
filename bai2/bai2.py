import winsound

sep = 2**(1./12.) # Can bac 12 cua 2
nla = 440
ams = [nla*(sep**i) for i in range(-8, 4)]

for it in ams:
    winsound.Beep(int(it), 1000)

# import wavio
import wave

# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 2
# fs = 44100  # Record at 44100 samples per second
# seconds = 3
# filename = "output.wav"
#
# p = pyaudio.PyAudio()  # Create an interface to PortAudio

