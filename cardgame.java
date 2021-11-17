import java.util.*;
import java.io.*;

public class cardgame {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("cardgame");
        int N = reader.nextInt();
        TreeSet<Integer> ECardsFirstHalf = new TreeSet<Integer>();
        TreeSet<Integer> ECardsSecondHalf = new TreeSet<Integer>();
        TreeSet<Integer> BCardsFirstHalf = new TreeSet<Integer>();
        TreeSet<Integer> BCardsSecondHalf = new TreeSet<Integer>();
        ArrayList<Integer> BCards = new ArrayList<Integer>();
        int maxWins = 0;
        for (int i = 0; i < N; i++) {
            if (i < N/2) ECardsFirstHalf.add(reader.nextInt());
            else ECardsSecondHalf.add(reader.nextInt());
        }
        for (int i = 1; i <= 2 * N; i++) {
            if (!ECardsFirstHalf.contains(i) && !ECardsSecondHalf.contains(i)) BCards.add(i);
        }
        for (int i = 0; i < N; i++) {
            if (i < N/2) BCardsSecondHalf.add(BCards.get(i));
            else BCardsFirstHalf.add(BCards.get(i));
        }

        for (int i = 0; i< N/2; i++) {
            if (BCardsFirstHalf.first() > ECardsFirstHalf.first()) {
                maxWins++;
                BCardsFirstHalf.pollFirst();
                ECardsFirstHalf.pollFirst();
            }
            else {
                BCardsFirstHalf.pollFirst();
                ECardsFirstHalf.pollLast();
            }
        }
        for (int i = 0; i< N/2; i++) {
            if (BCardsSecondHalf.last() < ECardsSecondHalf.last()) {
                maxWins++;
                BCardsSecondHalf.pollLast();
                ECardsSecondHalf.pollLast();
            }
            else {
                BCardsSecondHalf.pollLast();
                ECardsSecondHalf.pollFirst();
            }
        }

        reader.print(maxWins);
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
