# import sys

# INFINITE LOOP: OPTIONAL
# for i in range(sys.maxsize**10)
    
print("Temperature Converter\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
number_input = input("Enter your choice: ")
print("---------------------------------------\n \n")
choices = ["1","2"]
try:
    
        if number_input == "1":
            back = ("3")
            print("}{CELSIUS TO FAHRENHEIT}{\n3. Back")
            detect_celsius = int(input("Celsius: "))
            fahrenheit = float((1.8 * detect_celsius) + 32)
            print(f"Fahrenheit: {fahrenheit}")
                
                
        elif number_input == "2":
            print("}{FAHRENHEIT TO CELSIUS}{")
            detect_fahrenheit = int(input("Fahrenheit: "))
            celsius = float((detect_fahrenheit - 32) * 5/9)
            print(f"Celsius: {celsius}")
    
        else:
            print("ERROR")
            
except ValueError or SyntaxError:
    print("ERROR")