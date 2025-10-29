# Classic Rock Section 2 of 'Back to the Groove'

from tunepad.chords import *
from tunepad.constants import *

changeKey("D")

# Main: 16 bars (I–V–IV)
for _ in range(4):
    playChord("I",  beats=2, playType="block",  octave=3, velocity=112)
    playChord("V",  beats=2, playType="block",  octave=3, velocity=112)
    playChord("IV", beats=3, playType="rolled", octave=3, velocity=108); rest(1)

# Bridge: 8 bars (ii–V–I colour)
for _ in range(2):
    playChord("ii", beats=2, playType="rolled",  octave=4, velocity=108)  # Em
    playChord("V",  beats=2, playType="block",   octave=3, velocity=112)  # A
    playChord("I",  beats=4, playType="block",   octave=3, velocity=114)  # D

# Reprise: 8 bars
for _ in range(2):
    playChord("I",  beats=2, playType="block",  octave=3, velocity=114)
    playChord("V",  beats=2, playType="block",  octave=3, velocity=114)
    playChord("IV", beats=3, playType="rolled", octave=3, velocity=110); rest(1)
