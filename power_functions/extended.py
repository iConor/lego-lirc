"""LEGO Power Functions RC v1.20 - Extended Mode"""

import power_functions.pf_rc_protocol as rc

# Function Data
FUNCTIONS = ["BRK_A",     # Brake then float A
             "INC_A",     # Increment speed on A
             "DEC_A",     # Decrement speed on A
             "NOT_USED",  # ...
             "TGL_B",     # Toggle forward/float on B
             "NOT_USED",  # ...
             "TGL_ADR",   # Toggle address bit
             "ALN_TGL",   # Align toggle bit (get in sync)
             "RESERVED"]  # ...

def payload(_ch, _fn, _esc=rc.ESC.MODE, _addr=rc.ADDR.DEF):
    """Returns the payload for an Extended Mode command."""
    nibble1 = _esc | _ch
    nibble2 = _addr | rc.MODE.EXT
    nibble3 = _fn
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(_ch, _fn):
    """ Returns the button for an Extended Mode command."""
    return (rc.CHANNEL[_ch], FUNCTIONS[_fn])

def button_string(ch_, fn_):
    """Returns the string representation of an Extended Mode button."""
    return 'CH{:s}_{:s}'.format(ch_, fn_)

def lirc_codes():
    """Prints LIRC codes for Extended Mode."""
    for i in range(0, 4):
        for k, func in enumerate(FUNCTIONS):
            if func == "NOT_USED" or func == "RESERVED":
                continue
            hex_codes = rc.payload_string(*payload(i, k))
            lirc_patterns = button_string(*button(i, k))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
