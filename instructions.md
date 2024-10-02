## Python: If-Else Statements (Practice)

### Getting Started

- Create a GitHub repo named: **python-if-else-starter**
    - Upload your project files to the repo
    - **No need to share your repo with your teacher**
    - **Teacher will discuss your work with you during Teacher  Time**

- Also create a NEW project folder on your workstation desktop
- Use VS Code to save your work (temporarily) to your workstation folder


### Comment Block

```python
# Abraham Lincoln
# 20 SEP 20XX
# If-Else Statements 
```

### Coding Tasks

- Use comments to label each task in your script
  - Example: # Task 1, # Task 2, etc.
- Use f-strings to display the output for each task

#### Task 1

- Read **if-else Statements**, pp. 79 - 80 in the yellow PCC (*Python Crash Course*) book

#### Task 2

- Complete Exercise 5-4, **TRY IT YOURSELF**, p. 84 in PCC

#### Task 3

- Prompt the user to enter their first name
- Use the Python [`len()`](https://www.w3schools.com/python/ref_func_len.asp) function and an if statement to determine if the number of characters in the name is less than or equal to 5
- If the condition evaluates to True, tell the user their name is too short
- Otherwise, tell the user s/he has a long name

#### Task 4

- Start by creating a Python list of vowels, like so:

```python
# A Python list needs a name, usually in plural form
# Rules for naming lists are the same as the rules for naming variables
# Use a pair of square brackets to mark the beginning and end of your Python list
vowels = ['a', 'e', 'i', 'o', 'u']
```

- Prompt the user to enter a letter of the alphabet
- Apply the `lower()` string method to the prompt (from Step 1 above)

```python
# The lower ( ) method converts the user's input to all lowercase characters
letter = input('Please enter a letter of the alphabet:\n').lower()
```
- [Using the `in` membership operator (see Method 3 in the example)](https://www.tutorialspoint.com/how-does-in-operator-work-on-list-in-python), write an if-else statement that checks whether the letter the user entered is a vowel 
- If the letter IS a vowel, tell the user that the letter is indeed a vowel
- Otherwise, tell the user the letter they entered is a consonant

#### Task 5

- Prompt the user to enter two (2) **integers**
- What function tells Python to treat user input as an integer?
- Using the modulus operator (%), write an if statement that checks to see if the first integer divided by the second integer has a remainder of zero (0)
- If the condition evaluates to `True`, print a message that says that the first number is divisible by the second number
- Otherwise, print a message informing the user that the first number is NOT divisible by the second number
