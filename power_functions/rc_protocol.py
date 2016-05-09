"""LEGO Power Functions RC v1.20 - RC Protocol"""

from collections import namedtuple

# Escape Bit Masks
Escape = namedtuple('Escape', ['MODE', 'PWM'])
ESC = Escape(0x0, 0x4)

# Channel Bit Masks
CHANNEL = ["1", "2", "3", "4"]

# Address Space Bit Masks
Address = namedtuple('Address', ['DEF', 'EXT'])
ADDR = Address(0x0, 0x8)

# Mode Selection Bit Masks
Mode = namedtuple('Mode', ['EXT', 'DIR', 'RSVD', 'SNGL'])
MODE = Mode(0x0, 0x1, 0x2, 0x4)

def lrc(nibble1, nibble2, nibble3):
    """Returns the "Longitudinal Redundancy Check" nibble."""
    return 0xf ^ nibble1 ^ nibble2 ^ nibble3

def payload_string(nibble1, nibble2, nibble3, nibble4):
    """Returns the string representation of a payload."""
    return'0x{:X}{:X}{:X}{:X}'.format(nibble1, nibble2, nibble3, nibble4)

def lirc_remote(author, mode):
    """Prints LIRC remote info for LEGO Power Functions RC."""
    name = mode.split()[0] + '_' + mode.split()[1]
    with open('power_functions/lirc_remote.txt') as source:
        with open('power_functions/' + name, 'w') as dest:
            for line in source:
                text = line.rstrip('\n')
                end = text[-4:]
                if end == 'd by':
                    text += ' ' + author
                elif end == 'ions':
                    text += ' ' + mode + ' Mode'
                elif end == 'EGO_':
                    text += name
                dest.write(text + '\n')
