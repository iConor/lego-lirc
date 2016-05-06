#ifndef Generate_h
#define Generate_h

#include <string>

/*
 *  Address Space
 *  - Default or Extended
 */
const std::string[] ADDR = {"DEF, EXT"};

/*
 *  Available Channels
 */
const std::string[] CH = {"1", "2", "3", "4"};

/*
 *  Extended Mode
 *  - Functions
 */
const std::string[] FUNCTIONS = {"BRK_A", "INC_A", "DEC_A",
                                 "NOT_USED", "TGL_B", "NOT_USED",
                                 "TGL_ADR", "ALN_TGL", "RESERVED"};

/*
 *  Combo Direct
 *  - Output Data
 */
const std::string[] DIRECT_DATA = {"FLT", "FWD", "REV", "BRK"};

/*
 *  Single Output
 *  - Modes and Outputs
 */
const std::string[] SINGLE_MODE = {"PWM", "CSTID"};
const std::string[] SINGLE_OUTPUT = {"RED", "BLUE"}; // A, B

/*
 *  Single Output & Combo PWM
 *  - PWM Output Data
 */
const std::string[] PWM = {"FLT", "FWD1", "FWD2", "FWD3",
                           "FWD4", "FWD5","FWD6", "FWD7",
                           "BRK ", "REV7", "REV6", "REV5",
                           "REV4", "REV3", "REV2", "REV1"};

/*
 *  Single Output (CSTID)
 *  - Clear/Set/Toggle/Inc/Dec Data
 */
const std::string[] CSTID = {"TGL_FWD", "TGL_DIR", "NINC_PWM", "NDEC_PWM",
                             "INC_PWM", "DEC_PWM", "FWD_TIME", "REV_TIME",
                             "TGL_FWRV", "CLR_C1 ", "SET_C1 ", "TGL_C1 ",
                             "CLR_C2 ", "SET_C2 ", "TGL_C2 ", "TGL_REV"};


int printExtended();
int printComboDirect();
int printSingle();
int printComboPWM();
int lrc(int[] payload)

#endif
