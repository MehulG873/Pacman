import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LoadBalancing {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new File("./balancing.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("./balancing.out")));
        int N = sc.nextInt();
        int B = sc.nextInt();
        sc.nextLine();
        List<int[]> cords = new ArrayList<int[]>();
        for (int i = 0; i < N; i++) {
            cords.add(new int[] {sc.nextInt(), sc.nextInt()});
        }
        double xAverage = 0;
        double yAverage = 0;
        for (int i = 0; i < N; i++) {
            xAverage += cords.get(i)[0];
            yAverage += cords.get(i)[1];
        }
        xAverage /= N;
        yAverage /= N;
        System.out.println(xAverage + ", " + yAverage);
        long a = roundEven(xAverage);
        long b = roundEven(yAverage);
        List<int[]> tL = new ArrayList<int[]>();
        List<int[]> tR = new ArrayList<int[]>();
        List<int[]> bL = new ArrayList<int[]>();
        List<int[]> bR = new ArrayList<int[]>();
        for (int[] p : cords) {
            if (p[0] <= a) {
                if (p[1] <= b) {
                    tL.add(p);
                }
                else {
                    tR.add(p);
                }
            }
            else {
                if (p[1] <= b) {
                    bL.add(p);
                }
                else {
                    bR.add(p);
                }
            }
        }
        int M = Math.max(Math.max(tL.size(), tR.size()), Math.max(bL.size(), bR.size()));
        pw.println(M);
        pw.close();


    }
    public static long roundEven(double d) {
        return Math.round(d / 2) * 2;
    }   
}
