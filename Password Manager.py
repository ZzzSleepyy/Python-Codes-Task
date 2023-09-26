
# NOT SECURED YET


dictionaries = []

while True:
    
    dictionary = {"Name": "", "Password": "", }
    
    x = input("Enter a name: ")
    y = input("Enter your password: ")
    
    dictionary["Name"] = x
    dictionary["Password"] = y
    
    dictionaries.append(dictionary)
    
    print(dictionary)
    
    for i, dictionary in enumerate(dictionaries):
        print(f"{i + 1}. {dictionary}")
