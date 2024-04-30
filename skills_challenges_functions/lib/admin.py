
from dateutil.relativedelta import relativedelta
import datetime

def validate_age(dob):
    try:
        birthdate = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
        today = datetime.date.today()
        age = relativedelta(today, birthdate).years
        if age >= 16:
            return "Access granted"
        else:
            return f"Access denied. You are {age}. You must be at least 16 years old."
    except ValueError:
        raise ValueError("Wrong format. Please use YYYY-MM-DD format")
    except TypeError:
        raise TypeError("Wrong data type. Please enter a string using format YYYY-MM-DD")
   



