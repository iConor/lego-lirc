#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Extended Mode
#
#################################


import pf_rc_protocol as rc


#  Function Data
#
functions = ["BRK_A",     # Brake then float A
             "INC_A",     # Increment speed on A
             "DEC_A",     # Decrement speed on A
             "NOT_USED",  # ...
             "TGL_B",     # Toggle forward/float on B
             "NOT_USED",  # ...
             "TGL_ADR",   # Toggle address bit
             "ALN_TGL",   # Align toggle bit (get in sync)
             "RESERVED"]  # ...


#  Returns the payload for an Extended Mode command.
#
def payload(_ch, _fn, _esc=rc.esc.MODE, _addr=rc.addr.DEF):
    nibble1 = _esc | _ch
    nibble2 = _addr | rc.mode.EXT
    nibble3 = _fn
    nibble4 = rc.lrc(nibble1, nibble2, nibble3)
    return nibble1, nibble2, nibble3, nibble4


#  Returns the button for an Extended Mode command.
#
def button(_ch, _fn):
    return (rc.channel[_ch], functions[_fn])


#  Returns the string representation of an Extended Mode button.
#
def button_string(ch, fn):
    return 'CH{:s}_{:s}'.format(ch, fn)


#  Prints LIRC codes for Extended Mode.
#
def lirc_codes():
    for i in range(0, 4):
        for k, func in enumerate(functions):
            if func == "NOT_USED" or func == "RESERVED":
                continue

            hex_codes = rc.payload_string(*payload(i, k))
            lirc_patterns = button_string(*button(i, k))
            print "\t{}\t\t{}".format(lirc_patterns, hex_codes)
