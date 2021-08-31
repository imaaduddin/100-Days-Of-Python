# For loops with lists 
fruits = ["apple", "orange", "grape"]

for fruit in fruits:
  print(fruit)
  print(fruit + " pie")

# For loops with range
for number in range(1, 11, 3): # the 3 is step meaning how much it skips by
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)