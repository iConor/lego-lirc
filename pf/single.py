#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Single Output Mode
#
#################################


import rc


#  Mode Bits
#
mode = ["PWM",    # Mode = PWM
        "CSTID"]  # Mode = Clear/Set/Toggle/Inc/Dec
output = ["RED",  # Output A
          "BLU"]  # Output B


#  Data if Mode = PWM
#
pwm = ["FLT",    # Float
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


#  Data if Mode = Clear/Set/Toggle/Inc/Dec
#
cstid = ["TGL_FWD",  # Toggle full forward
         "TGL_DIR",  # Toggle direction
         "INC_NUM",  # Increment numerical PWM
         "DEC_NUM",  # Decrement numerical PWM
         "INC_PWM",  # Increment PWM
         "DEC_PWM",  # Decrement PWM
         "FWD_TO",  # Full forward (timeout)
         "REV_TO",  # Full backward (timeout)
         "TGL_FR",  # Toggle full forward/backward
         "CLR_C1",   # Clear C1
         "SET_C1",   # Set C1
         "TGL_C1",   # Toggle C1
         "CLR_C2",   # Clear C2
         "SET_C2",   # Set C2
         "TGL_C2",   # Toggle C2
         "TGL_REV"]  # Toggle full backward


#  Returns the payload for a Single Output Mode command.
#
def payload(_ch, _mode, _out, _data, _esc=rc.esc.MODE, _addr=rc.addr.DEF):
    nibble1 = _esc | _ch
    nibble2 = _addr | rc.mode.SNGL | (_mode << 1) | _out
    nibble3 = _data
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4


#  Returns the button for a Single Output Mode command.
#
def button(_ch, _mode, _output, _data):

    if _mode == 0:
        data_ = pwm[_data]
    else:
        data_ = cstid[_data]

    return (rc.channel[_ch], output[_output], data_)


#  Returns the string representation of a Single Output Mode button.
#
def button_string(ch, output, data):
    return 'CH{:s}_{:s}_{:s}'.format(ch, output, data)


#  Prints LIRC codes for Single Output Mode.
#
def lirc_codes():
    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 16):

                mode = (j & 0x2) >> 1
                output = j & 0x1

                hex_codes = rc.payload_string(*payload(i, mode, output, k))
                lirc_patterns = button_string(*button(i, mode, output, k))
                print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
