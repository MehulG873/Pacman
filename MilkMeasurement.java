import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;
public class MilkMeasurement {
    public static void main(String[] args) throws IOException {
        Scanner sc1 = new Scanner(new File("./measurement.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("./measurement.out")));

        int logs = sc1.nextInt();
        String[] logsBook = new String[101];
        int changes = 0;
        Boolean[] leaderboard = new Boolean[] {true, true, true};
        int[] dailyProduction = new int[] {7, 7, 7};
        for (int i = 0; i < logs; i++) {
            logsBook[sc1.nextInt()] = sc1.nextLine();
        }
        System.out.println(Arrays.toString(logsBook));
        int cow = 0;
        for (String log : logsBook) {
            if (log != null) {
                if (log.substring(0, log.length() - 3).equals(" Bessie")) {
                    cow = 0;
                }
                else if (log.substring(0, log.length() - 3).equals(" Elsie")) {
                    cow = 1;      
                }
                else if (log.substring(0, log.length() - 3).equals(" Mildred")) {
                    cow = 2;
                }
                else {
                    System.out.println(log.substring(0, log.length() - 3));
                }
                dailyProduction[cow] += Integer.parseInt(log.substring(log.length() - 2));
                System.out.println(Arrays.toString(dailyProduction));
                Boolean[] newLeaderBoard = leaderboard(dailyProduction);
                if (!Arrays.equals(newLeaderBoard, leaderboard)) {
                    changes += 1;
                    leaderboard = newLeaderBoard;
                }
            }
        }
        pw.println(changes);
        pw.close();

    }
    public static Boolean[] leaderboard(int[] dailyProduction) {
        Boolean[] board = new Boolean[3];
        int max = 0;
        for (int i = 0; i < 3; i++) {
            if (dailyProduction[i] > max) {
                max = dailyProduction[i];
                board = new Boolean[] {false, false, false};
                board[i] = true;
            }
            else if (dailyProduction[i] == max) {
                board[i] = true;
            }
        }

        return board;
    }
}
