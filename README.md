



# Codehort Coding Challenges

A small repository of my submissions to the Coding Challenges at Centennial College's Coding club.

While they differ in size and scope from one another (with the Tamagatchi project and 
the html creater representing two extremes on the spectrum) each was a humble attempt to solve a specific problem.
As such, I felt that, with the exception of Tamagotchi, this readme would serve as a short, general overview for the repos. 


## Convolve
Create a function or method called convolve() that takes a a 2d array of floating point numbers and returns a 2d array of floating point numbers. The function/method will sum every 3x3 section of the 2d array and return a new 2d array based on the summed numbers.
```bash
matrix_1 = [[1, 1, 1, 1, 0], 
            [1, 1, 0, 0, 0], 
            [0, 0, 1, 0, 1], 
            [0.5, 0, 0, 1, 0]]
            
print_output(convolve(matrix_1))

# oputput >>> [[6, 5, 4], [3.5, 3, 3]] 
```

## Marhkov


## Palindrome
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

## RomanNumerals


## RotatingArrays
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

## Tamagotchi

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

## VigenereCipher

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


## htmlCreator
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

## MadLibs

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
