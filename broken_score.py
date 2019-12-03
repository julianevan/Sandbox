
"""
CP1404/CP5632 - Practical

Broken program to determine score status

"""
def determine_result(score):
    if score < 0 or score > 100:  # if score is below 0 or above 100
        return ("Invalid Score")
    elif score >= 90:  # if score is 90 or above
        return ("Excellent")
    elif score >= 50:  # if score is 50 or above
        return ("Passable")
    else:  # if score is below 50
        return ("Bad")

# TODO: Fix this!
score = float(input("Enter score: "))
print(determine_result(score))
