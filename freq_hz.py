"""Note frequencies in Hz, taken from
https://pages.mtu.edu/~suits/notefreqs.html
(use is consistent with copyright terms)
"""

# As lookup table
c_major_freqs = {
"C2": 	65.41,
"D2": 	73.42, 
"E2": 	82.41,
"F2": 	87.31,
"G2":	98.00,
"A2":	110.00, 
"B2":	123.47,
"C3": 	130.81,
"D3": 	146.83,
"E3": 	164.81,
"F3": 	174.61,
"G3": 	196.00,
"A3": 	220.00,
"B3": 	246.94,
"C4": 	261.63, 	# Middle C
"D4": 	293.66,
"E4":	329.63,
"F4":	349.23,
"G4":	392.00,
"A4":	440.00,	# A4=440 is standard modern tuning
"B4":	493.88,
"C5": 	523.25
}

# As symbols,
C2 = 	65.41
D2 = 	73.42 
E2 = 	82.41
F2 = 	87.31
G2 =	98.00
A2 =	110.00 
B2 =	123.47
C3 = 130.81
D3 = 146.83
E3 = 164.81
F3 = 174.61
G3 = 196.00
A3 = 220.00
B3 = 246.94
C4 = 261.63 	# Middle C
D4 = 293.66
E4 =	329.63
F4 =	349.23
G4 =	392.00
A4 =	440.00	# A4 =440 is standard modern tuning
B4 =	493.88
C5 = 523.25

C_MAJOR_LOW = [C3, D3, E3, F3, G3, A3, B3, C4]
C_MAJOR_MIDDLE = [C4, D4, E4, F4, G4, A4, B4, C5]
C_MAJOR = C_MAJOR_LOW + C_MAJOR_MIDDLE[1:]



# Wider range, all harmonize
# (after https://medium.com/@astromattrusso/sonification-101-how-to-convert-data-into-music-with-python-71a6dd67751c)
C_MAJOR_PENTATONIC = [C2, D2, E2, G2, A2,
                      C3, D3, E3, G3, A3,
                      C4, D4, E4, G4, A4]

