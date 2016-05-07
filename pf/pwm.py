#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Combo PWM Mode
#
#################################


import rc


#  Data (PWM Steps)
#
steps = ["FLT",  # Float
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


#  Returns the payload for a Combo PWM Mode command.
#
def payload(_ch, _red, _blue, _esc=rc.esc.PWM, _addr=rc.addr.DEF):
    nibble1 = _addr | _esc | _ch
    nibble2 = _blue
    nibble3 = _red
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4


#  Returns the button for a Combo PWM Mode command.
#
def button(_ch, _red, _blue):
    return (rc.channel[_ch], steps[_red], steps[_blue])


#  Returns the string representation of a Combo PWM Mode button.
#
def button_string(ch, red, blue):
    return 'CH{:s}_{:s}_{:s}'.format(ch, red, blue)


#  Prints LIRC codes for Combo PWM Mode.
#
def lirc_codes():
    for i in range(0, 4):
        for j in range(0, 16):
            for k in range(0, 16):

                hex_codes = rc.payload_string(*payload(i, j, k))
                lirc_pattern = button_string(*button(i, j, k))
                print "\t{}\t\t{}".format(lirc_pattern, hex_codes)
