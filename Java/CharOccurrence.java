public class CharOccurrence {
    public static void main(String[] args) {
        String userInput = System.console().readLine();
        char find = 'a';
        int count = 0;
        for(int i = 0; i < userInput.length(); i++) {
            if(userInput.charAt(i) == find) {
                count++;
            }
        }
        System.out.println("Occurrence of "+find+" is "+count);
    }
}