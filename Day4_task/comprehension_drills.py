# Task 02: List Comprehension Drills

#Drill 1: Extract numbers divisible by 3 from a list of 20 integers
numbers = [1, 3, 7, 9, 12, 14, 15, 18, 20, 21, 25, 27, 30, 33, 37, 40, 42, 45, 49, 51]
div_by_3 = [n for n in numbers if n % 3 == 0]
print("Divisible by 3:", div_by_3)

#Drill 2: Words longer than 4 characters in Title Case
words = ["cat", "elephant", "dog", "python", "rat", "tiger", "ant", "leopard", "owl", "parrot"]
long_words = [w.title() for w in words if len(w) > 4]
print("Long words>3 (Title Case):", long_words)

#Drill 3: Convert Celsius temperatures to Fahrenheit
celsius_temps = [0, 10, 20, 25, 30, 37, 40, 100]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print("Fahrenheit:", fahrenheit_temps)

#Drill 4: Flatten a nested list using a single comprehension
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
flat = [item for sublist in nested for item in sublist]
print("Flattened:", flat)


# EXPLORE

# Dict comprehension: map each word to its length
word_lengths = {w: len(w) for w in words}
print("\nDict comprehension (word: length):", word_lengths)

# Set comprehension: unique first letters of words (sets remove duplicates automatically)
first_letters = {w[0].upper() for w in words}
print("Set comprehension (unique first letters):", first_letters)