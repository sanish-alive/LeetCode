
public class MatchingElement {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 1, 6, 7, 2, 8, 5};
        for(int i = 0; i < arr.length; i++){
            for(int j = i+1; j < arr.length; j++){
                if(arr[i]==arr[j]) {
                    System.out.println(arr[i]);
                }
            }
        }
    }
}