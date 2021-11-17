import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;


//AlphaStar Diagnostic Exam
public class paint {
    public static void main(String[] args) {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int a = reader.nextInt();
        int b = reader.nextInt();
        int c = reader.nextInt();
        int d = reader.nextInt();
        int sum = 0;
        sum += (b-a) + (d-c);
        if ( a<c){
            if (d < b){
                sum -= (d-c);
            }
            else if (b-c > 0){
                sum -= (b-c);
            }
        }
        else{
            if (b < d){
                sum -= (b-a);
            }
            else if (d-a > 0){
                sum -= (d-a);
            }
        }
        // }
        // sum = (b - a) + (d - c);
        // if (d - a > 0){
        //     sum -= (d-a);
        // }
        // else if (b-c > 0) {
        //     sum -= (b-c);
        // }

        System.out.println(sum); 
    }
}
