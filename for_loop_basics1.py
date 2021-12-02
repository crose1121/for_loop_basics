# Create a Python file called for_loop_basic1.py that performs the following tasks.

# Basic - Print all integers from 0 to 150.

for n in range(0,151):
    print(n)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for n in range(5,1001):
    if n%5 == 0:
        print(n)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for n in range(1,101):
    if n%10 == 0:
        print("Coding Dojo")
    elif n%5 == 0:
        print("Coding")
    else:
        print(n)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for n in range(0,500001):
    if n%2 != 0:
        sum +=n
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for n in range(2018,1,-4):
    print(n)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

low_num = 7
high_num = 121
mult = 15

for n in range(low_num, high_num):
    if n%15 == 0:
        print(n)


x = [5,34,10,1,6]
x.append(2)
print(x)