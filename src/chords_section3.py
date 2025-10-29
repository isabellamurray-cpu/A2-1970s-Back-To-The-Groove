# Jazz / Soul Section 3 of 'Back to the groove'

from tunepad.chords import *
from tunepad.constants import *

changeKey("C")

# Main: 16 bars (ii7 – V7 – I) with rolled/arpeggiated feel
for _ in range(4):
    playChord("ii7",   beats=2, playType="rolled",      octave=3, velocity=90)  # Dm7
    playChord("V7",    beats=2, playType="rolled",      octave=3, velocity=92)  # G7
    playChord("I",     beats=4, playType="arpeggio_up", octave=3, velocity=88)  # C triad

# Bridge: 8 bars (IV colour → ii–V–I)
for _ in range(2):
    playChord("IV",    beats=2, playType="block",  octave=3, velocity=90)  # F triad
    playChord("V7",    beats=2, playType="rolled", octave=3, velocity=92)
    playChord("I",     beats=4, playType="block",  octave=3, velocity=90)

# Outro: 16 beats (hold & fade)
playChord("I", beats=8, playType="rolled", octave=3, velocity=85)
playChord("I", beats=8, playType="rolled", octave=3, velocity=70)
