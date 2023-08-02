
public class Vowel {
    public static void main(String[] args) {
        System.out.print("Enter text :: ");
        String userInput = System.console().readLine();
        int[] counts = isVowel(userInput.toLowerCase());
        int vowelCount = counts[0];
        int consonantCount = counts[1];

        System.out.println("Vowel: "+vowelCount+" and Consonant: "+consonantCount);

    }

    public static int[] isVowel(String str) {
        int vowelCount = 0, consonantCount = 0;
        String vowels = "aeiou";

        for(char ch : str.toCharArray()) {
            if(vowels.contains(String.valueOf(ch))){
                vowelCount++;
            } else if (Character.isLetter(ch)) {
                consonantCount++;
            }
        }

        int[] counts = {vowelCount, consonantCount};
        return counts;
    }
}