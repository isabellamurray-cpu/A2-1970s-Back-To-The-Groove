# Funk/Disco Chords Section 1 of 'Back to the Groove'

# 1970s Chords / Keys 
from tunepad.chords import *       # Gives access to changeKey() and playChord()
from tunepad.constants import *    # Gives access to durations and velocity values

# Set key to A minor (for a funky/soul feel)
changeKey("Am")

# 4 bars of Am–F–G–Em repeated twice
for _ in range(2):
    playChord("i",   2, playType="block",  octave=3, velocity=100)
    playChord("VI",  2, playType="block",  octave=3, velocity=100)
    playChord("VII", 2, playType="block",  octave=3, velocity=100)
    playChord("v",   2, playType="block",  octave=3, velocity=100)
