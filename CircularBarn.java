import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class CircularBarn {
    public static void main(String[] args) throws IOException {
        Scanner sc1 = new Scanner(new File("./cbarn.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("./cbarn.out")));

        int min = Integer.MAX_VALUE;
        int rooms = sc1.nextInt();
        ArrayList<Integer> cows = new ArrayList<Integer>(rooms);
        for (int i = 0; i < rooms; i++ ){
            cows.add(sc1.nextInt());
        }
        int guess = 0;
        int currentR = 0;
        for (int i = 0; i < rooms; i++) {
            guess = 0;
            for (int r = i; r < rooms + i; r++) {
                currentR = r;
                if (r >= rooms){
                    currentR -= rooms;
                }
                guess += cows.get(currentR) * (r-i);
            }
            if (guess < min) {
                min = guess;
            }
        }
        pw.println(min);
        pw.close();
    }
}
