
"""
CP1404/CP5632 - Practical

Broken program to determine score status

"""
# TODO: Fix this!
score = float(input("Enter score: "))
if score < 0 or score > 100: #if score is below 0 or above 100
    print("Invalid score")
elif score >= 90:   #if score is 90 or above
    print("Excellent")
elif score >= 50:   #if score is 50 or above
    print("Passable")
else:              #if score is below 50
    print("Bad")
