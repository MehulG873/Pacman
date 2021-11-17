import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.concurrent.CountDownLatch;


//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=643 

//TIMED OUT:
/*
Possible Fix: store an int array with each index correpsonding to possible case
the value should be an int array of 2, helping you figure out max case possible with a left
*/
public class diamond {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("diamond");
        int n = reader.nextInt();
        int k = reader.nextInt();
        int[] diamonds = new int[n];
        int count = 0;
        int[][] possibleCounts = new int[n][2];
        for (int i = 0; i < n; i++) {
            diamonds[i] = reader.nextInt();
        }
        Arrays.sort(diamonds);
        for (int left = 0; left < n; left++) {
            int right = left + 1;
            int guess = 1;
            while (right < n && diamonds[right] - diamonds[left] <= k) {
                guess++;
                right++;
            }
            possibleCounts[left][0] = guess;
            possibleCounts[left][1] = right;
        }
        count = possibleCounts[0][0];

        for (int case1 = 0; case1 < possibleCounts.length - 1; case1++) {
            int guess = possibleCounts[case1][0]; 
            int cases = guess;
            for (int i = possibleCounts[case1][1]; i < n; i++) {
                guess = Math.max(guess, cases + possibleCounts[i][0]);
            }
            count = Math.max(count, guess);
        }

        reader.println(count);
        reader.close();

    }
    static class Kattio extends PrintWriter {
        private BufferedReader r;
        private StringTokenizer st;
    
        // standard input
        public Kattio() { this(System.in, System.out); }
        public Kattio(InputStream i, OutputStream o) {
            super(o);
            r = new BufferedReader(new InputStreamReader(i));
        }
        // USACO-style file input
        public Kattio(String problemName) throws IOException {
            super(new FileWriter(problemName + ".out"));
            r = new BufferedReader(new FileReader(problemName + ".in"));
        }
    
        // returns null if no more input
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens())
                    st = new StringTokenizer(r.readLine());
                return st.nextToken();
            } catch (Exception e) { }
            return null;
        }
    
        public int nextInt() { return Integer.parseInt(next()); }
        public double nextDouble() { return Double.parseDouble(next()); }
        public long nextLong() { return Long.parseLong(next()); }
    }
}
