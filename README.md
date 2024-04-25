# skills_challenges
# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

import datetime 

def validate_age(20020119):
    """Parameters: string representing date
    datetime.strptime(date, `YYYY-MM-DD => '%Y-%m-%d')
    current_date = datetime.now() 
    age = current_date  - date

from dateutil.relativedelta import relativedelta
import datetime
birthdate = "22-01-1995"
birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y').date()
today = datetime.date.today()
age = relativedelta(today, birthdate).years
print("your age is",age,"years.")

 denied entry
 granted access
 wrong format
 wrong data type (e.g. int) 20020119

 type (str) or format 1993-01-19


 if type(birth_date) != str:
    raise Exception("")

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

```
birth_date = '1993-01-19'  => granted access
birth_date = '2020-01-19'  => denied entry


birth_date = '2008-04-26' => "You are 15 years old. The required age is 16"
birth_date = '2008-04-25' => granted access 

birth_date = 20080425 => throws error (wrong data type)
birth_date = 26-04-2008 => throws error (wrong format)
```

try:
    # your code here
except (ValueError, TypeError) as e:
    # catch it, the exception is accessable via the variable e

# handler_statement.py

try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    print(f"{first} divided by {second} is {first / second}")
except ValueError:
    print("You must enter a number")
except ZeroDivisionError:
    print("You can't divide by zero")