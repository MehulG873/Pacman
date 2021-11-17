import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.Scanner;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
//Problem: Alphastar Diagnostic

public class MilkSchedule {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int N = reader.nextInt();
        int Q = reader.nextInt();
        int[] cowTimes = new int[N];
        int currentTime = -1;
        for (int i = 0; i < N; i++){
            currentTime += reader.nextInt();
            cowTimes[i] = currentTime;
        }
        for (int j = 0; j < Q; j++){
            int q = reader.nextInt();
            currentTime = -1;
            int cowNum = -1;
            while (q > currentTime){
                cowNum++;
                currentTime = cowTimes[cowNum];
            }
            System.out.println(cowNum + 1); 
        }
        
    }   
}
