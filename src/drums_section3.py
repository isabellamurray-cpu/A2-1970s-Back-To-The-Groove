# Jazz / Soul Section 3 of 'Back to the groove'

from tunepad.constants import *

# Soft brush kit feel + ghost notes + crescendo into outro
# Main: 16 bars
for bar in range(16):
    playNote(36, 1, 100); playNote(42, 0.5, 70); playNote(42, 0.5, 70)
    playNote(38, 1, 90);  playNote(42, 0.5, 70); playNote(42, 0.5, 70)
    playNote(36, 1, 100); playNote(42, 0.5, 70); playNote(42, 0.5, 70)
    # beat 4 with ghost every other bar
    if bar % 2 == 0:
        playNote(37, 0.5, 60); playNote(38, 0.5, 90)
    else:
        playNote(38, 1, 90)
# -- Bridge: 8 bars (ride pattern)
for bar in range(8):
    playNote(36, 1, 98);  playNote(51, 0.5, 75); playNote(51, 0.5, 75)  # ride cym
    playNote(38, 1, 88);  playNote(51, 0.5, 75); playNote(51, 0.5, 75)
    playNote(36, 1, 98);  playNote(51, 0.5, 75); playNote(51, 0.5, 75)
    playNote(38, 1, 88);  playNote(51, 0.5, 75); playNote(51, 0.5, 75)
# -- Outro: 8 bars (fade softness)
for v in [85,80,75,70,65,60,55,50]:
    playNote(36, 1, v); playNote(42, 0.5, v-20); playNote(42, 0.5, v-20)
    playNote(38, 1, v-10); playNote(42, 0.5, v-20); playNote(42, 0.5, v-20)
    playNote(36, 1, v); playNote(42, 0.5, v-20); playNote(42, 0.5, v-20)
    playNote(38, 1, v-10)
