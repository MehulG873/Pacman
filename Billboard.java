import java.io.*;
import java.util.*;

public class Billboard {
    public static void main(String[] args) throws IOException {
        Kattio io = new Kattio("billboard");
        int[] b1 = new int[] {io.nextInt(), io.nextInt(), io.nextInt(), io.nextInt()};
        int[] b2 = new int[] {io.nextInt(), io.nextInt(), io.nextInt(), io.nextInt()};
        int[] t = new int[] {io.nextInt(), io.nextInt(), io.nextInt(), io.nextInt()};
        int b1Area = (b1[2] - b1[0]) * (b1[3] - b1[1]);
        int b2area = (b2[2] - b2[0]) * (b2[3] - b2[1]);
        int intersection = intersection(b1, t) + intersection(b2, t);
        io.println(b1Area + b2area - intersection);
        io.close();

    }

    public static int intersection(int[] r1, int[] r2) {
        int width = Math.max(Math.min(r1[2], r2[2]) - Math.max(r1[0], r2[0]),0);
        int height = Math.max(Math.min(r1[3], r2[3]) - Math.max(r1[1], r2[1]),0);
        return width * height;
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
