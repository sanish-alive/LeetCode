import java.util.Arrays;
public class ReverseArray {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        for(int i = 0; i < a.length / 2; i++) {
            int tmp = a[i];
            a[i] = a[a.length-i-1];
            a[a.length-i-1] = tmp;
        }
        System.out.println(Arrays.toString(a));
    }
}