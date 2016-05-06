####################################
#
#   LEGO Power Functions RC Protocol
#
####################################

class Protocol:
    # Escape Bit`
    escape = ["MODE",  # Use 'Mode' below
              "PWM"]   # Use Combo PWM mode

    #  Channel Bits
    channel = ["1", "2", "3", "4"]

    #  Address Space Bit
    address = ["DEF",  # Default
               "EXT"]  # Extended

class Extended:
    # Mode Bits
    mode_mask = 0x0;
    # Function Bits
    function = ["BRK_A",     # Brake then float A
                "INC_A",     # Increment speed on A
                "DEC_A",     # Decrement speed on A
                "NOT_USED",  # ...
                "TGL_B",     # Toggle forward/float on B
                "NOT_USED",  # ...
                "TGL_ADR",   # Toggle address bit
                "ALN_TGL",   # Align toggle bit (get in sync)
                "RESERVED"]  # ...

class ComboDirect:
    # Mode Bits
    mode_mask = 0x1;
    # Data Bits
    data = ["FLT",  # Float
            "FWD",  # Forward
            "REV",  # Backward
            "BRK"]  # Brake

class SingleOutput:
    # Mode Bits
    mode_mask = 0x4;   # Always set
    mode = ["PWM",     # Mode = PWM
            "CSTID"]   # Mode = Clear/Set/Toggle/Inc/Dec
    output = ["RED",   # Output A
              "BLUE"]  # Output B
    # Data if Mode = PWM
    pwm = ["FLT", "FWD1", "FWD2", "FWD3", "FWD4", "FWD5","FWD6", "FWD7",  "REV4", "REV3", "REV2", "REV1"]
    # Data if Mode = Clear/Set/Toggle/Inc/Dec
    cstid = ["TGL_FWD", "TGL_DIR", "NINC_PWM", "NDEC_PWM", "INC_PWM", "DEC_PWM", "FWD_TIME", "REV_TIME", "TGL_FWRV", "CLR_C1 ", "SET_C1 ", "TGL_C1 ", "CLR_C2 ", "SET_C2 ", "TGL_C2 ", "TGL_REV"]

class ComboPWM:
    # Data (same as SingleOutput in PWM Mode)
    pwm = SingleOutput.pwm
