import java.util.Random;
import java.util.Scanner;

public class madLibDriver {


    public static void main(String[] args) {

        System.out.println("Welcome to Madlibs");

        String[] templateArray = getTemplate();

        String[] finalMadLib = buildMadLib(templateArray);

        System.out.println(String.join(" ", finalMadLib));

    }


    public static String[] buildMadLib(String[] template) {
        String[] finalMadLib = new String[template.length];

        for (int i = 0; i < template.length; i++) {
            String response;
            if (template[i] == "EXCL"){
                response = getExclamation();
                finalMadLib[i] = response;
            }
            else if (template[i] == "NOUN"){
                response = getNoun();
                finalMadLib[i] = response;
            }
            else if (template[i] == "ADJ"){
                response = getAdjective();
                finalMadLib[i] = response;
            }
            else if (template[i] == "ADV"){
                response = getAdverb();
                finalMadLib[i] = response;
            }
            else if (template[i] == "PLACE"){
                response = getPlace();
                finalMadLib[i] = response;
            } else {
                finalMadLib[i] = template[i];
            }
        }

        return finalMadLib;
    }

    public static String[] getTemplate(){

        Random random = new Random();

        String[][] templates = {
                {"","EXCL", "he said", "ADV", "as he jumped into his convertible", "NOUN", "and drove off with his", "ADJ", "wife."}
        };

        int randomIndex = random.nextInt(templates.length);
        return templates[randomIndex];
    }

    public static String getAdjective(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter an adjective: ");
        String adjective = input.next();

        return adjective;
    }

    public static String getAdverb(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter an adverb: ");
        String adverb = input.next();

        return adverb;
    }

    public static String getNoun(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a noun: ");
        String noun = input.next();

        return noun;
    }

    public static String getExclamation(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter an exclamation (with !): ");
        String exclamation = input.next();

        return exclamation;
    }

    public static String getPlace(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter a place: ");
        String exclamation = input.next();

        return exclamation;
    }
}

