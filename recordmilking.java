import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.HashMap;
import java.util.Scanner;

import javax.swing.text.DefaultStyledDocument.ElementSpec;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
//Problem: Alphastar Diagnostic

public class recordmilking {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int N = reader.nextInt();
        int M = reader.nextInt();
        int[] recordSpeed = new int[100];
        int[] bessieSpeed = new int[100];
        int nextChange = reader.nextInt();
        int speed = reader.nextInt();

        int bessieBest = 0;
        for (int i = 0; i < 100; i++){
            if (i == nextChange){
                nextChange += reader.nextInt();
                speed = reader.nextInt();
            }
            recordSpeed[i] = speed;
        }
        nextChange = reader.nextInt();
        speed = reader.nextInt();
        for (int i = 0; i < 100; i++){
            if (i == nextChange){
                nextChange += reader.nextInt();
                
                speed = reader.nextInt();
            }
            bessieSpeed[i] = speed;
        }
        for (int i = 0; i < 100; i++){
            int change = bessieSpeed[i]-recordSpeed[i];
            if (change > bessieBest){
                bessieBest = change;
            }
        }

        System.out.println(bessieBest);
    }
}
