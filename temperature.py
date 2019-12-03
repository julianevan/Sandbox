
"""

CP1404/CP5632 - Practical

Pseudocode for temperature conversion

"""

def calculate_celsius():
    celsius = float(input("Celsius: "))  # float so as to allow decimal input
    fahrenheit = celsius * 9.0 / 5 + 32  # formula for celsius to fahrenheit conversion
    print("Result: {:.2f} F".format(fahrenheit))  # displays fahrenheit, rounded to two decimal places.
def calculate_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))  # float so as to allow decimal input
    celsius = (5 / 9) * (fahrenheit - 32)  # formula for fahrenheit to celsius conversion
    print("Result: {:.2f} F".format(celsius))  # displays celsius, rounded to two decimal places

MENU = """C - Convert Celsius to Fahrenheit

F - Convert Fahrenheit to Celsius

Q - Quit"""

print(MENU)

choice = input(">>> ").upper() #to make the inputted text in upper case

while choice != "Q": #the program will loop until the user enters q
    if choice == "C": #if user enters c
        calculate_celsius()
    elif choice == "F": #if choice is F
        calculate_fahrenheit()
    else: #if choice is not C,F or Q.
        print("Invalid option")
        print(MENU)
    choice = input(">>> ").upper()
print("Thank you.") #if user inputs Q