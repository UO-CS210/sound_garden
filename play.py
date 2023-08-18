import pygame
import time
import pygame.mixer as mixer
pygame.init()
mixer.init()
sound = mixer.Sound("middle_c.wav")
sound.set_volume(0.2)
chan = sound.play()
print(f"Channel middle_c.wav is {chan}")
while chan.get_busy():
    time.sleep(0.05)
    print(".", end="")
print(".")

sound = mixer.Sound("waves/C4.wav")
sound.set_volume(0.2)
chan = sound.play()
print(f"Channel waves/C4.wav is {chan}")
while chan.get_busy():
    time.sleep(0.05)
    print(".", end="")
print(".")

sound = mixer.Sound("waves/A4.wav")
sound.set_volume(0.2)
chan = sound.play()
print(f"Channel waves/C4.wav is {chan}")
while chan.get_busy():
    time.sleep(0.05)
    print(".", end="")
print(".")

import freq_hz
for note in freq_hz.c_major_freqs.keys():
    wav_file_name = f"waves/{note}.wav"
    print(f"Loading sound from '{wav_file_name}'")
    sound = mixer.Sound(wav_file_name)
    print(f"Sound is {sound}")
    chan = sound.play()
    print(f"Channel is {chan}")
    while chan.get_busy():
        time.sleep(0.01)
        print(".", end="")
print(".")




