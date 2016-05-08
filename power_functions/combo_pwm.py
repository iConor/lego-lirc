"""LEGO Power Functions RC v1.20 - Combo PWM Mode"""

import power_functions.pf_rc_protocol as rc

# Data (PWM Steps)
STEPS = ["FLT",  # Float
         "FWD1",  # PWM forward, step 1
         "FWD2",  # PWM forward, step 2
         "FWD3",  # PWM forward, step 3
         "FWD4",  # PWM forward, step 4
         "FWD5",  # PWM forward, step 5
         "FWD6",  # PWM forward, step 6
         "FWD7",  # PWM forward, step 7
         "BRK",   # Brake then float
         "REV7",  # PWM backward, step 7
         "REV6",  # PWM backward, step 6
         "REV5",  # PWM backward, step 5
         "REV4",  # PWM backward, step 4
         "REV3",  # PWM backward, step 3
         "REV2",  # PWM backward, step 2
         "REV1"]  # PWM backward, step 1

def payload(_ch, _red, _blue, _esc=rc.ESC.PWM, _addr=rc.ADDR.DEF):
    """Returns the payload for a Combo PWM Mode command."""
    nibble1 = _addr | _esc | _ch
    nibble2 = _blue
    nibble3 = _red
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(_ch, _red, _blue):
    """Returns the button for a Combo PWM Mode command."""
    return (rc.CHANNEL[_ch], STEPS[_red], STEPS[_blue])

def button_string(ch_, red, blue):
    """Returns the string representation of a Combo PWM Mode button."""
    return 'CH{:s}_{:s}_{:s}'.format(ch_, red, blue)

def lirc_codes():
    """Prints LIRC codes for Combo PWM Mode."""
    for i in range(0, 4):
        for j in range(0, 16):
            for k in range(0, 16):
                hex_codes = rc.payload_string(*payload(i, j, k))
                lirc_pattern = button_string(*button(i, j, k))
                print "\t{}\t\t{}".format(lirc_pattern, hex_codes)
