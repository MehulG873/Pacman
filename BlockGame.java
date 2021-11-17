import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class BlockGame {
    public static void main(String[] args) throws IOException {
        Scanner sc1 = new Scanner(new File("./blocks.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("./blocks.out")));

        int numWords = sc1.nextInt() * 2;
        System.out.println(numWords);
        String[] words = new String[numWords];
        int[] letterCount = new int[26];
        for (int i = 0; i < numWords; i++){
            words[i] = sc1.next();
        }

        for (int i = 0; i < (numWords/2); i++) {
            System.out.println(i);
            int[] wordLetters1 = charCounts(words[i*2]);
            int[] wordLetters2 = charCounts(words[i*2 + 1]);
            //System.out.println(Arrays.toString(wordLetters1));
            //System.out.println(Arrays.toString(wordLetters2));
            for (int index = 0; index < 26; index++) {
                wordLetters1[index] = Math.max(wordLetters1[index], wordLetters2[index]);            
                //System.out.println(Arrays.toString(wordLetters1));
                letterCount[index] += wordLetters1[index];
                //System.out.println(Arrays.toString(letterCount));
            }
        }

        for (int c : letterCount) {
            pw.println(c);
        }
        pw.close();


    }

    public static int[] charCounts(String word) {
        int[] charCounts = new int[26];
        for (char c : word.toCharArray()) {
            charCounts[c - 'a'] += 1;
        }
        return charCounts;
    }
}
