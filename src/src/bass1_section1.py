# Funk/Disco Drums Section 1 of 'Back to the Groove'

from tunepad.constants import *
# Repeating 1970s style bass groove in A minor
for _ in range(4):  # repeat 4 times
    playNote(A2, QUARTER_NOTE, velocity=110)
    playNote(C3, EIGHTH_NOTE, velocity=100)
    playNote(D3, EIGHTH_NOTE, velocity=100)
    playNote(E3, QUARTER_NOTE, velocity=110)
    rest(QUARTER_NOTE)
