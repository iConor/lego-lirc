"""LEGO Power Functions RC v1.20 - Combo PWM Mode"""

import power_functions.rc_protocol as pf_rc

# Data (PWM Steps)
PWM_STEP = ["FLT",   # Float
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

def payload(channel, red, blue, _esc=pf_rc.ESC.PWM, _addr=pf_rc.ADDR.DEF):
    """Returns the payload for a Combo PWM Mode command."""
    nibble1 = _addr | _esc | channel
    nibble2 = blue
    nibble3 = red
    nibble4 = pf_rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(channel, red, blue):
    """Returns the button for a Combo PWM Mode command."""
    return (pf_rc.CHANNEL[channel], PWM_STEP[red], PWM_STEP[blue])

def button_string(channel, red, blue):
    """Returns the string representation of a Combo PWM Mode button."""
    return 'CH{:s}_{:s}_{:s}'.format(channel, red, blue)

def lirc_codes():
    """Prints LIRC codes for Combo PWM Mode."""
    for i in range(0, 4):
        for j in range(0, 16):
            for k in range(0, 16):
                hex_codes = pf_rc.payload_string(*payload(i, j, k))
                lirc_pattern = button_string(*button(i, j, k))
                print "\t{}\t\t{}".format(lirc_pattern, hex_codes)
