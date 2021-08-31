import random

# choice() function: Returns a random element from the given sequence
print("random number from range (100)", random.choice(range(100)))
print("random number from range (100, 150)", random.choice(range(100, 150)))
list = [1,2,3,5,9]
print("random element from list :", random.choice(list))
str = "Hello World"
print("random character from string :", random.choice(str))

# randrange(start, stop, step) function
print("randrange(1, 100, 2)", random.randrange(1, 100, 2))
print("randrange(100)", random.randrange(100))

# random() function: Returns a random float number between 0 and 1
print("random() :", random.random())

#seed() function: Initialize the random number generator
random.seed()
print("random number with default seed", random.random())
random.seed(10)
print("random number with int seed", random.random())
random.seed("hello", 2)
print("random number with string seed", random.random())

#shuffle() function: Takes a sequence and returns the sequence in a random order
list = [20, 16, 10, 5]
random.shuffle(list)
print("Reshuffled list :", list)
random.shuffle(list)
print("Reshuffled list :", list)

#uniform() function: Returns a random float number between two given parameters
print("Random float uniform(5, 10) :", random.uniform(5, 10))
print("Random float uniform(5, 10) :", random.uniform(7, 15))