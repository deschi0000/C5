import java.util.*;

public class madLibDriver {
    public static void main(String[] args) {

        System.out.println("Welcome to Madlibs");
        String[] templateArray = getTemplate();
        String[] finalMadLib = buildMadLib(templateArray);
        System.out.println("Your funny MadLib:");
        System.out.println(String.join(" ", finalMadLib));
    }

    public static String[] buildMadLib(String[] template) {
        String[] finalMadLib = new String[template.length];
        Scanner input = new Scanner(System.in);

        String[] words = {"EXCLAMATION(!)", "NOUN", "ADJECTIVE", "ADVERB", "PLACE"};
        ArrayList<String> wordTypes = new ArrayList<>(Arrays.asList(words));

        for (int i = 0; i < template.length; i++) {
            String response;
            if (wordTypes.contains(template[i])) {
                System.out.printf("Please enter a(n) %s: ", template[i]);
                response = input.next();
                finalMadLib[i] = response;
            }
            else {
                finalMadLib[i] = template[i];
            }
        }
        return finalMadLib;
    }

    public static String[] getTemplate() {

        Random random = new Random();
        String[][] templates = {
                {"EXCLAMATION(!)", "he said", "ADVERB", "as he jumped into his convertible", "NOUN", "and drove off with his", "ADJECTIVE", "wife."}
        };

        int randomIndex = random.nextInt(templates.length);

        return templates[randomIndex];
    }
}
