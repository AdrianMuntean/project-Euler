import java.math.BigInteger;

public class LatticePaths {
    static final int LEFT = 0;
    static final int DOWN = 1;

    long noPaths = 0;

    /*
    Simple solution with backtracking, but it's taking way too much time
    */
    void latticePathsWithDir(int gridSize, int dir, int indexI, int indexJ) {
        if (indexI > gridSize || indexJ > gridSize) {
            return;
        }

        if (indexI == gridSize && indexJ == gridSize) {
            noPaths++;
            return;
        }

        latticePathsWithDir(gridSize, LEFT, indexI + 1, indexJ);
        latticePathsWithDir(gridSize, DOWN, indexI, indexJ + 1);

    }

    void latticePaths(int gridSize) {
        latticePathsWithDir(gridSize, LEFT, 0, 0);
        return;
    }


    /*
    Use Pascal's triangle and the formula of binomial coefficient: (2 * gridSize)! / gridSize!^2
     */
    private long latticePathsWithMath(int gridSize) {
        BigInteger factOfDouble = BigInteger.ONE;
        BigInteger nFact = BigInteger.ONE;
        for (int i = 2; i <= gridSize * 2; i++) {
            factOfDouble = factOfDouble.multiply(BigInteger.valueOf(i));
            if (i <= gridSize) {
                nFact = nFact.multiply(BigInteger.valueOf(i));
            }
        }

        return factOfDouble.divide(nFact.multiply(nFact)).longValue();
    }

    public static void main(String[] args) {
        LatticePaths latticePaths = new LatticePaths();
        System.out.println(latticePaths.latticePathsWithMath(20));
//         latticePaths.latticePaths(20);
//        System.out.println(latticePaths.noPaths);

    }


}
