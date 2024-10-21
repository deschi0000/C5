def main():

    change(187)
    change(2461)
    # change(0)

    

def change(total_amount):
    ''''''
    print(f"Total Amount: {total_amount}")

    total_bills = 0
    bill_dict = {
        500:0,
        100:0,
        25:0,
        10:0,
        5:0,
        1:0
    }

    for i in bill_dict.keys():
        num_of_notes = total_amount // i
        total_amount -= (num_of_notes * i)
        if num_of_notes == 0:
            continue
        else:
            total_bills += num_of_notes 
            bill_dict[i] += num_of_notes


    print(f"Number of Bills: {total_bills}")
    print("Bills Breakdown: " + str(bill_dict))

if __name__ == "__main__":
    main()