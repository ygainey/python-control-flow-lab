import random

# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    letter = input('please input a letter A-Z or a-z').lower().strip()
    if letter in 'aeiou':
        print(f'The letter {letter} is a vowel')
    else:
        print(f'The letter {letter} is a consonant')

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    VOTING_AGE = 18
    age = int(input('Please input you age: '))

    if age < 1:
        print('You cannot be 0 Years old or have a negative age')
    elif age >= 18:
        print('You can vote')
    elif age < 18:
        print('You cannot vote')  

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = int(input('Please enter you dogs age: '))

    if dog_age <=2:
        print(f'Your dog is {dog_age * 10} years old')
    elif dog_age > 2:
        x = dog_age - 2
        dog_age = (x * 7) + 20
        print(f'Your dog is {dog_age} years old')


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    cold = input('Is it cold: (yes/no)').strip()
    raining = input('Is it raning: (yes/no)').strip()

    if cold == 'yes' and raining == 'yes':
        print('Wear a waterproof coat.')
    elif cold == 'yes' and raining == 'no':
        print('Wear a warm coat')
    elif cold == 'no' and raining == 'yes':
        print('Carry an umbrella.')    
    elif cold == 'no' and raining == 'no':
        print('Wear light clothing.')


# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')

    month = input('Enter the month of the year (Jan - Dec): ').lower().strip()
    day = int(input('Enter the day of the Month: '))
    if month in months:
        if (month == 'dec' and day >= 21) or (month == 'mar' and day <= 19) or (month =='jan' or month == 'feb'):
            print(f'{month}, {day} is in Winter')
        elif (month == 'mar' and day >= 20) or (month == 'jun' and day <= 20) or (month =='apr' or month == 'may'):
            print(f'{month}, {day} is in Spring')
        elif (month == 'jun' and day >= 21) or (month == 'sep' and day <= 21) or (month =='jul' or month == 'aug'):
            print(f'{month}, {day} is in Summer')
        elif (month == 'sep' and day >= 22) or (month == 'dec' and day <= 20) or (month =='oct' or month == 'nov'):
            print(f'{month}, {day} is in Fall') 
    else:
        print('please input a correct month, using the first 3 letters') 

# Call the function
determine_season()


# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    randon_number = random.randrange(1, 100)

    print("Guess the number between 1 and 100. You have 5 attempts.")
    
    for attempt in range(1, 6):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == randon_number:
            print("Congratulations, you guessed correctly!")
            break
        elif guess < randon_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        if attempt == 4:
            print("Last chance!")

        if attempt == 5:
            print("Sorry, you failed to guess the number in five attempts.")
            print(f"The correct number was {randon_number}.")
            break  


        

# Call the function
guess_number()
