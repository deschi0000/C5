using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumeralFunctions
{
    public class Class1
    {
        public static int NumeralToDigit(string numeral)
        {
            int totalNum = 0;
            char[] romanArr = numeral.ToUpper().ToCharArray();

            // Iterate through the Array. Check i and i+1. If i+1 is a half numeral (D,L,V) || i is the next full step numeral then i will be subtracted, else added
            // Return the total num

            for (int i = 0; i < romanArr.Length; i++)
            {
                int s = 1;
                Console.WriteLine($"i:{romanArr[i]}");
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
                        if (romanArr[i + s] == 'D' || romanArr[i + s] == 'M')
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
                catch (IndexOutOfRangeException e)
                {
                    Console.WriteLine(e.Message);
                }
            }
            return totalNum;
        }
    }
}
