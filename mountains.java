import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.StringTokenizer;

public class mountains {
    /*
    Can find out if one mountain is another, if the absolute value of the slope between the two peaks is >= 1
        If it is inside what you can do, is find the greater Y - value to find which mountain is the peak
    Idea 1
    create a set containing all the visible peaks
    for each new mountain iterate through the set, and compare both of them. Put the bigger on in the set and
        remove the other one from the set if possible
    Print out the size of set at the end to find the total amount of peaks.
    */
    public static void main(String[] args) throws IOException {
        Kattio reader = new Kattio("mountains");
        int N = reader.nextInt();
        Set<Mountain> viewMountains = new HashSet<Mountain>();
        Iterator<Mountain> viewIterator;
        Mountain[] mountains = new Mountain[N];
        for (int i = 0; i < N; i++) {
            mountains[i] = new Mountain(reader.nextInt(), reader.nextInt());
        }


        for (int i = 0; i < N; i++) {
            //System.out.println();
            Mountain currentMountain = mountains[i];
            boolean isVisible = true;
            viewMountains.add(currentMountain);
            Set<Mountain> copySet = Set.copyOf(viewMountains);
            //viewMountains.remove(currentMountain);
            viewIterator = copySet.iterator();
            while (viewIterator.hasNext()) {
                Mountain otherMountain = viewIterator.next();
                if (otherMountain != currentMountain) {
                    //System.out.println("Did not skip mountain: " + otherMountain);
                    //System.out.println("ERROR");
                    if (currentMountain.visibility(otherMountain) != null) {
                        if (currentMountain.visibility(otherMountain) == otherMountain){
                            viewMountains.remove(otherMountain);
                            //System.out.println("Other Mountain was overshadowed");
                        }
                        else {
                            viewMountains.remove(currentMountain);
                            break;
                        }
                    }
                }
                else{
                    //System.out.println("Found the same mountain!");
                }
                
            }
        }


        reader.println(viewMountains.size());
        reader.close();
    }

    static class Mountain {
        double x;
        double y;
        public Mountain(double _x, double _y) {
            x = _x;
            y = _y;
        }

        public Mountain visibility(Mountain other) {
            if (x == other.x ||
                 (Math.abs((y - other.y)/(x - other.x)) >= 1)) {
                if (other.y > y) {
                    return this;
                }
                else {
                    return other;
                }
            }
            else {

            }
            return null;
        }

        @Override
        public String toString(){
            return "Mountain at: [" + x + ", " + y +"]";
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
