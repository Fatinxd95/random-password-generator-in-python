import random

# List of alphanumeric characters
characters = [

    # Lowercase characters
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    # Uppercase characters
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    # Numeric characters
    "0","1","2","3","4","5","6","7","8","9",".",",","#","*"
]


try:

    # Trys to convert the string into an integer unless it has one or more non-digits
    length = int(input("How long should the password be? "))

    # For i in range of the integer value of arguement vectors 1st index 
    for i in range(length):

        # Shuffles the list of characters on each iteration
        random.shuffle(characters)

        # Prints the random element from the list and 
        print(characters[random.randint(1, len(characters) - 1)], end="")

    print()

except ValueError:
    print("Must be an integer")
    pass
