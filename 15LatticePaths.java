import java.math.BigInteger;


/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
*/

public class LatticePaths {
    long noPaths = 0;

    /*
    Simple solution with backtracking, but it's taking way too much time
    */
    void latticePathsWithDir(int gridSize, int indexI, int indexJ) {
        if (indexI > gridSize || indexJ > gridSize) {
            return;
        }

        if (indexI == gridSize && indexJ == gridSize) {
            noPaths++;
            return;
        }

        latticePathsWithDir(gridSize, indexI + 1, indexJ); // LEFT
        latticePathsWithDir(gridSize, indexI, indexJ + 1); // DOWN

    }

    void latticePaths(int gridSize) {
        latticePathsWithDir(gridSize, 0, 0);
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
