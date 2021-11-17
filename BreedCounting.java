import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
public class BreedCounting {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int N = reader.nextInt();
        int Q = reader.nextInt();
        ArrayList<int[]>[] counts = new ArrayList[log2(N)];
        counts[0] = new ArrayList<int[]>();
        for (int i = 0; i < N; i++){
            int[] count = new int[3];
            for (int j = 0; j < 3; j++){
                count[j] = 0;
            }
            count[reader.nextInt() - 1] = 1;

            counts[0].add(count);
        }

        for (int i = 1; i < counts.length; i++){
            counts[i] = buildCounts(counts[i-1]);
        }
        for (int j = 0; j < Q; j++){
            ArrayList<int[]> queryDeconstruct;
            int[] sum = new int[3];
            int a = reader.nextInt();
            int b = reader.nextInt();
            queryDeconstruct = deconstructQuery(a, b);
            for (int[] section:queryDeconstruct){
                //System.out.println(Arrays.toString(section));
                sum = countSum(sum, counts[section[0]].get(section[1]));
            }
            if (a==2){
            }
            printCount(sum);

        }
        System.out.println();
    }

    public static ArrayList<int[]> buildCounts(ArrayList<int[]> counts){
        ArrayList<int[]> level = new ArrayList<int[]>(counts.size()/2);
        for (int i = 0; i < counts.size()/2; i++){
            level.add(countSum(counts.get(2 * i), counts.get(2 * i + 1)));
        }
        return level;
    }

    public static ArrayList<int[]> deconstructQuery(int a, int b){
        ArrayList<int[]> queryDeconstruct = new ArrayList<int[]>();

        while (a < b){
            int twoFactor = 0;
            int aCopy = a - 1;
            while (aCopy % 2 == 0 ){
                if (a + Math.pow(2, twoFactor) - 1 > b){
                    break;
                }
                twoFactor++;
                aCopy = aCopy/2;
            }
            while (a + Math.pow(2, twoFactor) - 1 > b){
                twoFactor--;
            }
            if (twoFactor == 0){
                queryDeconstruct.add(new int[] {twoFactor, (int) (a/Math.pow(2, twoFactor)) - 1});
            }
            else{
                queryDeconstruct.add(new int[] {twoFactor, (int) (a/Math.pow(2, twoFactor))});
            }
            a += Math.pow(2, twoFactor);
        }


        return queryDeconstruct;
    }

    public static int[] countSum(int[] count1, int[] count2){
        int[] newCount = new int[3];
        for (int i =0; i < 3; i++){
            newCount[i] = count1[i] + count2[i];
        }
        return newCount;
    }

    public static void printCount(int[] count){
        System.out.print(count[0]);
        System.out.print(' ');
        System.out.print(count[1]);
        System.out.print(' ');
        System.out.println(count[2]);
    }
    
    public static int log2(int N)
    {
        int result = (int)(Math.log(N) / Math.log(2)) + 1;
  
        return result;
    }
}
