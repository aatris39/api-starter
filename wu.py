import random

nums = []

for i in range(100):
  n = random.randint(1, 4)
  nums.append(n)

for number in nums:
  if number == 1:
    print("Success!")