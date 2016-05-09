"""LEGO Power Functions RC v1.20 - Single Output Mode"""

import power_functions.rc_protocol as pf_rc

# Mode Bits
MODE = ["PWM",    # Mode = PWM
        "CSTID"]  # Mode = Clear/Set/Toggle/Inc/Dec
OUTPUT = ["RED",  # Output A
          "BLU"]  # Output B

# Data if Mode = PWM
PWM = ["FLT",    # Float
       "FWD_1",  # PWM forward, step 1
       "FWD_2",  # PWM forward, step 2
       "FWD_3",  # PWM forward, step 3
       "FWD_4",  # PWM forward, step 4
       "FWD_5",  # PWM forward, step 5
       "FWD_6",  # PWM forward, step 6
       "FWD_7",  # PWM forward, step 7
       "BRK",    # Brake then float
       "REV_7",  # PWM backward, step 7
       "REV_6",  # PWM backward, step 6
       "REV_5",  # PWM backward, step 5
       "REV_4",  # PWM backward, step 4
       "REV_3",  # PWM backward, step 3
       "REV_2",  # PWM backward, step 2
       "REV_1"]  # PWM backward, step 1


# Data if Mode = Clear/Set/Toggle/Inc/Dec
CSTID = ["TGL_FWD",  # Toggle full forward
         "TGL_DIR",  # Toggle direction
         "INC_NUM",  # Increment numerical PWM
         "DEC_NUM",  # Decrement numerical PWM
         "INC_PWM",  # Increment PWM
         "DEC_PWM",  # Decrement PWM
         "FWD_TO",   # Full forward (timeout)
         "REV_TO",   # Full backward (timeout)
         "TGL_FR",   # Toggle full forward/backward
         "CLR_C1",   # Clear C1
         "SET_C1",   # Set C1
         "TGL_C1",   # Toggle C1
         "CLR_C2",   # Clear C2
         "SET_C2",   # Set C2
         "TGL_C2",   # Toggle C2
         "TGL_REV"]  # Toggle full backward

def payload(channel, mode, output, data, _esc=pf_rc.ESC.MODE, _addr=pf_rc.ADDR.DEF):
    """Returns the payload for a Single Output Mode command."""
    nibble1 = _esc | channel
    nibble2 = _addr | pf_rc.MODE.SNGL | (mode << 1) | output
    nibble3 = data
    nibble4 = pf_rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4

def button(channel, mode, output, data):
    """Returns the button for a Single Output Mode command."""
    if mode == 0:
        data = PWM[data]
    else:
        data = CSTID[data]
    return (pf_rc.CHANNEL[channel], OUTPUT[output], data)

def button_string(channel, output, data):
    """Returns the string representation of a Single Output Mode button."""
    return 'CH{:s}_{:s}_{:s}'.format(channel, output, data)

def lirc_codes():
    """Prints LIRC codes for Single Output Mode."""
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 16):
                mode = (j & 0x2) >> 1
                output = j & 0x1
                hex_codes = pf_rc.payload_string(*payload(i, mode, output, k))
                lirc_patterns = button_string(*button(i, mode, output, k))
                print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
