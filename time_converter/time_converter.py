from datetime import timedelta

time_dict = {
    "s": "seconds",
    "m": "minutes",
    "h": "hours",
    "d": "days"
}

def main():

    # Retrieve the time unit converting from, from the user
    time_unit_from = get_time_unit_from()

    # Retrieve the time amount
    old_time = get_time()
    
    # Retrieve the time unit converting from, from the user
    time_unit_to = get_time_unit_to()

    # Convert to the new time using the inputs
    new_time = convert_time(time_unit_from, time_unit_to, old_time)    

    return f"{old_time:.1f} {time_dict[time_unit_from]} = {new_time:.1f} {time_dict[time_unit_to]}"


def convert_time(converting_from, converting_to, input_time):
    '''Takes a conversion unit and time, 
                    returning the new time'''
    
    if converting_to == "s":
        if converting_from == "m":
            return int(timedelta(minutes=input_time).total_seconds())
        elif converting_from == "h":
            return int(timedelta(hours=input_time).total_seconds())
        elif converting_from == "d":
            return int(timedelta(days=input_time).total_seconds())
        else:
            return "Invalid conversion unit."

    if converting_to == "m":
        if converting_from == "s":
            return input_time / 60
        elif converting_from == "h":
            return input_time * 60
        elif converting_from == "d":
            return input_time * 1440  # 24hrs*60mins
        else:
            return "Invalid conversion unit."

    if converting_to == "h":
        if converting_from == "s":
            return input_time / 3600  # 60secs*60mins
        elif converting_from == "m":
            return input_time / 60
        elif converting_from == "d":
            return input_time * 24
        else:
            return "Invalid conversion unit."

    if converting_to == "d":
        if converting_from == "s":
            return input_time / 86400  # 60secs*60mins*24hrs
        elif converting_from == "m":
            return input_time / 1440  # 24hrs*60mins
        elif converting_from == "h":
            return input_time / 24
        else:
            return "Invalid conversion unit."

    return "Invalid conversion target."


def get_time_unit_from():
    '''Gets the unit of time from a user'''

    convert_from = ""
    while convert_from not in ("d","h","m","s"):
        convert_from = input("Converting from [d]ays, [h]ours, [m]inutes or [s]econds: ")
    return convert_from


def get_time_unit_to():
    '''Gets the unit of time from a user'''

    convert_to = ""
    while convert_to not in ("d","h","m","s"):
        convert_to = input("Converting [d]ays, [h]ours, [m]inutes or [s]econds: ")
    return convert_to


def get_time():
    '''Gets the unit of time from a user'''
    while True:
        user_input = input("Enter a positive rational / whole number for time: ")
        try:
            user_time_input = float(user_input)
            if user_time_input > 0:
                return user_time_input
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a positive rational / whole number.")

if __name__ == "__main__":
    print(main())
