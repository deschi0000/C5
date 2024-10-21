



# Codehort Coding Challenges (Python)

A small repository of my submissions to the Coding Challenges at Centennial College's Coding club.

While they differ in size and scope from one another (with the Tamagatchi project and 
the html creater representing two extremes on the spectrum) each was a humble attempt to solve a specific problem.
As such, I felt that, with the exception of Tamagotchi, this readme would serve as a short, general overview for the repos. 


## Convolve (Python)
Create a function or method called convolve() that takes a a 2d array of floating point numbers and returns a 2d array of floating point numbers. The function/method will sum every 3x3 section of the 2d array and return a new 2d array based on the summed numbers.
```bash
matrix_1 = [[1, 1, 1, 1, 0], 
            [1, 1, 0, 0, 0], 
            [0, 0, 1, 0, 1], 
            [0.5, 0, 0, 1, 0]]
            
print_output(convolve(matrix_1))

# oputput >>> [[6, 5, 4], [3.5, 3, 3]] 
```

## Marhkov (Python)
A Markov chain algorithm basically determines the next most probable suffix word for a given prefix. 
To do this, a Markov chain program typically breaks an input text (training text) into a series of words, then by sliding along them in some fixed sized window, storing the first N words as a prefix and then the N + 1 word as a member of a set to choose from randomly for the suffix.
now he is gone she said he is gone for good

```bash
INPUT: now he is gone she said he is gone for good

PREFIX              SUFFIX
================================
now he              is
he is               gone, gone
is gone             she, for
gone she            said
she said            he
said he             is
gone for            good

OUTPUT: she said he she said he is gone she gone she said gone for good is gone she gone for good said he is he is gone he is gone

```

## Palindrome (Python)
Given a positive whole number, find the smallest palindrome greater than the given number.
```bash
$ python palindrome.py
0 => 11
808 => 818
999 => 1001
2133 => 2222
4128 => 4224
629 => 636
4052555153018976267 => 4052555153515552504
```

## RomanNumerals (JS)
A program that can convert Roman Numerals to Decimal numbers and Decimal numbers to Roman Numerals.
```bash
Symbol     I    V    X     L      C      D       M
Value      1    5    10    50    100    500    1000
```

```bash
console.log(romanToNum("IV"));
console.log(romanToNum("MMMXVIII"));
console.log(romanToNum("CDXLIX"));

┌─────────┬────────┐
│ (index) │ Values │
├─────────┼────────┤
│    0    │  'I'   │
│    1    │  'V'   │
└─────────┴────────┘
4
┌─────────┬────────┐
│ (index) │ Values │
├─────────┼────────┤
│    0    │  'M'   │
│    1    │  'M'   │
│    2    │  'M'   │
│    3    │  'X'   │
│    4    │  'V'   │
│    5    │  'I'   │
│    6    │  'I'   │
│    7    │  'I'   │
└─────────┴────────┘
3018
┌─────────┬────────┐
│ (index) │ Values │
├─────────┼────────┤
│    0    │  'C'   │
│    1    │  'D'   │
│    2    │  'X'   │
│    3    │  'L'   │
│    4    │  'I'   │
│    5    │  'X'   │
└─────────┴────────┘
449

```

## RomanNumerals (C#)
The same program specifications, but written as a console program using C#.

```bash
Would you like to Convert [N]umeral to Digit or [D]igit to numeral or [Q]uit? n
Please enter your roman numerals: cdlvii
The number cdlvii in Roman Numerals is: 457

Would you like to Convert [N]umeral to Digit or [D]igit to numeral or [Q]uit? d
Please enter your number: 1977
The number 1977 in Roman Numerals is: MCMLXXVII

Would you like to Convert [N]umeral to Digit or [D]igit to numeral or [Q]uit?

```


## RotatingArrays (Java)
Given a NxN size 2D array of numbers. Develop a way to rotate the data as if you rotated the data by 90 degrees clockwise.

```bash
How many times would you like to rotate? 90 / 180 / 270?: 90

Original Array:
1 2 3
4 5 6
7 8 9

Rotated Array:
7 4 1
8 5 2
9 6 3
```

## Tamagotchi (Python)

A virtual pet whose life you must sustain through various activities including eating, playing, making it sleep, and cleaning its poop. 
Tamagotchi's go through several life cycles, most notably, egg/infant, teen, adult, elderly. Tamagotchi's can die from lack of attention (in the classic ones, half a day of neglect would kill it) and also from age.

Requirements:
```bash
* Capable of being fed
* Capable of being put to bed
* Capable of going to sleep on its own, losing health from hunger and pooping on its own without prompting
* Capable of aging from birth through to death
```
Check out the repo for the in-depth readme: https://github.com/deschi0000/Codehort/tree/main/Tamagotchi 

## VigenereCipher (Python)

The cipher involves alphabet substitution using a shared keyword. Both people exchanging messages must agree on the secret keyword.  
To be effective, this keyword should not be written down anywhere, but memorized.

```bash
print(vignere_encode("python", "alwayslookonthebrightsideoflife"))
print(vignere_encode("moore ", "foryoureyesonly"))

ENCODING:
pjphmfamhrcaifxifvvfmzwqtmyswst
rcfpshdsmvwbzzm
```
```bash
print(vignere_decode("python", "pjphmfamhrcaifxifvvfmzwqtmyswst"))
print(vignere_decode("moore", "rcfpsgfspiecbcc"))

DECODING:
alwayslookonthebrightsideoflife
foryoureyesonly
```

## DnD
Dice Roller! One major part of making character sheets is rolling the character's stats. 
The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.
The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.

Output: The output the sum of all the rolls of that specified die, each on their own line.
```bash
$ python dnd_dice.py
Welcome to DND Dice
Please enter a dnd die (i.e. 3d6): 3d6
Would you like add another? (y/n) y
Please enter a dnd die (i.e. 3d6): 5d12
Would you like add another? (y/n) n
3d6 = 8
5d12 = 30
```


## htmlCreator (Python)
Devise a program that will automatically write all of the HTML for you

Input: On standard console input you should be prompted to enter a paragraph.
Output: Once your paragraph has been entered, it should be saved as a valid HTML file and opened in your default browser to display the results.

```bash
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title></title>
        </head>

        <body>
            <p>This is my paragraph entry</p>
        </body>
    </html>
```
Bonus: A stylesheet is also generated

## MadLibs (Java)

Mad Libs contain short stories with many key words replaced with blanks. Beneath each blank is specified a category, such as "noun", "verb", "place", "celebrity", "exclamation" or "part of the body". One player asks the other players, in turn, to contribute a word of the specified type for each blank, but without revealing the context for that word. Finally, the completed story is read aloud. The result is usually a sentence which is comical, surreal and/or takes on somewhat of a nonsensical tone.

```bash
Welcome to MadLibs
Please enter a(n) EXCLAMATION(!): Heck!
Please enter a(n) ADVERB: lazily
Please enter a(n) NOUN: banana
Please enter a(n) ADJECTIVE: lovely
Your funny MadLib:
Heck! he said lazily as he jumped into his convertible banana and drove off with his lovely wife.

```

## Time Converter (Python)
A simple converter that can convert between seconds, minutes, hours and days
```bash
Converting from [d]ays, [h]ours, [m]inutes or [s]econds: m
Enter a positive rational / whole number for time: 90
Converting [d]ays, [h]ours, [m]inutes or [s]econds: h
90.0 minutes = 1.5 hours

Converting from [d]ays, [h]ours, [m]inutes or [s]econds: m
Enter a positive rational / whole number for time: 0.5
Converting [d]ays, [h]ours, [m]inutes or [s]econds: s
0.5 minutes = 30.0 seconds
```

