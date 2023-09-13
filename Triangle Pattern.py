import random
error = ["Wrong Value, please try again.","Please input the right value.","Try again.","Value Error."]
error_val = random.choice(error)

try:    
    detection_integer = int(input("Enter an integer: "))

    detection_character = input("Enter a Character: ")
    
    
    for i in range(detection_integer + 1):
        path = detection_character * i
        print(path)
        
except ValueError:
    print(error_val)

