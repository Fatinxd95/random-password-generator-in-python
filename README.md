🔐 Random Password Generator (CLI)

A simple command-line password generator written in Python. The program
asks the user for a desired password length and generates a random
password using letters, numbers, and selected symbols.

📌 Features

-   Generates random passwords
-   User-defined password length
-   Uses:
    -   Lowercase letters (a-z)
    -   Uppercase letters (A-Z)
    -   Numbers (0-9)
    -   Symbols (. , # *)
-   Simple command-line interface
-   Basic input validation

🧠 How It Works

1.  The program prompts the user to enter the desired password length.
2.  A list of characters (letters, numbers, symbols) is defined.
3.  The list is shuffled repeatedly to increase randomness.
4.  A random character is selected each iteration until the password
    length is reached.
5.  The final password is printed to the terminal.

📂 Project Structure

password-generator/ │ ├── password_generator.py └── README.md

▶️ Running the Program

1. Clone the repository

git clone https://github.com/Fatinxd95/random-password-generator-in-python.git cd
password-generator

2. Run the script

python password_generator.py

3. Example

How long should the password be? 12 fA9#pQ2mB7*z

⚙️ Requirements

-   Python 3.x

No external libraries are required. The program only uses built-in
modules:

-   random

⚠️ Error Handling

If the user enters a value that is not an integer, the program will
display:

Must be an integer

🚀 Future Improvements

Possible upgrades:

-   Add more symbols
-   Add options for:
    -   numbers only
    -   symbols only
    -   letters only
-   Allow saving passwords to a file
-   Add strength validation
-   Convert to a GUI app

📜 License

This project is open source and available under the MIT License.
