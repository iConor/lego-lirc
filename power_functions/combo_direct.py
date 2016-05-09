"""LEGO Power Functions RC v1.20 - Combo Direct Mode"""

import power_functions.rc_protocol as pf_rc

# Output Data
OUTPUT = ["FLT",  # Float
          "FWD",  # Forward
          "REV",  # Backward
          "BRK"]  # Brake

def payload(channel, red, blue, _esc=pf_rc.ESC.MODE, _addr=pf_rc.ADDR.DEF):
    """Returns the payload for a Combo Direct Mode command."""
    nibble1 = _esc | channel
    nibble2 = _addr | pf_rc.MODE.DIR
    nibble3 = red | (blue << 2)
    nibble4 = pf_rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(channel, red, blue):
    """Returns the button for a Combo Direct Mode command."""
    return (pf_rc.CHANNEL[channel], OUTPUT[red], OUTPUT[blue])

def button_string(channel, red, blue):
    """Returns the string representation of Combo Direct Mode button."""
    return 'CH{:s}_{:s}_{:s}'.format(channel, red, blue)

def lirc_codes():
    """Prints LIRC codes for Combo Direct Mode."""
    for i in range(0, 4):
        for k in range(0, 16):
            red = k & 0x3
            blue = k >> 2
            hex_codes = pf_rc.payload_string(*payload(i, red, blue))
            lirc_patterns = button_string(*button(i, red, blue))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
