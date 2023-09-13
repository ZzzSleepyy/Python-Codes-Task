while True:
    user_input = input("Enter a list of numbers separated by spaces (e.g., 1 2 3): ")
    numbers = [int(x) for x in user_input.split()]

    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
            
        print("Even numbers:", even)
        print("Odd numbers:", odd)