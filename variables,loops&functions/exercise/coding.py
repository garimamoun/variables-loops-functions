# Function to calculate square of a number
def calculate_square(num):
    return num * num


# Variable (list of numbers)
numbers = [1, 2, 3, 4, 5]

print("🔢 Number and their Squares:")

# Loop through the list
for n in numbers:
    result = calculate_square(n)
    print(f"{n} -->{result}")
