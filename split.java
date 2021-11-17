//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=645
/*
1. Get the number of cows: Set that as N
2. Create a class for the cows, make sure to have consturctor and possibly comparator of coord.
2. Iterate through the coordinates, find the bottom left hand, and top right hand coordinates
    a. Calculate area of one fence
3. Iterate through cows again, but find area from left hand side, and right hand side.
    a. Create two seperate rectangles, with each cows going into pen1 or pen 2
4. Make sure that both pens don't overlap
5. Calculate area of two pens and subtract it from the area of the 1 pen
*/
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

import javax.swing.border.EmptyBorder;


public class split {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("split");
        int N = reader.nextInt();
        Cow[] cows = new Cow[N];
        int[] enclosure = new int[4];
        enclosure[0] = Integer.MAX_VALUE;
        enclosure[1] = Integer.MAX_VALUE;
        for (int i = 0; i < N; i++) {
            int x = reader.nextInt();
            int y = reader.nextInt();
            enclosure[0] = Math.min(enclosure[0], x);
            enclosure[1] = Math.min(enclosure[1], y);
            enclosure[2] = Math.max(enclosure[2], x);
            enclosure[3] = Math.max(enclosure[3], y);
            cows[i] = new Cow(x, y);
        }

        int[] enclosure1 = new int[4];
        enclosure1[0] = Integer.MAX_VALUE;
        enclosure1[1] = Integer.MAX_VALUE;

        int[] enclosure2 = new int[4];
        enclosure2[0] = Integer.MAX_VALUE;
        enclosure2[1] = Integer.MAX_VALUE;

        for (Cow cow: cows) {
            
        }
        //System.out.println(Arrays.toString(cows));
        
        System.out.println(((enclosure[3] - enclosure[1]) *
                            (enclosure[2] - enclosure[0])));

    }

    static class Cow {
        int x;
        int y;
        public Cow(int _x, int _y) {
            x = _x;
            y = _y;
        }

        @Override
        public String toString(){
            return "Cow at: (" + x + ", " + y + ")\n";
        }

        public int area(int[] cord) {
            return Math.abs((cord[0] - x) * (cord[1] - y));
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
