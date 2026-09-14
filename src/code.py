import board
import digitalio
import time
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# ==============================
# CONFIGURAÇÃO DA MATRIZ (61 TECLAS)
# ==============================

# Linhas (flat esquerdo) – OUTPUT
row_pins = [
    board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9
]

# Colunas (flat direito) – INPUT com pull-up
col_pins = [
    board.GP10, board.GP11, board.GP12, board.GP13,
    board.GP14, board.GP15, board.GP16, board.GP17
]

rows = []
cols = []

for pin in row_pins:
    r = digitalio.DigitalInOut(pin)
    r.direction = digitalio.Direction.OUTPUT
    r.value = True  # HIGH por padrão
    rows.append(r)

for pin in col_pins:
    c = digitalio.DigitalInOut(pin)
    c.direction = digitalio.Direction.INPUT
    c.pull = digitalio.Pull.UP
    cols.append(c)

# ==============================
# USB MIDI (CANAL 1)
# ==============================

midi = adafruit_midi.MIDI(
    midi_out=usb_midi.ports[1],
    out_channel=0  # Canal 1 (0-indexed)
)

# ==============================
# ESTADO DAS TECLAS
# ==============================

NUM_ROWS = 8
NUM_COLS = 8

key_state = [[False for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

BASE_NOTE = 36  # C2 (Dó 2)
MAX_NOTE = 96   # C7 (Dó 7)

DEBOUNCE_TIME = 0.005

# ==============================
# LOOP PRINCIPAL DE VARREDURA
# ==============================

while True:
    for row_index, row in enumerate(rows):
        # Ativa a linha atual (LOW)
        row.value = False
        time.sleep(DEBOUNCE_TIME)

        for col_index, col in enumerate(cols):
            pressed = not col.value  # LOW = pressionado (pull-up)
            note = BASE_NOTE + (row_index * 8) + col_index

            if note > MAX_NOTE:
                continue

            if pressed and not key_state[row_index][col_index]:
                midi.send(NoteOn(note, 127))
                key_state[row_index][col_index] = True

            elif not pressed and key_state[row_index][col_index]:
                midi.send(NoteOff(note, 0))
                key_state[row_index][col_index] = False

        # Desativa a linha (retorna para HIGH)
        row.value = True

    time.sleep(0.001)