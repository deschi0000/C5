'''
Next Palindrome
A palindrome is a whole number that's the same when read backward in base 10, such as 12321 or 9449.

Given a positive whole number, find the smallest palindrome greater than the given number.

    nextpal(808) => 818
    nextpal(999) => 1001
    nextpal(2133) => 2222


For large inputs, your solution must be much more efficient than incrementing and checking each subsequent number to see if it's a palindrome. 
Find nextpal(3^(39)) before posting your solution. Depending on your programming language, it should take a fraction of a second.


'''

def palindrome(num):

    if num + 0 == 0:
        num += 10

    arr = [i for i in str(num)]
    length = len(arr)
    

    if len(set(arr)) == 1:
        num += 1
        arr = [i for i in str(num)]
        length = len(arr)

    # if round((num/10 - num//10),1) == 0.9:
    #     num += 1    
    #     arr = [i for i in str(num)]
    #     length = len(arr)
    #     print("yes")


    if len(arr) % 2 != 0:                                        # If it is an odd numbered array
        middleindex = length // 2

        if arr[middleindex+1] > arr[middleindex]:               
            arr[middleindex] = str(int(arr[middleindex])+1)      # If middle index is lower than next, increment middle first
        
        for i in range(middleindex):                             # Increment after the middle index
            arr[length-1-i] = arr[i]

        # print(arr)
        return int(''.join(arr))

    if len(arr) % 2 == 0:
        middleindex = length // 2

        if arr[middleindex] > arr[middleindex-1]:
            arr[middleindex-1] = str(int(arr[middleindex-1])+1) 

        for i in range(middleindex):
            arr[length-1-i] = arr[i]    

        # print(arr)
        return int(''.join(arr))


if __name__ == '__main__':

    # user_input = int(input("Type in a number: "))
    # print(f"the next palindrome higher than {user_input} is {palindrome(user_input)}")
    test_cases = [0, 808, 999, 2133, 4128, 629, 3**39]
    for i in test_cases:
        # print(f"the next palindrome higher than {i} is {palindrome(i)}")
        print(f"{i} => {palindrome(i)}")

    # palindrome()
