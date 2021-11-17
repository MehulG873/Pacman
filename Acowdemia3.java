import java.util.Scanner;
import java.util.Set;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Arrays;

//Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=1133
//FAILED
// public class Acowdemia3 {
//     public static void main(String[] args) {
//         Scanner reader = new Scanner(new BufferedReader(
//             new InputStreamReader(System.in)));
//         int N = reader.nextInt();
//         int M = reader.nextInt();
//         AcowdemiaCow[][] field = new AcowdemiaCow[N][M];
//         char[][] fieldTypes = new char[N][M];
//         // Set<int[]> cows = new HashSet<int[]>();
//         // Set<int[]> grass = new HashSet<int[]>();
//         HashMap<int[], Set<AcowdemiaCow>> grass = new HashMap<int[], Set<AcowdemiaCow>>();
//         int friends = 0; 
//         reader.nextLine();

//         //Creating fieldTypes
//         for (int i =0; i < N; i++)

//         //Created all Cows
//         for (int i =0; i < N; i++){
//             String line = reader.nextLine();
//             for (int j = 0; j <M; j++){
//                 char type = line.charAt(j);
//                 if (type == 'C'){
//                     if (cows.get(i) == null){
//                         cows.put(i, new HashSet<Integer>());
//                     }
//                     cows.get(i).add(j);
//                     field[i][j] = new AcowdemiaCow(new int[] {i, j});
//                 }
//                 else if (type == 'G'){
//                     if (grass.get(i) == null){
//                         grass.put(i, new HashSet<Integer>());
//                     }
//                     grass.get(i).add(j);
//                 }
//             }
//         }

//         //Checked for Friends
//         for (int i: grass.keySet()){
//             for (int j: grass.get(i)){
                
//                 for (int dr = -1; dr < 2; dr += 2){

//                 }
//                 for (int dc = -2; dc < 3; dc += 4){
//                     int[] possibleFriend = new int[] {i, j + dc};
//                     int[] meetingPoint = new int[] {i, j + dc/2};
//                     if (isInside(possibleFriend, N, M) &&
//                         cows.get(possibleFriend[0]) != null && cows.get(possibleFriend[0]).contains(possibleFriend[1]) &&
//                         grass.get(meetingPoint[0]) != null && grass.get(meetingPoint[0]).contains(meetingPoint[1])){
//                         friends ++;
//                         grass.get(meetingPoint[0]).remove(meetingPoint[1]);
//                     }
//                     // else if (i == 1 && j == 1){
//                     //     if (isInside(possibleFriend, N, M) &&
//                     //         cows.get(possibleFriend[0]) != null && cows.get(possibleFriend[0]).contains(possibleFriend[1]) &&
//                     //         grass.get(meetingPoint[0]) != null && grass.get(meetingPoint[0]).contains(meetingPoint[1])){
//                     //         friends ++;
//                     //         grass.get(meetingPoint[0]).remove(meetingPoint[1]);
//                     //     }                       
//                     // }
//                 }

//             }
//         }
//         System.out.println(friends);
//     }

//     public static boolean isInside(int[] pos, int N, int M) {
//         return pos[0] >= 0 && pos[1] >= 0 && pos[0] < N && pos[1] < M;
//     }
// }
// class AcowdemiaCow{
//     int[] cord;
//     Set<AcowdemiaCow> friends = new HashSet<AcowdemiaCow>();

//     public AcowdemiaCow(int[] cord){
//         this.cord = cord;
//     }

//     public void addFriend(AcowdemiaCow friend){
//         friends.add(friend);
//     }

//     public boolean isFriend(AcowdemiaCow friend){
//         return friends.contains(friend);
//     }
// }