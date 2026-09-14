import board
import digitalio
import time
import pwmio
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# Define pins for 7 note buttons
note_pins = [board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8]
note_buttons = []

# Define octave control buttons
octave_up = digitalio.DigitalInOut(board.GP9)
octave_down = digitalio.DigitalInOut(board.GP10)

# Setup octave buttons with pull-up
octave_up.switch_to_input(pull=digitalio.Pull.UP)
octave_down.switch_to_input(pull=digitalio.Pull.UP)

# Setup 7 note buttons with pull-up
for pin in note_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.switch_to_input(pull=digitalio.Pull.UP)
    note_buttons.append(btn)

# PWM for speaker on GP15
buzzer = pwmio.PWMOut(board.GP15, duty_cycle=0, frequency=440, variable_frequency=True)

# MIDI setup
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

# C major scale notes (MIDI numbers for C4 to B4)
note_numbers = [60, 62, 64, 65, 67, 69, 71]

# Octave state
octave_shift = 0
last_button_states = [True]*7  # All start unpressed (True = not pressed with pull-up)
note_playing = [False]*7

while True:
    # Handle octave buttons (pressed = LOW)
    if not octave_up.value:
        octave_shift = min(octave_shift + 1, 3)  # Limit to 3 octaves up
        time.sleep(0.3)  # Debounce
    if not octave_down.value:
        octave_shift = max(octave_shift - 1, -3)  # Limit to 3 octaves down
        time.sleep(0.3)

    # Handle 7 note buttons
    for i, btn in enumerate(note_buttons):
        current_state = btn.value  # True when not pressed, False when pressed
        note = note_numbers[i] + (12 * octave_shift)

        if not current_state and last_button_states[i]:  # Button pressed
            midi.send(NoteOn(note, 127))
            buzzer.frequency = int(440 * 2 ** ((note - 69) / 12))  # Convert MIDI note to Hz
            buzzer.duty_cycle = 32768
            note_playing[i] = True

        elif current_state and not last_button_states[i]:  # Button released
            midi.send(NoteOff(note, 0))
            buzzer.duty_cycle = 0
            note_playing[i] = False

        last_button_states[i] = current_state

    time.sleep(0.01)