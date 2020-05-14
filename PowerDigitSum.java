import java.math.BigInteger;

public class PowerDigitSum {

    int powerDigitSum(int n) {
        BigInteger number = BigInteger.TWO.pow(n);
        int sum = 0;
        while (number.compareTo(BigInteger.ZERO) > 0 ) {
            sum += number.mod(BigInteger.TEN).intValue();
            number = number.divide(BigInteger.TEN);
        }

        return sum;
    }

    public static void main(String[] args) {
        PowerDigitSum latticePaths = new PowerDigitSum();
        System.out.println(latticePaths.powerDigitSum(1000));
    }
}
