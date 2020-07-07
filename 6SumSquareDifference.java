import java.util.stream.IntStream;

public class SumSquareDifference {
    long compute(int number) {
        long sumOfSquares = IntStream.rangeClosed(1, number).map(n -> n * n).sum();
        long squareOfSum = (long) Math.pow(IntStream.rangeClosed(1, number).sum(), 2);

        return Math.abs(sumOfSquares - squareOfSum);
    }

    public static void main(String[] args) {
        System.out.println(new SumSquareDifference().compute(100));
    }
}
