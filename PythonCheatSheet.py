# ===============================
# 1. IMPORTS (like Java import)
# ===============================
import math
import random

# ===============================
# 2. INPUT / OUTPUT
# ===============================
name = input("Enter your name: ")      # always returns string
age = int(input("Enter age: "))        # type casting

print("Hello", name)
print(f"Age is {age}")                 # f-string (VERY IMPORTANT)

# ===============================
# 3. VARIABLES (no types)
# ===============================
x = 10
y = 2.5
flag = True

# ===============================
# 4. CONDITIONS
# ===============================
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Smaller")

# ===============================
# 5. LOOPS
# ===============================
for i in range(5):              # 0 to 4
    print(i)

for i in range(1, 10, 2):       # start, end, step
    print(i)

while x > 0:
    x -= 1

# ===============================
# 6. FUNCTIONS
# ===============================
def add(a, b):
    return a + b

def greet(name="User"):         # default argument
    print("Hello", name)

print(add(3, 4))
greet()
greet("Tanvi")

# ===============================
# 7. LIST (MOST USED IN AI)
# ===============================
arr = [1, 2, 3, 4]

arr.append(5)
arr.insert(1, 10)
arr.remove(3)
arr.pop()
arr.sort()
arr.reverse()

print(arr)
print(len(arr))
print(arr[0])
print(arr[-1])                  # last element

# List comprehension (VERY IMPORTANT)
squares = [x*x for x in range(5)]
print(squares)

# ===============================
# 8. TUPLE (IMMUTABLE LIST)
# ===============================
t = (1, 2, 3)
print(t[0])

# ===============================
# 9. SET (UNIQUE ELEMENTS)
# ===============================
s = {1, 2, 3}
s.add(4)
s.remove(2)

print(s)

# ===============================
# 10. DICTIONARY (KEY-VALUE)
# ===============================
mp = {"a": 1, "b": 2}

mp["c"] = 3
mp["a"] = 10

print(mp["a"])
print(mp.keys())
print(mp.values())
print(mp.items())

for key, value in mp.items():
    print(key, value)

# ===============================
# 11. STRING METHODS (SUPER IMPORTANT)
# ===============================
text = "  Hello Python  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "AI"))
print(text.split())

# ===============================
# 12. EXCEPTION HANDLING
# ===============================
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Done")

# ===============================
# 13. FILE HANDLING (BASIC)
# ===============================
with open("data.txt", "w") as f:
    f.write("Hello AI")

with open("data.txt", "r") as f:
    print(f.read())

# ===============================
# 14. CLASS (JAVA-LIKE)
# ===============================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Tanvi", 22)
s1.display()

# Check existence
if 5 in arr:
    print("Found")

# Length
len(arr)

# Type check
type(arr)

# Multiple assignment
a, b = 10, 20

# Swap (no temp variable)
a, b = b, a
