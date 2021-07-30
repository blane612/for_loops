# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$
#    $$$
#     $$
#      $
#
#   >> symbol... %
#   >> size... 6
#
#   %%%%%% | i = 6 | number of symbols = 6 = i | number of spaces = 0 = (size - i) = 6 - 6
#    %%%%% | i = 5 | number of symbols = 6 = i | number of spaces = 1 = (size - i) = 6 - 5
#     %%%% | i = 4 | number of symbols = 6 = i | number of spaces = 2 = (size - i) = 6 - 4
#      %%% | i = 3 | number of symbols = 6 = i | number of spaces = 3 = (size - i) = 6 - 3
#       %% | i = 2 | number of symbols = 6 = i | number of spaces = 4 = (size - i) = 6 - 2
#        % | i = 1 | number of symbols = 6 = i | number of spaces = 5 = (size - i) = 6 - 1
#
# 
#
# Write Code Below #
s = input('Enter a symbol: ')
size = int(input('Enter a number: '))
for i in range(size, 0, -1):
  print(" " * (size - i) + s * i )
print()

# range(10) --> sequence
#   --> returns the sequence [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(5)
#   --> returns the sequence [0, 1, 2, 3, 4]
# range(7)
#   --> returns the sequence [0, 1, 2, 3, 4, 5, 6]

# range(start, stop)
# range(start, stop, step)

# range(3, 7)
#   --> returns the sequence [3, 4, 5, 6]
# range(2, 8)
#   --> returns the sequence [2, 3, 4, 5, 6, 7]

# range(10, 0, -1)
#   --> returns the sequence [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# range(8, 4, -1)
#   --> returns the sequence [8, 7, 6, 5]

# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
input('Enter a symbol: ')



# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #


# ---------- Part 2 | Mathematical Patterns ---------- #
print(
    '>> Section 2\n'
    '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #


# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #