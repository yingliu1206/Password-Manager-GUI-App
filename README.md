# Password-Manager-GUI-App
The Password Manager is a secure application designed to store passwords locally in JSON format. It generates complex passwords, copies them to the clipboard for user convenience, allows users to search existing passwords, and includes automatic checks for empty fields and duplicates.

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
* Search Function: Allows you to search existing passwords saved in the JSON file.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Password-Manager-GUI-App.git
   cd Password-Manager-GUI-App

2. **Running the Application**:
   ```bash
   python main.py

### Interface
![application interface.png](application%20interface.png)

## Instructions
* Generate Password: Click the "Generate Password" button to create a new password.
* Save Password: Fill in the website and email (defaulted), then click "Add" to save your password.
* Copy Password: The generated password will be automatically copied to your clipboard.
* Search Password: Enter the website and click the "Search" button. If there is an existing password associated with the website, it will pop up in a new window. If not, you will be notified.

## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
