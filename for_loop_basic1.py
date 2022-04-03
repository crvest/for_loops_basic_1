# Basics
for x in range(151):
    print(x)

# Multiples of 5
for x in range(5,1001,5):
    print(x)

# Counting, the Dojo Way
for x in range(1, 101):
    if x % 5 == 0 and x % 10 != 0:
        print("Coding")
    elif x % 10 == 0:
        print("Coding Dojo")
    else:
        print(x)

# Whoa. That Sucker's Huge
sum = 0
for x in range(500001):
    if x % 2 != 0:
        sum += x

print("The final sum is:", sum)

# Countdown by Fours
for x in range(2018, 0, -4):
    print(x)

# Flexible Counter
lowNum = int(input(" Enter lower bound: ")) # accepts input from terminal and changes the type from string to int before passing to range function
highNum = int(input("Enter upper bound: "))
mult = int(input("Enter multiple: "))
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)