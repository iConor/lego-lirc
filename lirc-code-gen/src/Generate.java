public class Generate {

	public static void main(String[] args) {
//		comboDirect();
		 comboPWM();
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
