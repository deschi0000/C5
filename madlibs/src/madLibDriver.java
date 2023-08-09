import java.util.Random;
import java.util.Scanner;

public class madLibDriver {


    public static void main(String[] args) {

        System.out.println("Welcome to Madlibs");

        String[] templateArray = getTemplate();
        String[] finalMadLib = buildMadLib(templateArray);

        System.out.println(String.join("Your Madlib: "));
        System.out.println(String.join(" ", finalMadLib));

    }


    public static String[] buildMadLib(String[] template) {
        String[] finalMadLib = new String[template.length];
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < template.length; i++) {
            String response;
            if (template[i] == "EXCL") {
                System.out.println("Please enter an exclamation (with !): ");
                response = input.next();
                finalMadLib[i] = response;
            } else if (template[i] == "NOUN") {
                System.out.println("Please enter a noun: ");
                response = input.next();
                finalMadLib[i] = response;
            } else if (template[i] == "ADJ") {
                System.out.println("Please enter an adjective: ");
                response = input.next();
                finalMadLib[i] = response;
            } else if (template[i] == "ADV") {
                System.out.println("Please enter an adverb: ");
                response = input.next();
                finalMadLib[i] = response;
            } else if (template[i] == "PLACE") {
                System.out.println("Please enter a place: ");
                response = input.next();
                finalMadLib[i] = response;
            } else {
                finalMadLib[i] = template[i];
            }
        }

        return finalMadLib;
    }

    public static String[] getTemplate() {

        Random random = new Random();

        String[][] templates = {
                {"EXCL", "he said", "ADV", "as he jumped into his convertible", "NOUN", "and drove off with his", "ADJ", "wife."}
        };

        int randomIndex = random.nextInt(templates.length);

        return templates[randomIndex];
    }

}