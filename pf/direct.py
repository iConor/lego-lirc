#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Combo Direct Mode
#
#################################


import rc


#  Output Data
#
output = ["FLT",  # Float
          "FWD",  # Forward
          "REV",  # Backward
          "BRK"]  # Brake


#  Returns the payload for a Combo Direct Mode command.
#
def payload(_ch, _red, _blue, _esc=rc.esc.MODE, _addr=rc.addr.DEF):
    nibble1 = _esc | _ch
    nibble2 = _addr | rc.mode.DIR
    nibble3 = _red | (_blue << 2)
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4


#  Returns the button for a Combo Direct Mode command.
#
def button(_ch, _red, _blue):
    return (rc.channel[_ch], output[_red], output[_blue])


#  Returns the string representation of Combo Direct Mode button.
#
def button_string(ch, red, blue):
    return 'CH{:s}_{:s}_{:s}'.format(ch, red, blue)


#  Prints LIRC codes for Combo Direct Mode.
#
def lirc_codes():
    for i in range(0, 4):
        for k in range(0, 16):

            red = k & 0x3
            blue = k >> 2

            hex_codes = rc.payload_string(*payload(i, red, blue))
            lirc_patterns = button_string(*button(i, red, blue))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
