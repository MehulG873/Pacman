import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

class Censoring {
    public static void main(String[] args) throws IOException {
        Scanner sc1 = new Scanner(new File("./censor.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("./censor.out")));

        String S = sc1.nextLine();
        String T = sc1.nextLine();
        ArrayList<Integer> indexes = new ArrayList<Integer>();
        int index = S.indexOf(T);
        while (index != -1) {
            indexes.add(index);
            index = S.indexOf(T, indexes.get(indexes.size() - 1) + T.length() );
            while (index  != - 1) {
                indexes.add(index);
                index = S.indexOf(T, indexes.get(indexes.size() - 1) + T.length());
            }
            String sub = S.substring(0, indexes.get(0));
            for (int i = 1; i < indexes.size(); i++) {
                sub += S.substring(indexes.get(i - 1) + T.length(), indexes.get(i));
            }
            sub += S.substring(indexes.get(indexes.size() - 1));
            S = sub;
            System.out.println(S);
            index = S.indexOf(T);
            indexes = new ArrayList<Integer>();

        }
        pw.println(S);
        pw.close();
    }
}