import java.util.*;
import java.io.*;

public class convention2 {
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("convention2");
        int N = reader.nextInt();
        int maxWaitingTime = 0;
        TreeSet<Cow> arrivals = new TreeSet<Cow>(new ArrivalComparator());
        TreeSet<Cow> waiting = new TreeSet<Cow>(new SeniorComparator());
        int time = 0;
        for (int i = 0; i < N; i++) {
            arrivals.add(new Cow(reader.nextInt(), reader.nextInt(), i));
        }
        for (int i = 0; i < N; i++) {
            if (!arrivals.isEmpty() && waiting.isEmpty()) {
                time = Math.max(time, arrivals.first().arrival);
            }
            while (!arrivals.isEmpty() && arrivals.first().arrival <= time) {
                waiting.add(arrivals.pollFirst());
            }
            if (!waiting.isEmpty()) {
                Cow nextCow = waiting.pollFirst();
                maxWaitingTime = Math.max(maxWaitingTime, time - nextCow.arrival);
                time += nextCow.time;
            }

            // System.out.println("Next Cow");
        }

        
        reader.println(maxWaitingTime);
        reader.close();
    }

    static class ArrivalComparator implements Comparator<Cow> {

        @Override
        public int compare(convention2.Cow o1, convention2.Cow o2) {
            if (o1.arrival == o2.arrival) {
                return o1.seniority - o2.seniority;
            }
            return o1.arrival - o2.arrival;
        }

    }

    static class SeniorComparator implements Comparator<Cow> {

        @Override
        public int compare(convention2.Cow o1, convention2.Cow o2) {
            return o1.seniority - o2.seniority;
        }

    }
    
    static class Cow {
        int arrival;
        int time;
        int seniority;
        public Cow(int _a, int _t, int _s) {
            arrival = _a;
            time = _t;
            seniority = _s;
        }

        @Override
        public String toString() {
            return ("Cow: " + arrival + 
                    "; " + time +
                    "; " + seniority);
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
