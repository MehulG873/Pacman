import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Scanner;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Acowdemia1 {
    public static void main(String[] args) throws IOException {
        Scanner reader = new Scanner(new BufferedReader(
            new InputStreamReader(System.in)));
        int N = reader.nextInt();
        int L = reader.nextInt();
        int hI;
        HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
        List<Integer> citations = new ArrayList<Integer>(N);
        for (int i = 0; i < N; i++){
            int n = reader.nextInt();
            citations.add(n);
            if (counts.get(n) == null){
                counts.put(n, 1);
            }
            else{
                counts.put(n, counts.get(n) + 1);
            }
        }
        citations = mergeSort(citations);
        hI = getHIndex(citations);
        for (int i = citations.size() - 1; i > - 1; i--) {
            if (i == citations.size() - 1){
                int n = citations.get(i) + 1;
                int numLeft = n - citations.size() + i + 1;
                if ((n > hI && counts.get(n - 1) != null &&
                    counts.get(n-1) >= numLeft && numLeft <= L)){
                        //System.out.println(n);
                        hI = n;
                }
            }
            for (int n = citations.get(i); (i - 1) >= 0 && n > citations.get(i-1); n--){
                int numLeft = n - citations.size() + i;
                if ((n > hI && counts.get(n - 1) != null &&

                    counts.get(n-1) >= numLeft && numLeft <= L)){
                        //System.out.println(n);
                        hI = n;

                }
            }
            //System.out.println(n);
        }

        System.out.println(hI);        
    }

    public static List<Integer> mergeSort(List<Integer> L) {
        if (L.size() < 2){
            return L;
        }
        List<Integer> first = mergeSort(L.subList(0, L.size()/2));
        List<Integer> last = mergeSort(L.subList(L.size()/2, L.size()));
        List<Integer> sorted = new ArrayList<Integer>();
        int fIndex = 0;
        int lIndex = 0;
        while (fIndex != first.size()) {
            if (first.get(fIndex) < last.get(lIndex)) {
                sorted.add(first.get(fIndex));
                fIndex ++;
            }
            else{
                sorted.add(last.get(lIndex));
                lIndex ++;
            }
            if (lIndex == last.size()) {
                sorted.addAll(first.subList(fIndex, first.size()));
                break;
            }
        }
        sorted.addAll(last.subList(lIndex, last.size()));
        return sorted;
    }

    public static int getHIndex(List<Integer> citations){
        int hI = 0;
        for (int i = 0; i < citations.size(); i++){
            if (citations.get(i) > (citations.size() - i)) {
                break;
            }
            hI = citations.get(i);
        }
        return hI;
    }
}