public class Generate {

	public static void main(String[] args) {
		extendedMode();
		//comboDirect();
		//singleOutput();
		// comboPWM();
	}

	/**
	 * Generates LEGO LIRC codes for Extended Mode.
	 */
	static void extendedMode() {
		// Array of Extended mode functions names.
		String[] function = {"B-F_A","INC_A", "DEC_A", "NOT_USED", "TGL_B", "NOT_USED", "TGL_ADR", "ALN_TGL", "RESERVED"};
		// Nibble 1 -- Toggle = 0, Escape = 0, Channel = #, Channel = #.
		for (int nibble1 = 0; nibble1 < 4; nibble1++) { // 4 to 7 is ch1 to ch4
			// Nibble 2 -- Address = 0, Mode = 0, Mode = 0, Mode = 0.
			int nibble2 = 0; // = 0
			// Nibble 3 -- Outputs: 0b0000 through 0b1000.
			for (int nibble3 = 0; nibble3 < 9; nibble3++) {
				if(function[nibble3]=="NOT_USED" || function[nibble3]=="RESERVED"){
					continue;
				}
				// Print name of function.
				System.out.print("\tCH" + nibble1 + "_" + function[nibble3]);
				// Print hex formatted code:
				System.out.print("\t\t0x");
				System.out.print(nibble1);
				System.out.print(nibble2);
				System.out.print(nibble3);
				// LRC = 0xF xor Nibble 1 xor Nibble 2 xor Nibble 3
				System.out.println(Integer.toHexString(
						0xF ^ nibble1 ^ nibble2 ^ nibble3).toUpperCase());
			}
		}
	}

	/**
	 * Generates LEGO LIRC codes for Combo Direct Mode.
	 */
	static void comboDirect() {
		// Nibble 1 -- Toggle = 0, Escape = 0, Channel = #, Channel = #.
		for (int nibble1 = 0; nibble1 < 4; nibble1++) { // 4 to 7 is ch1 to ch4
			// Nibble 2 -- Address = 0, Mode = 0, Mode = 0, Mode = 1.
			int nibble2 = 1; // = 1
			// Nibble 3 -- Outputs: 0b0000 through 0b1111 (0bBBAA).
			for (int nibble3 = 0; nibble3 < 16; nibble3++) {
				// Output B -- Nibble 3: 0b##xx.
				int b = nibble3 >> 2;
				// Output A -- Nibble 3: 0bxx##.
				int a = nibble3 % 4;
				// Print name of code ("(ch#)"_"B"_"A"), see codeName().
				System.out.print("\t" + (nibble1 + 1) + "_" + codeName(b) + "_"
						+ codeName(a));
				// Print hex formatted code:
				System.out.print("\t\t0x");
				System.out.print(nibble1);
				System.out.print(nibble2);
				System.out.print(Integer.toHexString(nibble3).toUpperCase());
				// LRC = 0xF xor Nibble 1 xor Nibble 2 xor Nibble 3
				System.out.println(Integer.toHexString(
						0xF ^ nibble1 ^ nibble2 ^ nibble3).toUpperCase());
			}
		}
	}

	/**
	 * Generates name of a code represented by half a nibble.
	 * 
	 * @param nib
	 *            Two bits. Half of Nibble 3. Output A or B.
	 * @return cmd String. Name of command represented by nib.
	 */
	static String codeName(int nib) {
		String cmd;
		if (nib == 0) {
			cmd = "FLOAT";
		} else if (nib == 1) {
			cmd = "FORWARD";
		} else if (nib == 2) {
			cmd = "BACKWARD";
		} else {
			cmd = "BRAKE";
		}
		return cmd;
	}

	/**
	 * Generates codes for single output mode
	 */
	static void singleOutput() {
		// Nibble 1 -- Address = 0, Escape = 0, Channel = #, Channel = #.
		for (int nibble1 = 0; nibble1 < 4; nibble1++) {
			// Nibble 2 -- Output A/B: 0b0100 through 0b0101.
			for (int nibble2 = 4; nibble2 <= 5; nibble2++) {
				// Nibble 3 -- Output A: 0b0000 through 0b1111.
				for (int nibble3 = 0; nibble3 < 16; nibble3++) {
					// Print name of code (raw hex string).
					System.out.print("\t");
					System.out.print((nibble1 & 3) + 1); // Channel
					System.out.print((nibble2 & 1) == 0 ? "R" : "B"); // Red / Blue
					System.out.print("_");
                                        if (nibble3 == 8)
                                            System.out.print("BRAKE");  // Brake then float
                                        else if ((nibble3 & 8) != 0) {
                                            System.out.print("M");      // Minus
                                            System.out.print(8 - (nibble3 & 7));
                                        } else
                                            System.out.print(nibble3 & 7);

                                        // Print hex formatted code:
                                        System.out.print("\t\t0x");
                                        System.out.print(nibble1);
                                        System.out.print(nibble2);
                                        System.out.print(Integer.toHexString(nibble3).toUpperCase());
                                        // LRC = 0xF xor Nibble 1 xor Nibble 2 xor Nibble 3
                                        System.out.println(Integer.toHexString(
                                                        0xF ^ nibble1 ^ nibble2 ^ nibble3).toUpperCase());
				}
			}
		}
	}

	/**
	 * Generates codes for Combo PWM mode.
	 */
	static void comboPWM() {
		// Nibble 1 -- Address = 0, Escape = 1, Channel = #, Channel = #.
		for (int nibble1 = 4; nibble1 < 8; nibble1++) { // 4 to 7 is ch1 to ch4
			// Nibble 2 -- Output B: 0b0000 through 0b1111.
			for (int nibble2 = 0; nibble2 < 16; nibble2++) {
				// Nibble 3 -- Output A: 0b0000 through 0b1111.
				for (int nibble3 = 0; nibble3 < 16; nibble3++) {
					// Print name of code (raw hex string).
					System.out.print("\t");
					System.out
							.print(Integer.toHexString(nibble1).toUpperCase());
					System.out
							.print(Integer.toHexString(nibble2).toUpperCase());
					System.out
							.print(Integer.toHexString(nibble3).toUpperCase());
					System.out.print(Integer.toHexString(
							0xF ^ nibble1 ^ nibble2 ^ nibble3).toUpperCase());
					// Print hex formatted code.
					System.out.print("\t\t0x");
					System.out
							.print(Integer.toHexString(nibble1).toUpperCase());
					System.out
							.print(Integer.toHexString(nibble2).toUpperCase());
					System.out
							.print(Integer.toHexString(nibble3).toUpperCase());
					System.out.print(Integer.toHexString(
							(0xF ^ nibble1 ^ nibble2 ^ nibble3)).toUpperCase());
					System.out.println("");
				}
			}
		}
	}
}
