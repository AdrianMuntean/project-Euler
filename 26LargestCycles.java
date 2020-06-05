public class Cycles {

    private StringBuilder result = new StringBuilder();

    int recurringCycleLength(int n) {
        result.setLength(0);
        int toDivide = 10;
        int remainder = 1;
        while (remainder != 0) {
            int fractionUnit = toDivide / n;
            remainder = toDivide % n;
            if (result.length() > 3) {
                int index = result.indexOf("" + result.charAt(result.length() - 2) +
                        result.charAt(result.length() - 1) + fractionUnit);
                if (index >= 0) {
                    result.append(fractionUnit);
                    break;
                }
            }
            result.append(fractionUnit);
            toDivide = remainder * 10;
        }

        return remainder == 0 ? 0 : result.indexOf("" + result.charAt(result.length() - 3) +
                result.charAt(result.length() - 2) + result.charAt(result.length() - 1)) + result.length() - 3;
    }


    int reciprocalCycles(int n) {
        int largestIndex = 0;
        int largestCycle = 0;
        for (int i = 3; i < n; i++) {

            int cycleLen = recurringCycleLength(i);
            if (cycleLen > largestCycle) {
                largestIndex = i;
                largestCycle = cycleLen;
            }
        }
        return largestIndex;
    }

    public static void main(String[] args) {
        System.out.println(new Cycles().reciprocalCycles(1000)); // 983
    }
}
