#################################
#
#   LEGO Power Functions RC v1.20
#
#   - Extended Mode
#
#################################

#  Mode Bits
#
mode = 0x0;

#  Function Bits
#
function = ["BRK_A",     # Brake then float A
            "INC_A",     # Increment speed on A
            "DEC_A",     # Decrement speed on A
            "NOT_USED",  # ...
            "TGL_B",     # Toggle forward/float on B
            "NOT_USED",  # ...
            "TGL_ADR",   # Toggle address bit
            "ALN_TGL",   # Align toggle bit (get in sync)
            "RESERVED"]  # ...
