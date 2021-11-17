import java.io.*;
import java.util.*;

public class roomAllocation{
    public static void main(String[] args) {
        Kattio reader= new Kattio();
        int n = reader.nextInt();
        TreeSet<Bookings> change= new TreeSet<Bookings>();
        TreeSet<Integer> rooms = new TreeSet<Integer>();
        int[] roomAssignments = new int[n + 1];
        int numberOfRooms = 0;
        for (int i = 0; i < n; i++) {
            change.add(new Bookings(reader.nextInt(), true, i + 1));
            change.add(new Bookings(reader.nextInt(), false, i + 1));
        }

        for (Bookings booking : change) {
            if (booking.isArrival) {
                if (rooms.isEmpty()) {
                    numberOfRooms++;
                    rooms.add(numberOfRooms);
                }
                roomAssignments[booking.customer] = rooms.first();
                rooms.remove(roomAssignments[booking.customer]);
            }
            else {
                rooms.add(roomAssignments[booking.customer]);
            }
        }

        System.out.println(numberOfRooms);
        for (int i = 1; i <= n; i++) {
            System.out.print(roomAssignments[i] + " ");
        }

        reader.close();
    }

    static class Bookings implements Comparable<Bookings> {
        int day;
        boolean isArrival;
        int customer;
        public Bookings(int _d, boolean _isArrival, int _c) {
            day = _d;
            isArrival = _isArrival;
            customer = _c;
        }

        @Override
        public int compareTo(Bookings o) {
            if (day == o.day) {
                if (customer == o.customer) {
                    if (isArrival) {
                        return -1;
                    }
                    else {
                        return +1;
                    }
                }
                return Integer.compare(customer, o.customer);
            }
            // if ( o.day == day && o.isArrival && !isArrival) {
            //     return 1;
            // }
            // else if ( o.day == day && !o.isArrival && isArrival) {
            //     return -1;
            // }
            return Integer.compare(day, o.day);
        }

        @Override
        public String toString() {
            return "Change on day: " + day + "; It is an arrival: " + isArrival; 
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
