import random

sample1 = "now he is gone she said he is gone for good"
sample2 = "there is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here it will instantly disappear and be replaced by something even more bizarre and inexplicable there is another theory which states that this has already happened"

def markhov(s, key_length, output_range):

    '''
    Split a string into a dictionary,
    Keys (prefix) are defined by the key_length argument,
    which hold the value (suffix) -> next value in the string.
    It prints a table and creates a new string, length of values
    equal to the output_range
    '''

    print("\nINPUT:")
    print(f"{s}\n")

    split_string = s.split(" ")

    prefixes = {}                                                        
    string_length = len(split_string)   
    
    while string_length > 0:
        for i in range(0, len(split_string)-(key_length)):              

            current_prefix = ""
            for j in range(0, key_length):
                current_prefix += f"{split_string[j]} "
            try:
                prefixes[current_prefix].append(split_string[key_length])
                string_length -= 1
                break
            except:
                prefixes[current_prefix] = [split_string[key_length]]
                string_length -= 1
            break
        if string_length > key_length:
            split_string.pop(0)
        else:
            break

    # Print the table
    print(f"{'PREFIX':<20}{'SUFFIX':<20}")
    print("================================")
    for key, value in prefixes.items():
        if len(value) > 1:
            print(f"{key:<20}{', '.join(value):<20}")
        else:
            print(f"{key:<20}{value[0]:<20}")
            

    # print(f"\n{prefixes}\n")

    new_string = ""
    for i in range(0, output_range): 
        random_prefix = str(random.choice(list(prefixes.keys())))
        random_suffix = prefixes[random_prefix]

        new_string += random_prefix
        if len(random_suffix) > 1:
            new_string += random.choice(random_suffix) + " "
        else:
            new_string += random_suffix[0] + " "

    print(f"\nOUTPUT:{new_string}\n")

markhov(sample1, 2, 5)
markhov(sample1, 3, 10)

markhov(sample2, 2, 30)