print('Nhan Ctrl+C de tat\n-------------\n')
import winsound, time
try:
    LEN = 12
    while(True):
        for i in range(LEN):
            winsound.PlaySound(str(i)+"_out.wav", winsound.SND_FILENAME)
            time.sleep(0.2)
except KeyboardInterrupt:
    print('\n------Done-------\n')
