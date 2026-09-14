# 🎹 Raspberry Pi Pico USB-MIDI Mechanical Controller

[![Microcontroller](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Pico%20(RP2040)-C51A4A.svg)](https://raspberrypi.com/)
[![Runtime](https://img.shields.io/badge/Firmware-CircuitPython%2010.x-306998.svg)](https://circuitpython.org/)
[![Protocol](https://img.shields.io/badge/Protocol-USB%20MIDI%20Class%20Compliant-orange.svg)](https://midi.org/)
[![DAW](https://img.shields.io/badge/DAW-GarageBand%20%7C%20Logic%20Pro%20%7C%20Ableton-purple.svg)]()

> **Controlador musical USB-MIDI físico desenvolvido com o microcontrolador RP2040 (Raspberry Pi Pico)**. O dispositivo funciona de forma nativa (*plug-and-play*) em macOS, Windows, Linux e iOS/iPadOS, enviando mensagens MIDI padrão de `NoteOn` e `NoteOff` para softwares de produção musical e sintetizadores, além de contar com um gerador acústico PWM local integrado.

---

## ✨ Recursos

- **Plug-and-Play USB MIDI**: Reconhecido automaticamente pelo sistema operacional sem necessidade de drivers proprietários (compatível com CoreMIDI no macOS/iOS).
- **Escala Diatônica Completa (Dó Maior / C Major)**: 7 teclas mapeadas com resistores internos de pull-up para digitação rápida e responsiva.
- **Transposição Dinâmica de Oitavas**: Botões de `Octave Up` e `Octave Down` permitindo transitar por 7 oitavas completas (alcance de $C_1$ a $B_7$).
- **Sintetizador de Feedback Sonoro (PWM Buzzer)**: Conversão matemática em tempo real do número da nota MIDI para frequência acústica em Hertz ($f = 440 \cdot 2^{\frac{n - 69}{12}}$), permitindo praticar mesmo sem fones ou caixas de som conectadas ao computador.
- **Debounce por Software**: Algoritmo de filtragem temporal para eliminar falsos disparos provocados pelo repique mecânico dos switches.

---

## 🔌 Pinout & Mapeamento de Teclas

| Função | Pino GPIO Pico | Tipo | Nota Padrão (Oitava 0) | Frequência Acústica |
|---|---|---|---|---|
| **Nota 1** | `GP2` | Entrada (Pull-Up) | Dó 4 ($C_4$ / MIDI 60) | 261.63 Hz |
| **Nota 2** | `GP3` | Entrada (Pull-Up) | Ré 4 ($D_4$ / MIDI 62) | 293.66 Hz |
| **Nota 3** | `GP4` | Entrada (Pull-Up) | Mi 4 ($E_4$ / MIDI 64) | 329.63 Hz |
| **Nota 4** | `GP5` | Entrada (Pull-Up) | Fá 4 ($F_4$ / MIDI 65) | 349.23 Hz |
| **Nota 5** | `GP6` | Entrada (Pull-Up) | Sol 4 ($G_4$ / MIDI 67) | 392.00 Hz |
| **Nota 6** | `GP7` | Entrada (Pull-Up) | Lá 4 ($A_4$ / MIDI 69) | 440.00 Hz |
| **Nota 7** | `GP8` | Entrada (Pull-Up) | Si 4 ($B_4$ / MIDI 71) | 493.88 Hz |
| **Subir Oitava** | `GP9` | Entrada (Pull-Up) | $+1$ Oitava ($+12$ semitons) | — |
| **Descer Oitava** | `GP10` | Entrada (Pull-Up) | $-1$ Oitava ($-12$ semitons) | — |
| **Buzzer Sintetizador**| `GP15` | Saída PWM | Alto-falante / Piezo | Frequência dinâmica |

---

## 📂 Estrutura do Repositório

```bash
pico-midi-mechanical-keyboard/
├── src/
│   └── code.py                  # Script principal CircuitPython (detecção e disparo MIDI)
└── hardware/
    └── PINOUT RASPBERRY PI PICO.png # Esquema visual de pinagem da placa
```

---

## 🚀 Como Instalar e Usar

1. Conecte o **Raspberry Pi Pico** ao computador segurando o botão `BOOTSEL`.
2. Instale o firmware do **CircuitPython 9.x ou 10.x** arrastando o arquivo `.uf2` para a unidade `RPI-RP2`.
3. Na unidade montada `CIRCUITPY`:
   - Copie a biblioteca `adafruit_midi` para a pasta `/lib`.
   - Copie o arquivo `src/code.py` para a raiz da unidade.
4. Abra sua DAW favorita (**Apple Logic Pro, GarageBand, Ableton Live ou FL Studio**) e comece a tocar!

---

## 👨‍💻 Autor

Desenvolvido por **Enzo Grasciano de Figueiredo**  
Universidade Federal do Paraná (UFPR)  
E-mail: enzo.g.figueiredo@gmail.com  
GitHub: [@enzo-grasciano-de-figueiredo](https://github.com/enzo-grasciano-de-figueiredo)
