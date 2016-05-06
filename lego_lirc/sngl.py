#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Single Output Mode
#
#################################

#  Mode Bits
#
mode = 0x4;         # Always set
submode = ["PWM",     # Mode = PWM
           "CSTID"]   # Mode = Clear/Set/Toggle/Inc/Dec
output = ["RED",    # Output A
          "BLUE"]   # Output B

#  Data if Mode = PWM
#
pwm = ["FLT",   # Float
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

#  Data if Mode = Clear/Set/Toggle/Inc/Dec
#
cstid = ["TGL_FWD",   # Toggle full forward
         "TGL_DIR",   # Toggle direction
         "NINC_PWM",  # Increment numerical PWM
         "NDEC_PWM",  # Decrement numerical PWM
         "INC_PWM",   # Increment PWM
         "DEC_PWM",   # Decrement PWM
         "FWD_TIME",  # Full forward (timeout)
         "REV_TIME",  # Full backward (timeout)
         "TGL_FR",    # Toggle full forward/backward
         "CLR_C1",    # Clear C1
         "SET_C1",    # Set C1
         "TGL_C1",    # Toggle C1
         "CLR_C2",    # Clear C2
         "SET_C2",    # Set C2
         "TGL_C2",    # Toggle C2
         "TGL_REV"]   # Toggle full backward
