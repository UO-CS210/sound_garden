import numpy as np
import freq_hz as freq
import wavio

rate = 22050  # samples per second.  Why this value?
T = 0.15  # duration in seconds
n = int(rate * T)  # number of samples
t = np.arange(n)/rate  # grid of time values (evenly spaced in interval)
f = 440.0  # frequency (Hz)  Should be middle A
x = np.sin(2*np.pi * f * t)  # sine wave amplitude 1
wavio.write("middle_c.wav", x, rate, sampwidth=3)

# FIXME:  Ramp audio down to 0 by reducing amplitude gradually for
#   the last half of the note, to avoid a "pop" at end of sample.
#   Partly done --- now ramping down linearly from start.  Next step
#   is ramping different segments between different bounds.

def ramp(wave: list[float],
         from_index: int, to_index: int,
         from_level: float, to_level: float):
    """Interpolate coefficients from from_level to to_level
    over the interval from_index to to_index - 1.
    """
    ...
    for i in range(from_index, to_index):
        prior = wave[i]
        frac = (i - from_index) / (to_index - from_index)
        amped = prior * (from_level + frac * (to_level - from_level))
        wave[i] = amped

for note, hz in freq.c_major_freqs.items():
    print(f"Making waves at {hz}hz")
    x = np.sin(2*np.pi * hz * t)
    # Ramp down samples to avoid pop at end of each sample
    ramp(x, 0, len(x)//4, 0.0, 1.0)
    ramp(x, len(x)//2, len(x), 1.0, 0.0)
    wavio.write(f"waves/{note}.wav", x, rate, sampwidth=3)






