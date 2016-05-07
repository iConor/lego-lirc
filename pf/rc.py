#################################
#
#   LEGO Power Functions RC v1.20
#
#   - LPF RC Protocol
#
#################################


#  Escape Bit Masks
#
class esc:
    MODE = 0x0 # Use 'Mode' below
    PWM  = 0x4 # Use Combo PWM mode


#  Channel Bit Masks
#
channel = ["1", "2", "3", "4"]


#  Address Space Bit Masks
#
class addr:
    DEF = 0x0 # Default
    EXT = 0x8 # Extended


#  Mode Selection Bit Masks
#
class mode:
    EXT  = 0x0 # Extended Mode
    DIR  = 0x1 # Combo Direct Mode
    RSVD = 0x2 # Reserved...
    SNGL = 0x4 # Single Output Mode


#  Returns the "Longitudinal Redundancy Check" nibble.
#
def lrc(nibble1, nibble2, nibble3):
    return 0xf ^ nibble1 ^ nibble2 ^ nibble3


#  Returns the string representation of a payload.
#
def payload_string(nib1, nib2, nib3, nib4):
    return'0x{:X}{:X}{:X}{:X}'.format(nib1, nib2, nib3, nib4)
