import java.io.BufferedReader;
import java.util.Scanner;
import java.io.InputStreamReader;

public class GoodSubarrays {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int testCases = reader.nextInt();
        for ( int k = 0; k < testCases; k++) {
            int goodSubarrays = 0;

            int L = reader.nextInt();
            int[] array = new int[L];
            int[] prefix = new int[L];
            char[] tempArray = reader.next().toCharArray();
            for (int i = 0; i < L; i++) {
                array[i] = Character.getNumericValue(tempArray[i]);
            }
            prefix[0] = array[0];
            for (int i = 1; i < L; i++) {
                prefix[i] = prefix[i-1] + array[i];
            }

            for (int l = 0; l < L; l++) {
                for (int r = l; r < L; r++) {
                    if (l != 0 && prefix[r] - prefix[l - 1] == r-l + 1) {
                        goodSubarrays ++;
                    } 
                    else if (l == 0 && prefix[r] == r-l + 1) {
                        goodSubarrays++;
                    }
                }
            }

            System.out.println(goodSubarrays);
        }
    }
}
