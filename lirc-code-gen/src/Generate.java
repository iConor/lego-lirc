public class Generate {

	public static void main(String[] args) {
		comboDirect();
		// comboPWM();
	}

	/**
	 * Generates LEGO LIRC codes for Combo Direct Mode.
	 */
	static void comboDirect() {
		int nibble1 = 0; // Toggle, escape, channel, channel.
		int nibble2 = 1; // Address, mode, mode, mode.
		for (int nibble3 = 0; nibble3 < 16; nibble3++) {
			// Nibble 3 - ##xx - output B.
			int b = nibble3 >> 2;
			// Nibble 3 - xx## - output A.
			int a = nibble3 % 4;
			// Print name of code and spacing.
			System.out.print("\t" + codeName(b) + "_" + codeName(a) + "\t\t0x");
			// Print code:
			System.out.print(nibble1);
			System.out.print(nibble2);
			System.out.print(Integer.toHexString(nibble3).toUpperCase());
			// LRC = 0xF xor Nibble 1 xor Nibble 2 xor Nibble 3
			System.out.println(Integer.toHexString(
					0xF ^ nibble1 ^ nibble2 ^ nibble3).toUpperCase());
		}
	}

	/**
	 * Generates name of code half a nibble represents.
	 * 
	 * @param nib
	 *            Two bits. Half of Nibble 3. Output A or B.
	 * @return cmd String. Name of command nib represents.
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
		for (int i = 4; i < 5; i++) { // Nibble 1
			for (int j = 0; j < 16; j++) { // Nibble 2
				for (int k = 0; k < 16; k++) { // Nibble 3
					System.out.print("\t");
					System.out.print(Integer.toHexString(i).toUpperCase());
					System.out.print(Integer.toHexString(j).toUpperCase());
					System.out.print(Integer.toHexString(k).toUpperCase());
					System.out.print(Integer.toHexString(0xF ^ i ^ j ^ k)
							.toUpperCase());
					System.out.print("\t\t0x");
					System.out.print(Integer.toHexString(i).toUpperCase());
					System.out.print(Integer.toHexString(j).toUpperCase());
					System.out.print(Integer.toHexString(k).toUpperCase());
					System.out.print(Integer.toHexString((0xF ^ i ^ j ^ k))
							.toUpperCase());
					System.out.println("");
				}
			}
		}
	}

}
