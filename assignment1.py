import time, math
import os

#Coding of prime number sum
def Prime_digits(numbers):
    if numbers < 2: 
        return False
    for i in range(2, int(math.sqrt(numbers)) + 1):
        if numbers % i == 0: 
            return False
    return True


def sum_of_primes(initial, last):
    prime_sum = 0
    for digits in range(initial, last + 1):
        if Prime_digits(digits):
            prime_sum += digits
    return prime_sum

#Covertng length coding

def convert_units(num1, direction1):
    if direction1== "M":
        print(f"{num1} meters is = {round(num1 * 3.28084, 2)} feet.")
    elif direction1 == "F":
        print(f"{num1} feet is = {round(num1 / 3.28084, 2)} meters")
    else:
        print("Direction Error404!, Please use M for meters or F for feet")

#consonant counter
def counting_consonant_of_word(Text):
    v = 'AEIOUaeiou'
    counting_consonant = 0
    for i in Text:
        if i.isalpha() and i not in v:
            counting_consonant = counting_consonant + 1
    return counting_consonant

#Finding leastest and greatest of number
def minimum_maximum(number3):
    greatest = least = number3[0]

    for num in number3:
        if num> greatest:
            greatest = num
        elif num< least:
            least = num
    return least,greatest 

#palindrome 
def palindrome(r):
   
    r = r.replace(" ", "").lower()
    if r == r[::-1]:
        return True
    else:
        return False

#word counter
def word_counter():
    filename = input("Enter the file path: ")
    if not os.path.isfile(filename):
        print("Invalid file path.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().lower()
        counts = {word: content.split().count(word) for word in ["the", "was", "and"]}
        print("Word counts:", counts)
    except Exception as e:
        print(f"Error reading file: {e}")

#menu coding
main_menu_option = ('1','2','3','4','5','6','0')


while True:
    print()
    print(">_<     Menu     >_<", "\n[1] Calculating Sum of Prime Numbers", "\n[2] Converting Units of Length", "\n[3] Counting Consonants", "\n[4] Finding Min/Max of Numbers", "\n[5] Checking Palindrome", "\n[6] Word Counter", "\n[0] Exiting Program")
    
    print()
    User_input = input("Select One of the Options")

    if User_input in main_menu_option:
        break

    else:
        print()
        print("Invalid! Currently this option is not available")
    
if User_input == '1':
    print('Processing.....')
    time.sleep(3)
    initial, last = int(input("Enter your starting range ->")), int(input("Enter your Ending range ->"))
    print('on the way....')
    time.sleep(2)
    print("Sum of Prime numbers:", sum_of_primes(initial, last))
    print()
    
elif User_input == "2":
    print("Processing......")
    time.sleep(2)
    Value1 = float(input("Enter Value: "))
    direction2 = input("Convert from 'M' to feet or 'F' to Meters: ").upper()
    print("almost there....")
    time.sleep(2)
    convert_units(Value1, direction2)

elif User_input == "3": 
    print("Processing......")
    time.sleep(2)
    input_word = input("Please enter your word: ")
    consonants = counting_consonant_of_word(input_word)
    print("almost there....")
    time.sleep(2)
    print(f"Total Number of consonants is: {consonants}")

elif User_input == "4":
    print("Processing......")
    time.sleep(2)
    numbers = list(map(int, input("Enter numbers but separate it with space not comma: ").split()))
    smallest, largest = minimum_maximum(numbers)
    print("almost there....")
    time.sleep(2)
    print(f"Smallest number= {smallest}, Largest number = {largest}")

elif User_input == "5": 
    print("Processing......")
    time.sleep(2)
    r = input("Enter the text string: ")
    if palindrome(r):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

elif User_input == "6":
    word_counter()

elif User_input == "0":
    print("Thank you for using it, goodbye")