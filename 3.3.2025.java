import java.util.Scanner;

public class RemoveSpaces {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("give a sentence:");
        String input = scanner.nextLine();
      
        
        String output = input.trim().replaceAll("\\s+", " ");
        System.out.println(output);

        System.out.println(" output is:");
        System.out.println(output);
    }
}
import java.util.Scanner;

public class Transform {
    public static void main(String[] args) {
       
        Scanner scanner = new Scanner(System.in);
        System.out.print("enter a string: ");
        String input = scanner.nextLine();
       

        String output = transform(input);

        System.out.println( output);
    }

    public static String transform(String str) {

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (Character.isDigit(ch)) {
                int repeat = Character.getNumericValue(ch); 

              
                char lastChar;
                if (result.length() > 0) {
                    lastChar = result.charAt(result.length() - 1);
                } else {
                    lastChar = ' '; 
                }

                
                for (int j = 0; j < repeat - 1; j++) {
                    result.append(lastChar);
                }
            } else {
               
                result.append(ch);
            }
        }

        
        return result.toString();
    }
}
