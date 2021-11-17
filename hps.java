//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=691 
import java.io.*;
import java.util.*;

public class hps {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("hps");
        int N = reader.nextInt();
        int wins = 0;
        //H - 0, S - 1, P - 2
        int[][] counts = new int[N + 1][3];
        for (int i = 1; i <= N; i++) {
            char action = reader.next().toCharArray()[0];
            if (action == 'H') {
                counts[i][0] = counts[i-1][0];
                counts[i][1] = counts[i-1][1];
                counts[i][2] = counts[i-1][2];
                counts[i][0] ++;
            }
            else if (action == 'S') {
                counts[i][0] = counts[i-1][0];
                counts[i][1] = counts[i-1][1];
                counts[i][2] = counts[i-1][2];
                counts[i][1] ++;
            }
            else if (action == 'P') {
                counts[i][0] = counts[i-1][0];
                counts[i][1] = counts[i-1][1];
                counts[i][2] = counts[i-1][2];
                counts[i][2] ++;
            }
        }
        for (int i = 1; i <= N; i++) {
            int wins1 = Math.max(counts[i][0], Math.max(counts[i][1], counts[i][2]));
            int wins2 = Math.max(counts[N][0] - counts[i][0], Math.max(counts[N][1] - counts[i][1], counts[N][2] - counts[i][2]));
            wins = Math.max(wins, wins1 + wins2);

        }
        
        reader.println(wins);
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