import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
//Problem: Alphastar Diagnostic Silver

public class Clairvoyance {
    public static void main(String[] args) {        
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int N = reader.nextInt();
        boolean[] cards = new boolean[2 * N];
        int[] oppositeCards = new int[N];
        int wins = 0;
        for (int i = 1; i <= 2 * N; i++){
            cards[i - 1] = true;
        }
        for (int i = 0; i < N; i++){
            int oppositeCard = reader.nextInt();
            cards[oppositeCard - 1] = false;
            oppositeCards[i] = oppositeCard;
        }

        //Checking Points
        for (int oCard: oppositeCards){
            int playedCard = oCard + 1;
            while (playedCard <= 2 * N && !cards[playedCard - 1]){
                playedCard += 1;
            }
            if (playedCard <= 2 * N && cards[playedCard - 1]){
                cards[playedCard - 1] = false;
                wins++;
            }
        }

        System.out.println(wins);
    }
}
