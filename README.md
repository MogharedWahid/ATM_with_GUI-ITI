# ATM Simulator

This Python project simulates a basic ATM machine using the tkinter library for the graphical user interface.

## Features

- **User Authentication:**
    - Prompts the user to enter their account ID.
    - Validates the entered ID.
    - Prompts the user to enter their password.
    - Validates the password and limits the number of attempts (locks the account after three failed attempts).

- **Main Menu:**
    - Provides the following options:
        - Cash Withdraw
        - Balance Inquiry
        - Password Change
        - Fawry Service (for mobile phone recharges)
    - Allows the user to exit the application.

- **Cash Withdraw:**
    - Allows the user to enter the withdrawal amount.
    - Validates the amount (must be a multiple of 100 and within the withdrawal limit).
    - Updates the account balance.
    - Simulates the ATM dispensing cash.

- **Balance Inquiry:**
    - Displays the current account balance.

- **Password Change:**
    - Allows the user to change their password.
    - Validates the new password (must be four digits and match the confirmation).

- **Fawry Service:**
    - Allows the user to select the mobile network operator (Vodafone, Etisalat, Orange, WE).
    - Prompts the user to enter the phone number and recharge amount.
    - Validates the phone number and ensures sufficient balance.
    - Deducts the recharge amount from the account balance.

## How to Run

1. Save the code as a Python file (e.g., `atm_simulator.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the command: `python atm_simulator.py`

## Note

- This is a basic simulation and does not include real-world features like transaction history, receipts, or integration with actual bank systems.
- The account data is currently hardcoded within the script. For a more realistic implementation, you would typically store this data in a database.

## Further Improvements

- Implement error handling and more robust input validation.
- Add features like transaction history, mini-statements, and account statements.
- Integrate with a database to store and manage account information.
- Enhance the GUI with a more modern and user-friendly design.
- Add security measures like two-factor authentication.
