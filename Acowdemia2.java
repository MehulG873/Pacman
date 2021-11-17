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
//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=1132 
public class Acowdemia2 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int K = reader.nextInt();
        int N = reader.nextInt();
        String[] names = new String[N];
        HashMap<String, HashSet<String>> juniors = new HashMap<String, HashSet<String>>();
        //Setting Up Junior Map to tell each person's juniors
        for (int i = 0; i < N; i++){
            String name = reader.next();
            names[i] = name;
            juniors.put(name, new HashSet<String>());
        }
        reader.nextLine();
        //Adding juniors of each name
        for (int i = 0; i < K; i++){
            HashSet<String> lowers = new HashSet<String>();
            String[] line = new String[N];
            for (int j = 0; j < N; j++){
                line[j] = reader.next();
            }
            HashSet<String> sameLevel = new HashSet<String>();
            if (line[1].compareTo(line[0]) >= 0){
                sameLevel.add(line[0]);
            }
            else{
                lowers.add(line[0]);
            }
            for (int j = 1; j < N; j++){
                if (line[j].compareTo(line[j-1]) >= 0){
                    sameLevel.add(line[j]);
                    sameLevel.add(line[j-1]);
                }
                else{
                    lowers.addAll(sameLevel);
                }
                juniors.get(line[j]).addAll(lowers);  
            }
           //System.out.println(juniors);
        }
        //Printing Out Juniors in Proper Format
        for (int i = 0; i < N; i++){
            for (int j = 0; j<N; j++){
                if (i == j) System.out.print('B');
                else{
                    if (juniors.get(names[i]).contains(names[j])){
                        System.out.print(1);
                    }
                    else if (juniors.get(names[j]).contains(names[i])){
                        System.out.print(0);
                    }
                    else System.out.print('?');
                }
            }
            System.out.println();
        }
    }
}

