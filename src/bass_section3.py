# Jazz / Soul Section 3 of 'Back to the groove'

from tunepad.constants import *

# Walking flavour outlining ii–V–I in C major without accidentals
# Main: 16 bars (two-bar cycle x8)
for _ in range(8):
    # Dm7 (D F A C) then head to G
    playNote(D2,0.5,95); playNote(F2,0.5,95); playNote(A2,0.5,95); playNote(C3,0.5,95)
    playNote(B2,0.5,95); playNote(A2,0.5,95); playNote(G2,0.5,95); rest(0.5)
    # G7 (G B D F) resolve to C
    playNote(G2,0.5,95); playNote(B2,0.5,95); playNote(D3,0.5,95); playNote(F3,0.5,95)
    playNote(E3,0.5,95); playNote(D3,0.5,95); playNote(C3,0.5,100); rest(0.5)

# Bridge: 8 bars (roots to open space)
for _ in range(8):
    playNote(D2,1,92); playNote(G2,1,92); playNote(C2,1,94); rest(1)

# Outro: 8 bars descending
for _ in range(2):
    playNote(C3,1,90); playNote(B2,1,88); playNote(A2,1,86); playNote(G2,1,84)
