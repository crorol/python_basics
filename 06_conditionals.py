# 1. Ways to declare strings
# -----------------------------------------------------------------------------------------------
# Basic Structure
age = 21

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



# 2. Handling Multiple Conditions with elif
# -----------------------------------------------------------------------------------------------
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")



# 3. Nested if Statements
# -----------------------------------------------------------------------------------------------
user = "admin"
logged_in = True

if logged_in:
    if user == "admin"":
        print("Welcome to the admin page.")
    else:
        print("Welcome to the user page.")
else:
    print("Please log in.")



# 4. Combining Logical Operators (and, or, not)
# -----------------------------------------------------------------------------------------------
age = 25
has_id = True

if age >= 20 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")



# 5. Conditional Expression (Ternary Operator)
# -----------------------------------------------------------------------------------------------
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)



# 6. truthy & Falsy Values
# -----------------------------------------------------------------------------------------------
if "":
    print("Won't run")   # Empty string -> False
if "text":
    print("Will run")    # Non-empty string -> True
if 0:
    print("Won't run")   # Number 0 -> False
if -1:
    print("Will run")    # Any non-zero number -> True

'''
    In Python, 




# 5. Conditional Expression (Ternary Operator)
# -----------------------------------------------------------------------------------------------




# 5. Conditional Expression (Ternary Operator)
# -----------------------------------------------------------------------------------------------




# 5. Conditional Expression (Ternary Operator)
# -----------------------------------------------------------------------------------------------




# 5. Conditional Expression (Ternary Operator)
# -----------------------------------------------------------------------------------------------










    
