# Function to check age
def check_age():
    try:
        age = int(input("Please enter your age: "))
        if 10 <= age <= 20:
            print("Your age is between 10 and 20 years.")
        else:
            print("Your age is not between 10 and 20 years.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Call the function
check_age()

        