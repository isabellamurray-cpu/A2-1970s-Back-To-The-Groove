# Funk/Disco Drums – Section 1 of 'Back to the Groove'

from tunepad.constants import *
# A minor pentatonic flavor: A2 C3 D3 E3 G3
# EIGHTH_NOTE = 0.5 beat; QUARTER_NOTE = 1 beat

for bar in range(4):  # 4 bars loop
    playNote(A2, EIGHTH_NOTE); playNote(C3, EIGHTH_NOTE)
    playNote(D3, QUARTER_NOTE); rest(EIGHTH_NOTE); playNote(E3, EIGHTH_NOTE)
    playNote(G3, EIGHTH_NOTE);  playNote(E3, EIGHTH_NOTE)
    playNote(D3, QUARTER_NOTE); rest(QUARTER_NOTE)
