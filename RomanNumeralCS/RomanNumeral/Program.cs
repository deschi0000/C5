using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RomanNumeral
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //Console.WriteLine(DigitToNumeral("17"));
            //Console.WriteLine(DigitToNumeral("15"));
            //Console.WriteLine(DigitToNumeral("125"));
            //Console.WriteLine(DigitToNumeral("1357"));
            //Console.WriteLine(NumeralToDigit("XV"));
            //Console.WriteLine(NumeralToDigit("MCCCLVII"));
            //Console.WriteLine(NumeralToDigit("MMXX"));

            Driver();

        }

        public static string DigitToNumeral(string number)
        {
            
            char[] numberArr = number.ToCharArray();
            int arrLength = numberArr.Length;
            string romanNum = "";
            string nextRomanNum;

            while (arrLength > 0)
            {
                string currentString = new String(numberArr);
                double currentNum = Convert.ToDouble(currentString);
                int currentDigit;
               
                switch (arrLength)
                {
                    case 4:
                        currentDigit = Convert.ToInt32(Math.Floor(currentNum / 1000));
                        nextRomanNum = Numeral("M", currentDigit, "v", "m");      // v and m are placeholders; don't have the special symbols for 5000, 10000...
                        romanNum += nextRomanNum;
                        break;
                    case 3:
                        currentDigit = Convert.ToInt32(Math.Floor(currentNum / 100));
                        nextRomanNum = Numeral("C", currentDigit, "D", "M");      // v and m are placeholders; don't have the special symbols for 5000, 10000...
                        romanNum += nextRomanNum;
                        break;
                    case 2:
                        currentDigit = Convert.ToInt32(Math.Floor(currentNum / 10));
                        nextRomanNum = Numeral("X", currentDigit, "L", "C");      // v and m are placeholders; don't have the special symbols for 5000, 10000...
                        romanNum += nextRomanNum;
                        break;
                    case 1:
                        currentDigit = Convert.ToInt32(Math.Floor(currentNum / 1));
                        nextRomanNum = Numeral("I", currentDigit, "V", "X");      // v and m are placeholders; don't have the special symbols for 5000, 10000...
                        romanNum += nextRomanNum;
                        break;
                }
                arrLength--;
                numberArr = numberArr.Skip(1).ToArray();
            }

            return romanNum;
        }

        public static string Numeral(string n, int digit, string halfNumeral, string nextNumeral)
        {
            // We will check the digit, passing along the appropriate halfnumeral and next numeral denotation.
            // It will return the correct string Numeral.
            string numeral = "";
            try
            {
                switch (digit)
                {
                    case 0:
                        numeral += "";
                        break;
                    case 1:
                        numeral += n;
                        break;
                    case 2:
                        numeral += (n + n);
                        break;
                    case 3:
                        numeral += (n + n + n);
                        break;
                    case 4:
                        numeral += (n + halfNumeral);
                        break;
                    case 5:
                        numeral += halfNumeral;
                        break;
                    case 6:
                        numeral += (halfNumeral + n);
                        break;
                    case 7:
                        numeral += (halfNumeral + n + n);
                        break;
                    case 8:
                        numeral += (halfNumeral + n + n + n);
                        break;
                    case 9:
                        numeral += (n + nextNumeral);
                        break;
                }
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
            return numeral;
        }

        public static int NumeralToDigit(string numeral)
        {
            int totalNum = 0;
            char[] romanArr = numeral.ToUpper().ToCharArray();

            // Iterate through the Array. Check i and i+1. If i+1 is a half numeral (D,L,V) || i is the next full step numeral then i will be subtracted, else added
            // Return the total num

            for (int i = 0; i < romanArr.Length; i++)
            {
                int s = 1;
                //Console.WriteLine($"i:{romanArr[i]}");
                if (i == romanArr.Length - 1)
                {
                    s = 0;
                }

                // Check the half numerals
                try
                {      
                    if (romanArr[i] == 'M')
                    {
                        totalNum += 1000;
                    }
                    else if (romanArr[i] == 'D')
                    {
                        totalNum += 500;
                    }
                    else if (romanArr[i] == 'L')
                    {
                        totalNum += 50;
                    }
                    else if (romanArr[i] == 'V')
                    {
                        totalNum += 5;
                    }

                    // Check the Full numerals then decided whether to subtract or add
                    else if (romanArr[i] == 'C')
                    {
                        if(romanArr[i + s] == 'D' || romanArr[i + s] == 'M')
                        {
                            totalNum -= 100;
                        }
                        else
                        {
                            totalNum += 100;
                        }
                    }
                    else if (romanArr[i] == 'X')
                    {
                        if (romanArr[i + s] == 'L' || romanArr[i + s] == 'C')
                        {
                            totalNum -= 10;
                        }
                        else
                        {
                            totalNum += 10;
                        }
                    }
                    else if (romanArr[i] == 'I')
                    {
                        if (romanArr[i + s] == 'V' || romanArr[i + s] == 'X')
                        {
                            totalNum -= 1;
                        }
                        else
                        {
                            totalNum += 1;
                        }
                    }

                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
            return totalNum;
        }

        public static void Driver()
        {
            string input = "";

            while (input != "q")
            {
                Console.Write("Would you like to Convert [N]umeral to Digit or [D]igit to numeral or [Q]uit? ");
                input = Console.ReadLine();
                int result;

                switch (input.ToLower())
                {
                    case "d":
                        Console.Write("Please enter your number: ");
                        string userNumber = Console.ReadLine();
                        while (!(int.TryParse(userNumber, out result)))
                        {
                            Console.Write("Please enter a valid number: ");
                            userNumber = Console.ReadLine();
                        }
                        string numeral = DigitToNumeral(userNumber);
                        Console.Write($"The number {userNumber} in Roman Numerals is: {numeral}\n\n");
                        break;

                    case "n":
                        Console.Write("Please enter your roman numerals: ");
                        string userNumerals = Console.ReadLine();
                        char[] checkArr = userNumerals.ToLower().ToCharArray();

                        string newDigit = Convert.ToString(NumeralToDigit(userNumerals));
                        Console.Write($"The number {userNumerals} in Roman Numerals is: {newDigit}\n\n");
                        break;
                    case "q":
                        break;
                }
            }
        }
    }
}
