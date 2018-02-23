# 1. The CSS drawing problem is found in wk03challenges.html

# 2. Find the Pythagorean triplet such that a + b + c = 1000. Return the product abc.

for a in range(1, 1001):
    for b in range(a+1, 1001):
        for c in range(b+1, 1001):
            if a + c + c == 1000 and a**2 + b**2 == c**2:
                # return (a, b, c)
                return a * b * c

# 3. Find the single different character between two strings
str1 = 'abcd'
str2 = 'abcde'
for letter in str2:
    if (str.1count(letter) != str2.count(letter)):
        difference = letter
        print(letter)

# another solution
# load both sets of characters into list (how about a set???), loop through to find the single entry that is different