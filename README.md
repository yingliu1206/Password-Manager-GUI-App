# Password-Manager-GUI-App
The Password Manager is a secure application designed to store passwords locally in the format "website | email | password". It features automatic checks for empty fields and duplicates, generates complex passwords, and copies them to the clipboard for user convenience.

## Overview

This program utilizes the Python modules Tkinter and Pyperclip to create a user-friendly graphical interface for managing passwords efficiently.

### Key Components
* Tkinter: The core library for building the GUI.
* Window: The main application window that hosts all components.
* Label: Displays prompts and messages to the user.
* Entry: Input fields for website, email, and password.
* Button: Interactive elements to generate passwords and save entries.

### Features
* Input Validation: Automatically checks for empty fields before saving.
* Duplicate Check: Ensures passwords for the same website are not duplicated.
* Password Generation: Generates complex passwords for enhanced security.
* Clipboard Functionality: Copies generated passwords to the clipboard automatically.
* Defaulted Email: Displays a default email on the front-end to streamline the input process.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Password-Manager-GUI-App.git
   cd Password-Manager-GUI-App

2. **Running the Application**:
   ```bash
   python main.py

### Interface
<img width="563" alt="Screenshot 2024-10-05 at 8 58 46 PM" src="https://github.com/user-attachments/assets/4d536078-788b-4da3-9011-1d2e99feb540">


## Instructions
* Generate Password: Click the "Generate Password" button to create a new password.
* Save Password: Fill in the website and email (defaulted), then click "Add" to save your password.
* Copy Password: The generated password will be automatically copied to your clipboard.

## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
