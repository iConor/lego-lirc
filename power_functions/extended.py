"""LEGO Power Functions RC v1.20 - Extended Mode"""

import power_functions.rc_protocol as pf_rc

# Function Data
FUNCTION = ["BRK_A",     # Brake then float A
            "INC_A",     # Increment speed on A
            "DEC_A",     # Decrement speed on A
            "NOT_USED",  # ...
            "TGL_B",     # Toggle forward/float on B
            "NOT_USED",  # ...
            "TGL_ADR",   # Toggle address bit
            "ALN_TGL",   # Align toggle bit (get in sync)
            "RESERVED"]  # ...

def payload(channel, function, _esc=pf_rc.ESC.MODE, _addr=pf_rc.ADDR.DEF):
    """Returns the payload for an Extended Mode command."""
    nibble1 = _esc | channel
    nibble2 = _addr | pf_rc.MODE.EXT
    nibble3 = function
    nibble4 = pf_rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(channel, function):
    """ Returns the button for an Extended Mode command."""
    return (pf_rc.CHANNEL[channel], FUNCTION[function])

def button_string(channel, function):
    """Returns the string representation of an Extended Mode button."""
    return 'CH{:s}_{:s}'.format(channel, function)

def lirc_codes():
    """Prints LIRC codes for Extended Mode."""
    for i in range(0, 4):
        for k, func in enumerate(FUNCTION):
            if func == "NOT_USED" or func == "RESERVED":
                continue
            hex_codes = pf_rc.payload_string(*payload(i, k))
            lirc_patterns = button_string(*button(i, k))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
