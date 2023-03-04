// Convert a roman numeral to a digit
function numToRoman(number) {

    // I, II, III, IV, V, VI, VII, VIII, IX
    // X, XX, XXX, XL, L, LX, LXX, LXXX, XC
    // C, CC, CCC, CD, D, DC, DCC, DCCC, CM
    // M

    let numString = number.toString();
    // console.log(numString);
    // console.log(`type: ${typeof(numString)}`);

    let numArr = numString.split("");
    let length = numArr.length
    let romanNum = "";
    let nextRomanNum = "";
    // console.log(`Original Num: ${number}`);
    while (length > 0) {

        switch (length) {
            case 4:
 
            // console.table(numArr);
                // console.log("1000s");
                nextRomanNum = romanMethod("M", Math.floor(numArr.join("") / 1000), "v","m");
                romanNum += nextRomanNum;
                break;
            case 3:
                // console.table(numArr);
                // console.log("100s");
                nextRomanNum = romanMethod("C", Math.floor(numArr.join("") / 100), "D", "C");
                romanNum += nextRomanNum;
                break;
            case 2:
                // console.table(numArr);
                // console.log("10s");
                nextRomanNum = romanMethod("X", Math.floor(numArr.join("") / 10), "L", "C");
                romanNum += nextRomanNum;
                break;
            case 1:
                // console.table(numArr);
                // console.log("1s");
                nextRomanNum = romanMethod("I", Math.floor(numArr.join("") / 1), "V", "X");
                romanNum += nextRomanNum;
                break;
        }
        length--;
        numArr.shift();
    }
    console.log(`Current Roman Num Total " ${romanNum}`);
    return romanNum;
    
}

// Convert a digit to roman numeral
function romanMethod(s, num, half, next) {
    console.log(`s:${s} and number:${num}`);

    switch (num) {
        case 0:
            return "";
        case 1:
            return s;

        case 2:
            return s + s;

        case 3:
            return s + s + s;

        case 4:
            return s + half;

        case 5:
            return half;

        case 6:
            return half + s;

        case 7:
            return half + s + s;

        case 8:
            return half + s + s + s;

        case 9:
            return s + next;
    }
}

// console.log(numToRoman(248));
// console.log(numToRoman(2784));



function romanToNum(string) {    
    // I, II, III, IV, V, VI, VII, VIII, IX
    // X, XX, XXX, XL, L, LX, LXX, LXXX, XC
    // C, CC, CCC, CD, D, DC, DCC, DCCC, CM
    // M

    // How to parse?
    let num = 0;

    let romanArr = string.toUpperCase().split("");
    console.table(romanArr);

    for (let i = 0; i < romanArr.length; i ++){

        if (romanArr[i] === "M"){
            num += 1000;
        } else if (romanArr[i] === "D") {
            num += 500;
        } else if (romanArr[i] === "L") {
            num += 50;      
        } else if (romanArr[i] === "V") {
            num += 5;
        } else if (romanArr[i] === "C"){
            if (romanArr[i+1] === "D" || romanArr[i+1] === "M"){
                num -= 100;
            } else {
                num += 100;
            }
        } else if (romanArr[i] === "X"){
            if (romanArr[i+1] === "L" || romanArr[i+1] === "C"){
                num -= 10;
            } else {
                num += 10;
            }
        } else if (romanArr[i] === "I"){
            if (romanArr[i+1] === "V" || romanArr[i+1] === "X"){
                num -= 1;
            } else {
                num += 1;
            }
        }
    }

    return num;
}

// console.log(romanToNum("IV"));
// console.log(romanToNum("MMMXVIII"));
// console.log(romanToNum("CDXLIX"));
