with open("one_test.txt", "r") as input_file:

    current_value=0
    highest_value=0
    for line in input_file:
        stripped = line.strip()
        if stripped != "": 
            current_value=current_value+int(stripped)
        else:
            current_value=0
        if highest_value<current_value:
            highest_value=current_value
    print(highest_value)             


