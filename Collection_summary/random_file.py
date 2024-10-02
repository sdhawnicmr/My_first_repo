import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print(random_number)

# Generate a random float between 0 and 1
random_float = random.random()  #generates decimal numbers
print(random_float)

# Generate a random float between 1.5 and 5.5
random_float_in_range = random.uniform(1.5, 5.5)
print(random_float_in_range)

# Generate a random number between 0 and 100, with step 5
random_step = random.randrange(0, 100, 5)
print(random_step)

# Generate a random choice from a list
choices = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(choices)
print(random_choice)

# Shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Generate a list of 3 random numbers between 1 and 10
random_numbers = random.sample(range(1, 11), 3)
print(random_numbers)

# Set the seed
random.seed(42)
# Generate random numbers
print(random.randint(1, 10))
print(random.random())




