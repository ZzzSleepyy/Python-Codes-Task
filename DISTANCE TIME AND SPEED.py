#CALCULATE DISTANCE TIME TO SPEED
distance = int(input("Distance(meters): "))
time = int(input("Time(seconds): "))

calculate = float(distance / time)

print(f"Speed: {calculate} mph")

#UPDATED

#CALCULATE DISTANCE TIME AND SPEED
import os
os.system("cls")

def indent():
    os.system("cls")


while True:
    try:
        print("1. Time\n2. Speed\n3. Distance")
        input_choices = input("Choose(1/2/3): ")

        choices =  ["1","2","3"]
        
        if input_choices == choices[0]:
            
            indent()
            
            distance = int(input("Distance(meters): "))
            time = int(input("Time(seconds): "))

            calculate = float(distance / time)

            print(f"Speed: {calculate} mph")
            

        elif input_choices == choices[1]:
            
            indent()
        
            speed = int(input("Speed(mph): "))
            time = int(input("Time(seconds): "))
        
            calculate = float(speed * time) 
        
            print(f"Distance: {calculate} meters")
        
        elif input_choices == choices[2]:
            
            indent()
        
            distance = int(input("Distance(meters): "))
            speed = int(input("Speed(mph): "))
        
            calculate = distance / speed
        
            print(f"Time: {calculate} seconds")
        
        else:
            print("Error")
    except ValueError:
        print("Error")
