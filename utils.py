def get_marks():
    """
    Asks for 3 marks
    """
    marks = []
    for i in range(3):
        marks.append(get_number(f"Please insert the mark in the position number {i+1} (or None if not presented): "))
    return marks

def get_number(message):
    """
    Recieves a message to print in the input. Checks the input is a number and is positive.
    Returns None if None is typed.
    """
    while True:
        number = input(message)
        if number.lower() == "none":
            number = None
            break

        else:
            try: 
                number = float(number)
            except ValueError:
                print("Error. Please, insert a valid number.")
        if number < 0 or number > 10:
            print("Please insert a positive number below or equal to 10.")
            continue
        else:
            break
    return number

def average_list(lst):
    sum = 0
    for element in lst:
        sum += element
    return sum / len(lst)