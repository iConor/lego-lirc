"""LEGO Power Functions RC v1.20 - Combo Direct Mode"""

import power_functions.pf_rc_protocol as rc

# Output Data
OUTPUT = ["FLT",  # Float
          "FWD",  # Forward
          "REV",  # Backward
          "BRK"]  # Brake

def payload(_ch, _red, _blue, _esc=rc.ESC.MODE, _addr=rc.ADDR.DEF):
    """Returns the payload for a Combo Direct Mode command."""
    nibble1 = _esc | _ch
    nibble2 = _addr | rc.MODE.DIR
    nibble3 = _red | (_blue << 2)
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(_ch, _red, _blue):
    """Returns the button for a Combo Direct Mode command."""
    return (rc.CHANNEL[_ch], OUTPUT[_red], OUTPUT[_blue])

def button_string(ch_, red, blue):
    """Returns the string representation of Combo Direct Mode button."""
    return 'CH{:s}_{:s}_{:s}'.format(ch_, red, blue)

def lirc_codes():
    """Prints LIRC codes for Combo Direct Mode."""
    for i in range(0, 4):
        for k in range(0, 16):
            red = k & 0x3
            blue = k >> 2
            hex_codes = rc.payload_string(*payload(i, red, blue))
            lirc_patterns = button_string(*button(i, red, blue))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
