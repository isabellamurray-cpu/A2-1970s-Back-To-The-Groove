# Classic Rock Section 2 of 'Back to the Groove'

from tunepad.constants import *

# D major feel using only safe constants (no sharps/flats)
# I–V–IV (D–A–G) with simple diatonic approaches

# Main: 16 bars (2-bar phrase x8)
for _ in range(8):
    # bar 1: D → A → approach up to G
    playNote(D2, 1, 115); playNote(A2, 1, 110)
    playNote(E2, 0.5, 100); playNote(G2, 0.5, 108)   # approach to G (skip F#)
    playNote(G2, 1, 110); rest(1)

    # bar 2: A → (walk) → back to D
    playNote(A2, 1, 110); playNote(E2, 0.5, 100); playNote(G2, 0.5, 100)
    playNote(G2, 1, 108); playNote(B2, 0.5, 95); playNote(D2, 0.5, 115)

# Bridge: 8 bars (roots for drive)
for _ in range(8):
    playNote(D2, 1, 115); playNote(A2, 1, 112); playNote(G2, 1, 112); rest(1)

# Reprise: 8 bars (main riff again)
for _ in range(4):
    playNote(D2, 1, 115); playNote(A2, 1, 110); playNote(E2, 0.5, 100); playNote(G2, 0.5, 108)
    playNote(G2, 1, 110); rest(1)
    playNote(A2, 1, 110); playNote(E2, 0.5, 100); playNote(G2, 0.5, 100)
    playNote(G2, 1, 108); playNote(B2, 0.5, 95); playNote(D2, 0.5, 115)
