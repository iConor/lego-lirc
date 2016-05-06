#################################
#
#   LEGO Power Functions RC v1.20
#
#################################

#  Escape Bit
#
escape = ["MODE",  # Use 'Mode' below
          "PWM"]   # Use Combo PWM mode

#  Channel Bits
#
channel = ["1", "2", "3", "4"]

#  Address Space Bit
#
address = ["DEF",  # Default
           "EXT"]  # Extended

#  Returns the "Longitudinal Redundancy Check" nibble.
#
def lrc(nib1, nib2, nib3):
    return 0xf ^ nib1 ^ nib2 ^ nib3
