import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_sum(start, end):
    """Calculate the sum of all prime numbers in the given range [start, end]."""
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

def length_unit_converter(value, direction):
    """Convert length units between meters and feet."""
    if direction == 'M':
        # Convert meters to feet
        return round(value * 3.28084, 2)
    elif direction == 'F':
        # Convert feet to meters
        return round(value / 3.28084, 2)
    else:
        return "Invalid direction. Please use 'M' or 'F'."

def consonant_counter(text):
    """Count the number of consonants in a given string (case-insensitive)."""
    vowels = "aeiouAEIOU"
    consonants = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonants += 1
    return consonants

def min_max_finder(numbers):
    """Find the smallest and largest numbers from a list of numbers."""
    if not numbers:
        return "No numbers provided."
    smallest = min(numbers)
    largest = max(numbers)
    return f"Smallest: {smallest}, Largest: {largest}"

def palindrome_checker(text):
    """Check if a string is a palindrome, ignoring spaces and case."""
    text = ''.join(text.split()).lower()
    return text == text[::-1]

def word_counter(filename):
    """Count the occurrence of specific words in a text file."""
    words_to_count = ["the", "was", "and"]
    word_count = {word: 0 for word in words_to_count}
    
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            for word in words_to_count:
                word_count[word] = text.count(word)
    except FileNotFoundError:
        return "File not found."
    
    return word_count


def display_menu():
    """Display the program's main menu."""
    print("\nPlease select an option:")
    print("1. Prime number sum calculator")
    print("2. Length unit converter")
    print("3. Consonant counter")
    print("4. Min-Max number finder")
    print("5. Palindrome checker")
    print("6. Word counter (from a text file)")
    print("7. Exit")

def main():
    """Main program loop to run the menu and handle user input."""
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                print(f"Sum of prime numbers: {prime_number_sum(start, end)}")
            except ValueError:
                print("Invalid input! Please enter integers for the range.")
        
        elif choice == 2:
            try:
                value = float(input("Enter the value to convert: "))
                direction = input("Enter the direction (M for meters to feet, F for feet to meters): ").upper()
                print(f"Converted value: {length_unit_converter(value, direction)}")
            except ValueError:
                print("Invalid input! Please enter a valid number for the value.")
        
        elif choice == 3:
            text = input("Enter a string: ")
            print(f"Number of consonants: {consonant_counter(text)}")
        
        elif choice == 4:
            try:
                num_count = int(input("How many numbers do you want to enter? "))
                numbers = []
                for _ in range(num_count):
                    number = float(input("Enter a number: "))
                    numbers.append(number)
                print(min_max_finder(numbers))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        elif choice == 5:
            text = input("Enter a string: ")
            print(f"Is the string a palindrome? {palindrome_checker(text)}")
        
        elif choice == 6:
            filename = input("Enter the filename (e.g., 'sample.txt'): ")
            word_counts = word_counter(filename)
            print(f"Word counts: {word_counts}")
        
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please choose a number between 1 and 7.")
        
        cont = input("Would you like to perform another calculation? (y/n): ").lower()
        if cont != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
