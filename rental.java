import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.stream.Stream;
import java.lang.Comparable;

//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=787 

public class rental {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("rental");
        int N = reader.nextInt();
        int M = reader.nextInt();
        int R = reader.nextInt();
        Integer[] cows = new Integer[N];
        Stores[] stores = new Stores[M];
        Integer[] rentals = new Integer[R];
        long profit = 0;

        for (int i = 0; i < N; i++) {
            cows[i] = reader.nextInt();
        }
        for (int i = 0; i < M; i++) {
            stores[i] = new Stores(reader.nextInt(), reader.nextInt()); 
        }
        for (int i = 0; i < R; i++) {
            rentals[i] = reader.nextInt();
        }
        
        Arrays.sort(cows);
        Arrays.sort(stores);
        Arrays.sort(rentals);
        int cowIndex = 0;
        int storeIndex = M - 1;
        int rentIndex = R - 1;

        for (int i = N - 1; i >= 0; i--) {
            if (cows[i] != 0) {
                int milk = cows[i];
                int p = 0;
                int storeIndexCopy = storeIndex;
                while (milk > 0 && storeIndexCopy >= 0) {
                    int milkSold = Math.min(stores[storeIndexCopy].g, milk);
                    milk -= milkSold;
                    p += stores[storeIndexCopy].p * milkSold;
                    // stores[storeIndexCopy].g -= milkSold;
                    // System.out.println(milkSold);
                    storeIndexCopy -= 1;
                }
                if (rentIndex < 0 || p > rentals[rentIndex]) {
                    while (cows[i] > 0 && storeIndex >= 0) {
                        int milkSold = Math.min(stores[storeIndex].g, cows[i]);
                        cows[i] -= milkSold;
                        profit += stores[storeIndex].p * milkSold;
                        stores[storeIndex].g -= milkSold;
                        // System.out.println(milkSold);
                        if (stores[storeIndex].g <= 0) {
                            storeIndex -= 1;
                        }
                        // System.out.println();
                    }
                }
                else if (rentIndex >= 0 && cowIndex < N) {
                    cows[cowIndex] = 0;
                    cowIndex++;
                    profit += rentals[rentIndex];
                    rentIndex--;
                    i++;
                }
            }
        }

        reader.println(profit);
        reader.close();
    }

    static class Stores implements Comparable<Stores> {
        int g, p;
        public Stores(int _g, int _p) {
            g = _g;
            p = _p;
        }

        public int compareTo(Stores o) {
            return Integer.compare(p, o.p);
        }
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



