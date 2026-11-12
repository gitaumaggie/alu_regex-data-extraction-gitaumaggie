Regex Data Validator
A Python-Based Data Validation Application Using Regular Expressions
1. Project Overview
Regex Data Validator is a Python-based application developed to demonstrate the practical application of Regular Expressions (Regex) in validating structured data.
The application enables users to validate different types of input through an interactive web interface built with Streamlit. Users select a validation category, provide an input value and receive immediate feedback indicating whether the submitted data follows the expected format.
The project combines Python's built-in re module with Streamlit to demonstrate how pattern matching can be integrated into a functional web application.
Rather than relying on manual inspection, the application uses predefined regular expression patterns to identify valid and invalid input formats.
2. Project Objectives
The primary objectives of this project are to:
Understand and apply regular expressions in practical data validation scenarios.
Develop regex patterns capable of identifying specific data formats.
Implement reusable Python functions for validating different types of data.
Integrate validation logic into an interactive web application.
Apply software engineering principles such as modularity, code reusability and separation of concerns.
Implement automated testing to evaluate the accuracy and reliability of validation functions.
Demonstrate how regular expressions can be used to improve input validation in software applications.
3. Supported Validation Categories
The application supports eight validation categories.
No.
Validation Category
Description
1
Email Address
Checks whether an email address follows the expected email format.
2
URL
Validates URLs beginning with HTTP or HTTPS.
3
Phone Number
Checks phone numbers against supported formatting conventions.
4
Credit Card Number
Validates 16-digit numbers separated consistently by spaces or hyphens.
5
Time
Supports both 12-hour and 24-hour time formats.
6
HTML Tag
Checks simple HTML tag structures.
7
Hashtag
Validates hashtags beginning with # and containing letters, numbers or underscores.
8
Currency Amount
Validates US dollar amounts with exactly two decimal places and optional comma-based thousands separators.

3.1 Email Address Validation
The email validator checks whether an input follows an expected email address structure.
Examples:
Valid inputs:
user@example.com
john.doe@gmail.com
user+tag@example.co.ke
123456@gmail.com
Invalid inputs:
invalid-email
.user@example.com
user..name@example.com
user@-example.com
user@example
The pattern supports common email address structures while rejecting several malformed formats.
3.2 URL Validation
The URL validator checks whether a submitted URL begins with an HTTP or HTTPS protocol and follows the expected domain structure.
Valid inputs:
https://www.example.com
http://example.org
https://subdomain.example.com/page
Invalid inputs:
www.example.com
example.com
ftp://example.com
3.3 Phone Number Validation
The phone number validator supports three specific phone number formats.
Valid inputs:
(123) 456-7890
123-456-7890
123.456.7890
Invalid inputs:
1234567890
(123)456-7890
123-45-6789
3.4 Credit Card Number Validation
The credit card validator checks for a 16-digit number separated consistently by either spaces or hyphens.
Valid inputs:
1234 5678 9012 3456
1234-5678-9012-3456
Invalid inputs:
1234567890123456
1234-5678 9012-3456
1234-5678-9012
3.5 Time Validation
The time validator supports both standard time representations.
12-hour format:
Requires an AM or PM indicator.
Examples:
02:30 PM
11:45 AM
12:00 PM
24-hour format:
Uses hours ranging from 00 to 23 without an AM or PM indicator.
Examples:
14:30
09:15
23:59
Invalid inputs:
25:30
13:22 PM
12:75 PM
01:22 AMM
3.6 HTML Tag Validation
The HTML tag validator checks simple HTML tag structures.
Valid inputs:
<p>
<div class="example">
<img src="image.jpg" alt="description">
Invalid inputs:
p
<123>
<div
<>
3.7 Hashtag Validation
The hashtag validator checks whether an input begins with #, followed by letters, numbers or underscores.
Valid inputs:
#technology
#SoftwareEngineering
#Tech2026
#African_Developers
Invalid inputs:
technology
#
#hello world
##technology
3.8 Currency Amount Validation
The currency validator checks US dollar amounts containing exactly two decimal places.
The application displays the dollar sign separately, allowing users to enter the numerical amount without typing $. The application automatically attaches the symbol before passing the value to the validator.
Valid inputs:
19.99
1234.56
1,234.56
12,345.67
Invalid inputs:
19.9
1234
1,23.45
12.345
4. Application Features
The application provides the following features:
Multiple validation categories: Supports eight different types of data validation.
Interactive interface: Users can select a validation category through a dropdown menu.
Real-time interaction: Users can submit values and receive validation feedback.
Input guidance: Each validation category provides instructions and examples.
Success notifications: Displays confirmation when an input follows the expected format.
Error notifications: Identifies invalid inputs and provides an example of the expected format.
Currency input enhancement: Displays the dollar symbol separately and automatically includes it during validation.
Modular implementation: Separates validation logic from the web interface.
Automated testing: Uses pytest to test validation functions.
5. Technologies and Tools
Technology
Purpose
Python 3
Main programming language
Regular Expressions (re)
Pattern matching and input validation
Streamlit
Interactive web application framework
Pytest
Automated testing
Git
Version control
GitHub
Source code hosting and collaboration
Linux
Development environment

6. Project Architecture
The application follows a modular structure that separates validation logic, user interaction and automated testing.
Project Directory Structure
alu_regex-data-extraction-gitaumaggie/
│
├── app.py
│
├── validators.py
│
├── requirements.txt
│
├── README.md
│
├── tests/
│   └── test_validators.py
│
└── .gitignore
6.1 app.py
This is the main application file.
It is responsible for:
Configuring the Streamlit application.
Displaying the application interface.
Providing validation category selections.
Collecting user input.
Connecting user selections to the appropriate validation functions.
Displaying validation results and feedback.
6.2 validators.py
This module contains the regular expression patterns and corresponding Python validation functions.
Each validation function receives an input value, evaluates it against its corresponding regex pattern and returns a Boolean result.
True indicates that the input matches the expected pattern.
False indicates that the input does not match the expected pattern.
The module uses Python's built-in re library and re.fullmatch() to ensure that the entire input is checked against the specified pattern.
6.3 tests/test_validators.py
This directory contains automated tests for the validation functions.
The tests use assertions to verify that:
Valid inputs return True.
Invalid inputs return False.
Pytest is used to discover and execute the test functions.
6.4 requirements.txt
This file specifies the external Python dependencies required by the application.
It allows developers and deployment platforms to install the necessary packages using pip.
7. How the Application Works
The application follows a straightforward validation process:
The user opens the application.
The user selects one of the eight validation categories.
The application displays instructions and an example of the expected format.
The user enters the value they want to validate.
The user clicks the Validate button.
The application identifies the corresponding validation function.
The input is passed to the selected function.
The regular expression evaluates the input.
The function returns a Boolean result.
Streamlit displays a success or failure message.
Validation Workflow
        User opens application
                 |
                 v
       Select validation category
                 |
                 v
          Enter input value
                 |
                 v
          Click Validate
                 |
                 v
       Select validation function
                 |
                 v
        Execute regex pattern
                 |
                 v
       Evaluate matching result
                 |
           +-----+-----+
           |           |
           v           v
       Match found   No match
           |           |
           v           v
      Valid input   Invalid input
           |           |
           v           v
      Success      Error feedback
      message      and example
8. Installation and Setup
Follow the instructions below to run the application locally.
Prerequisites
Ensure that you have the following installed:
Python 3
Git
pip
A web browser
Step 1: Clone the repository
git clone https://github.com/gitaumaggie/alu_regex-data-extraction-gitaumaggie.git
Step 2: Navigate into the project directory
cd alu_regex-data-extraction-gitaumaggie
Step 3: Create a virtual environment
python3 -m venv venv
Step 4: Activate the virtual environment
For Linux and macOS:
source venv/bin/activate
Step 5: Install project dependencies
python -m pip install -r requirements.txt
Step 6: Run the application
streamlit run app.py
The application will be available locally at:
http://localhost:8501
Open the address in your web browser to access the application.
9. Testing
Automated testing is an important part of this project because regex patterns must correctly identify both valid and invalid inputs.
The project uses pytest to execute the test functions in tests/test_validators.py.
Run the tests
From the project's root directory, execute:
pytest -v
The -v option provides detailed output showing individual test results.
The tests cover all eight validation categories.
Testing Approach
Each validator is tested using:
Positive test cases: Inputs expected to be valid.
Negative test cases: Inputs expected to be invalid.
Edge cases: Inputs that test the boundaries and restrictions of the regex patterns.
The objective is to ensure that the validators behave consistently with their defined requirements.
10. Limitations and Considerations
Although the application validates input formats using regular expressions, it does not establish whether submitted information is genuine, registered or operational.
Some important limitations include:
Email addresses: The validator checks email structure but does not verify whether the mailbox exists or can receive messages.
URLs: The validator checks URL formatting but does not confirm whether the website is accessible.
Phone numbers: The validator checks supported formats but does not establish whether a number is registered or active.
Credit card numbers: The validator checks the expected digit grouping and separator consistency. It does not verify card authenticity, issuer information or the Luhn checksum.
Time: The validator checks the specified time formats but does not interpret time zones.
HTML tags: The validator checks simple tag-shaped strings and does not perform complete HTML parsing or structural validation.
Hashtags: The validator checks the supported hashtag format but does not determine whether a hashtag exists on a social media platform.
Currency amounts: The validator checks US dollar formatting and does not perform currency conversion or financial verification.
These limitations demonstrate the distinction between format validation and deeper verification.
11. Future Improvements
Potential enhancements include:
Expanding email validation to support additional standards and edge cases.
Supporting international phone number formats.
Adding additional URL validation rules.
Implementing Luhn checksum verification for credit card numbers.
Supporting additional currencies.
Improving the visual design and accessibility of the interface.
Adding input history and validation summaries.
Expanding automated tests to cover more edge cases.
Deploying the application to a publicly accessible hosting platform.
12. Learning Outcomes
Through this project, the following practical software engineering concepts are explored:
Writing and interpreting regular expressions.
Using Python's re module for pattern matching.
Designing reusable validation functions.
Working with Boolean expressions and conditional statements.
Building interactive applications using Streamlit.
Organizing Python projects into separate modules.
Writing automated tests using pytest.
Using Git and GitHub for source code management.
Understanding the importance of edge-case testing and input validation.
13. Author
Margaret Gitau
Software Engineering Student
Africa Leadership College of Higher Education (ALCHE)
GitHub: @gitaumaggie

Developed as part of the Regex Data Extraction onboarding hackathon.


