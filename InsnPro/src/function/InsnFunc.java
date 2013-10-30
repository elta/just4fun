package function;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class InsnFunc {
	public static void StringToInsn(String str) {
		int bits = 32;
		String finalInsn[] = { "", "", "", "", "" }; // d, s, t, r, imm
		String finalInsn2[] = { "", "" }; // offset/index, base
		int code[] = { 0, 0xFFFFFFFF };

		int tmpCode = 0;

		tmpInsn = str.split(" ");

		if (tmpInsn.length == 0 || !tmpInsn[0].equals("/*")) {
			return;
		}

		if (tmpInsn[1].toCharArray()[0] >= 'A'
				&& tmpInsn[1].toCharArray()[0] <= 'Z') {
			System.out.println("");
			System.out.println(str);

			return;
		} else {
			System.out.println(str);
		}

		for (int i = 2; i < tmpInsn.length - 1; i++) {
			if (isReg(tmpInsn[i]) != -1) {
				int regL = regLength(tmpInsn[i]);
				bits -= regL;

				tmpInsn[i] = regReName(tmpInsn[i], bits);

				if (tmpInsn[i].contains("D")) {
					finalInsn[0] = tmpInsn[i];
				} else if (tmpInsn[i].contains("S")) { // *s
					finalInsn[1] = tmpInsn[i];
				} else if (tmpInsn[i].contains("T")) { // *t
					finalInsn[2] = tmpInsn[i];
				} else if (tmpInsn[i].contains("R")) { // *r
					finalInsn[3] = tmpInsn[i];
				} else if (tmpInsn[i].contains("I")) { // imm*
					finalInsn[4] = tmpInsn[i];
				} else if (tmpInsn[i].contains("O")) { // offset*
					finalInsn2[0] = tmpInsn[i];
				} else if (tmpInsn[i].contains("B")) { // base
					finalInsn2[1] = tmpInsn[i];
				} else if (tmpInsn[i].contains("X")) { // index
					finalInsn2[0] = tmpInsn[i];
				}

				code[1] = code[1] & ~(((1 << regL) - 1) << bits);
			} else {
				bits -= tmpInsn[i].length();
				tmpCode = 0;
				for (int j = 0; j < tmpInsn[i].length(); j++) {
					tmpCode = tmpCode << 1;
					tmpCode |= (tmpInsn[i].toCharArray()[j] - '0');
				}
				code[0] = code[0] | (tmpCode << bits);
			}
			if (bits <= 0) {
				if (i != (tmpInsn.length - 2)) {
					// System.out.println("error bits num....");
				}
				break;
			}
		}

		// System.out.println("Bits is " + bits);

		System.out.print("{");
		System.out.print("\"" + tmpInsn[1] + "\", \"");
		int k;
		boolean hasCommonReg = false;

		for (k = 0; k < finalInsn.length; k++) {
			if (!finalInsn[k].equals("")) {
				System.out.print(finalInsn[k]);
				k++;
				hasCommonReg = true;
				break;
			}
		}
		for (; k < finalInsn.length; k++) {
			if (!finalInsn[k].equals("")) {
				System.out.print("," + finalInsn[k]);
				hasCommonReg = true;
			}
		}

		if (hasCommonReg) {
			System.out.print(",");
		}

		if (!finalInsn2[0].equals("")) {
			System.out.print(finalInsn2[0]);
		}

		if (!finalInsn2[1].equals("")) {
			System.out.print("(" + finalInsn2[1] + ")");
		}

		System.out.print("\", ");
		System.out.print("0x" + Integer.toHexString(code[0]) + ", ");
		System.out.print("0x" + Integer.toHexString(code[1]) + ", ");
		System.out.println("0, 0, I1 },");
	}

	private static int regLength(String str) {
		if (str.contains("mm")) {
			return str.toCharArray()[3] - '0';
		} else if (str.contains("offset13")) {
			return 13;
		} else if (str.contains("offset16")) {
			return 16;
		} else {
			return 5;
		}
	}

	private static int isReg(String str) {
		for (int i = 0; i < regName.length; i++) {
			if (str.startsWith(regName[i])) {
				return i;
			}
		}

		return -1;
	}

	private static String regReName(String regName, int index) {
		String newName = new String();
		HashMap<Integer, String> map = new HashMap<Integer, String>();

		map.put(index, regName);

		if (regNamePosMap.containsKey(map)) {
			newName = regNamePosMap.get(map);
		} else {
			if (regName.contains("offset")) {
				newName = "@O" + regPos[0]++;
			} else if (regName.contains("base")) {
				newName = "@B" + regPos[1]++;
			} else if (regName.contains("index")) {
				newName = "@X" + regPos[2]++;
			} else if (regName.contains("d")) {
				newName = "@D" + regPos[3]++;
			} else if (regName.contains("s")) {
				newName = "@S" + regPos[4]++;
			} else if (regName.contains("t")) {
				newName = "@T" + regPos[5]++;
			} else if (regName.contains("r")) {
				newName = "@R" + regPos[6]++;
			} else if (regName.contains("mm")) {
				newName = "@I" + regPos[7]++;
			}

			regNamePosMap.put(map, newName);
		}

		return newName;
	}

	public static void showAllRegPosition() {

		HashMap<Integer, String> key = null;
		Set keys = regNamePosMap.keySet();
		Iterator it = keys.iterator();

		System.out.println("\n\nNow show all reg:");
		while (it.hasNext()) {
			key = (HashMap<Integer, String>) it.next();
			System.out.print(regNamePosMap.get(key) + " ");

			Integer key2;
			Set keys2 = key.keySet();
			Iterator it2 = keys2.iterator();
			while (it2.hasNext()) {
				key2 = (Integer) it2.next();
				System.out.print(key2 + " ");
				System.out.println(key.get(key2));
			}
		}
	}

	// d, s, t, r, mm, o
	private static int[] regPos = { 1, 1, 1, 1, 1, 1, 1, 1 };

	private static String[] tmpInsn = new String[20];
	private static String regName[] = { "vr", "vd", "vs", "vt", "fd", "fs",
			"ft", "rd", "rs", "rt", "imm", "fmt", "base", "offset", "index" };
	private static HashMap<HashMap<Integer, String>, String> regNamePosMap = new HashMap<HashMap<Integer, String>, String>();
}
