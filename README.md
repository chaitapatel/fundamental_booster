# Personal Data Collector

This project contains a simple interactive Python script that collects personal information from the user and prints it back along with data types and memory addresses.

## Description

The script:

- Welcomes the user.
- Prompts for `name`, `age`, `height` in meters, and `favourite number`.
- Displays the collected information with Python type and memory address.
- Calculates and displays an approximate birth year based on the current year.
- Thanks the user and ends.

## Code

```python
from datetime import datetime

print("Welcome to the Interactive Personal Data Collector!")

# Taking input
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_num = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {fav_num} (Type: {type(fav_num)}, Memory Address: {id(fav_num)})")

# Calculate birth year
current_year = datetime.now().year
birth_year = current_year - age

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

print("\nThank you for using the Personal Data Collector.")
print("Goodbye! Keep exploring Python!")
```

## Usage

Run the script in a Python environment and follow the prompts:

```bash
python ak.ipynb  # convert notebook to script first or run the equivalent Python script
```

> Note: This repository contains a Jupyter notebook (`ak.ipynb`). If you want to run the code directly, convert it to a `.py` script or copy the code into a Python file.
