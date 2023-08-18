# Musical note frequencies

Frequency in hertz can be derived mathematically, but as we need 
only a few nice-sounding notes it will be enough to hard-code their
frequencies.  These are taken from [the physics of sound]
(https://pages.mtu.edu/~suits/notefreqs.html), by  B. H. Suits, 
Physics Department, Michigan Technological University, (copyright 
1998-2023).   

See the link above for updates.  

C4 is middle C.  We will take C scale (so no sharps or flats) for 
three octaves spanning middle C. 

note  freq   cm
C3	130.81	263.74
 C#3/Db3 	138.59	248.93
D3	146.83	234.96
 D#3/Eb3 	155.56	221.77
E3	164.81	209.33
F3	174.61	197.58
 F#3/Gb3 	185.00	186.49
G3	196.00	176.02
 G#3/Ab3 	207.65	166.14
A3	220.00	156.82
 A#3/Bb3 	233.08	148.02
B3	246.94	139.71
C4	261.63	131.87
 C#4/Db4 	277.18	124.47
D4	293.66	117.48
 D#4/Eb4 	311.13	110.89
E4	329.63	104.66
F4	349.23	98.79
 F#4/Gb4 	369.99	93.24
G4	392.00	88.01
 G#4/Ab4 	415.30	83.07
A4	440.00	78.41
 A#4/Bb4 	466.16	74.01
B4	493.88	69.85
C5	523.25	65.93

## Avoiding a pop

Creating a uniform amplitude WAV file creates a pop at the end of 
each sample on playback.  From Stack Overflow: 

This is known as the "dread audio cliff of noise".

When you have a digital signal which is higher than 0 and you abruptly cut it off, the waveform must plummet to 0. As people who deal with analog signals will tell you, the digital cliff has (in principle) all frequencies present at some amplitude. This transition sounds like a "pop" by the time it gets to the speakers.

Almost all audio is mastered so that the amplitude is faded to zero
by the time the sample ends. If your sample doesn't have this
characteristic, fade the sample to zero upon playback. As was noted by
the OP, even a 2.5 millisecond fade can be enough to avoid the pop.

@msw This was the problem - I never knew that abruptly turning off the
sound would cause this, although I really should have suspected it, what
with speakers being physical devices. Even an approximately 0.0025
second fade time was enough to prevent the "popping", accomplished by
adding if i>40900: freq1=int(freq1*(41000-i)/100.0) into the audio
generation loop. Thank you! Could you put this in an answer so I can
mark it as correct? –
Larkeith
Sep 7, 2015 
