import usb_midi
import usb_cdc

# Ativa a interface de áudio/instrumento USB-MIDI nativa
usb_midi.enable()

# Desativa a porta serial CDC para o computador reconhecer imediatamente como instrumento MIDI
usb_cdc.disable()
