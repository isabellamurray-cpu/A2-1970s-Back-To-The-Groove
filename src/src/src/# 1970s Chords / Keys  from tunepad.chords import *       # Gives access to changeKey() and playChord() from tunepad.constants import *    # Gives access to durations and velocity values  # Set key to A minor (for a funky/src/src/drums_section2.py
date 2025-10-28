# Classic Rock Drums Section 2 of 'Back to the Groove'

from tunepad.constants import *
# Crash in
playNote(49, QUARTER_NOTE, velocity=120); rest(3)  # crash + three beats rest

# --- Main groove: 16 bars (kick on 1&3, snare on 2&4, hats 8ths) ---
for bar in range(16):
    # beat 1
    playNote(36, QUARTER_NOTE, 120)   # kick
    playNote(42, 0.5, 85); playNote(42, 0.5, 85)  # hats
    # beat 2
    playNote(38, QUARTER_NOTE, 115)   # snare
    playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    # beat 3
    playNote(36, QUARTER_NOTE, 120)
    playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    # beat 4
    playNote(38, QUARTER_NOTE, 115)
    playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    # tiny fill every 4 bars
    if bar % 4 == 3:
        playNote(45, 0.5, 105); playNote(47, 0.5, 105)  # toms

# Bridge: 8 bars (open-hat lift + tom fill into downbeat)
for bar in range(8):
    playNote(36, QUARTER_NOTE, 118)
    playNote(46, 0.5, 95); playNote(46, 0.5, 95)  # OPEN hat
    playNote(38, QUARTER_NOTE, 112)
    playNote(46, 0.5, 95); playNote(46, 0.5, 95)
    playNote(36, QUARTER_NOTE, 118)
    playNote(46, 0.5, 95); playNote(46, 0.5, 95)
    playNote(38, QUARTER_NOTE, 112)
    playNote(46, 0.5, 95); playNote(46, 0.5, 95)
    if bar == 7:
        playNote(45, 0.5, 108); playNote(47, 0.5, 108); playNote(50, 0.5, 110)
        playNote(49, QUARTER_NOTE, 120)  # crash back into main

# Main reprise: 8 bars (back to closed hats)
for bar in range(8):
    playNote(36, QUARTER_NOTE, 120); playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    playNote(38, QUARTER_NOTE, 115); playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    playNote(36, QUARTER_NOTE, 120); playNote(42, 0.5, 85); playNote(42, 0.5, 85)
    playNote(38, QUARTER_NOTE, 115); playNote(42, 0.5, 85); playNote(42, 0.5, 85)
