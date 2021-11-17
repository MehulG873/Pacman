import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Sorting {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < 100; i++) list.add(i);
        Collections.shuffle(list);
        System.out.println(mergeSort(list));

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
}
