def vignere_encode(codeword, message):

    # message = "thepackagehasbeendelivered"
    # codeword = "snitch"
    codeword_repeated_array = []
    message_array = [i for i in message]
    codeword_array = [i for i in codeword]
    codeword_array_length = len(codeword_array)

    for index, letter in enumerate(message_array):    
        codeword_repeated_array.append(codeword_array[index % codeword_array_length])

            
    # print(codeword_repeated_array)
    # for index, letter in enumerate(message_array):
    #     print(str(index) + " " + message_array[index] + " " + codeword_repeated_array[index])

    encoded_message = []

    for index, char in enumerate(message_array):
            shift_value = ord(codeword_repeated_array[index]) - ord("a") # (97 in ascii), resulting in alphabet index
            # print(f"char: {char} | shift_value: {shift_value}")

            shifted_index = (ord(char) - ord("a") + shift_value) % 26
            result = chr(shifted_index + ord("a"))
            encoded_message.append(result)

    return "".join(encoded_message)

print("ENCODING: ")
print(vignere_encode("snitch", "thepackagehasbeendelivered"))
print(vignere_encode("train", "murderontheorientexpress"))
print(vignere_encode("garden ", "themolessnuckintothegardenlastnight"))

def vignere_decode(codeword, coded_message):

    # message = "thepackagehasbeendelivered"
    # codeword = "snitch"
    codeword_repeated_array = []
    message_array = [i for i in coded_message]
    codeword_array = [i for i in codeword]
    codeword_array_length = len(codeword_array)

    for index, letter in enumerate(message_array):    
        codeword_repeated_array.append(codeword_array[index % codeword_array_length])

    # print(f"repeated array: {codeword_repeated_array}")           
    # print(codeword_repeated_array)
    # for index, letter in enumerate(message_array):
    #     print(str(index) + " " + message_array[index] + " " + codeword_repeated_array[index])

    decoded_message = []

    for index, char in enumerate(message_array):
            shift_value = ord(codeword_repeated_array[index % codeword_array_length]) - ord("a") # (97 in ascii), resulting in alphabet index
            # print(f"char: {char} | shift_value: {shift_value}")

            shifted_index = (ord(char) - ord("a") - shift_value) % 26
            result = chr(shifted_index + ord("a"))
            decoded_message.append(result)

    return "".join(decoded_message)

print("\nDECODING")
print(vignere_decode("snitch", "lumicjcnoxjhkomxpkwyqogywq"))
print(vignere_decode("train", "flrlrkfnbuxfrqrgkefckvsa"))
print(vignere_decode("cloak", "klatrgafedvtssdwywcyty"))
print(vignere_decode("python", "pjphmfamhrcaifxifvvfmzwqtmyswst"))
print(vignere_decode("moore", "rcfpsgfspiecbcc"))