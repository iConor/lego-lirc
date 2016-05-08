"""LEGO Power Functions RC v1.20 - LPF RC Protocol"""

from collections import namedtuple

# Escape Bit Masks
Esc = namedtuple('Esc', ['MODE', 'PWM'])
ESC = Esc(0x0, 0x4)

# Channel Bit Masks
CHANNEL = ["1", "2", "3", "4"]

# Address Space Bit Masks
Addr = namedtuple('Addr', ['DEF', 'EXT'])
ADDR = Addr(0x0, 0x8)

# Mode Selection Bit Masks
Mode = namedtuple('Mode', ['EXT', 'DIR', 'RSVD', 'SNGL'])
MODE = Mode(0x0, 0x1, 0x2, 0x4)

def lrc(nibble1, nibble2, nibble3):
    """Returns the "Longitudinal Redundancy Check" nibble."""
    return 0xf ^ nibble1 ^ nibble2 ^ nibble3

def payload_string(nib1, nib2, nib3, nib4):
    """Returns the string representation of a payload."""
    return'0x{:X}{:X}{:X}{:X}'.format(nib1, nib2, nib3, nib4)
