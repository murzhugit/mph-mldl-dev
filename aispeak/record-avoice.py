# @Author: mphz
# @Program: record-avoice.py                                                                                                   
# @Description: use pyaudio to record a voice then output to a wave audio file

import wave, pyaudio

# Settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 10

# Record Function
def recordWave():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT,
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)

    print ('-->Recording...-->')

    buffer = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        audio_data = stream.read(CHUNK)
        buffer.append(audio_data)

    print('-->Record Done-->')

    stream.stop_stream()
    stream.close()
    pa.terminate()

    wf = wave.open('murphyvoice.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(buffer))
    wf.close()

if __name__ == '__main__':
    recordWave()