import random
import json

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Create a new list to store the original words
original_words = words.copy()

# Create a dictionary to store the original words and their indices
original_words_dict = {}

# Loop through each word in the original words list
for i, word in enumerate(original_words):
  # Add the word and its index to the dictionary
  original_words_dict[i+1] = word

# Initialize a flag to track whether the user has entered a valid input
valid_input = False

# Continuously prompt the user for input until a valid input is entered
while not valid_input:
  # Get the numbers of the words to shuffle from the user
  word_numbers = input("Enter the numbers of the words to shuffle (separated by spaces): ")

  # Split the word numbers string into a list of integers
  word_numbers = [int(x) for x in word_numbers.split()]

  # Check whether any of the word numbers are negative
  if any(x < 0 for x in word_numbers):
    print("Error: Word numbers must be positive integers.")
  # Check whether any of the word numbers are equal to 0
  elif any(x == 0 for x in word_numbers):
    print("Error: Word numbers must not be 0.")
  # Check whether any of the word numbers are larger than the number of words in the sentence
  elif any(x > len(words) for x in word_numbers):
    print("Error: Word numbers must not be larger than the number of words in the sentence.")
  else:
    # Set the valid_input flag to True to exit the loop
    valid_input = True

# Loop through each word number
for word_number in word_numbers:
  # Decrement the word number to get the index of the word in
  # Decrement the word number to get the index of the word in the list (since list indices start at 0)
  word_index = word_number - 1

  # Get the word to shuffle
  word = words[word_index]

  # Convert the word to a list of letters
  letters = list(word)

  # Use the shuffle function from the random module to shuffle the list of letters
  random.shuffle(letters)

  # Join the shuffled letters back into a single string
  shuffled_word = ''.join(letters)

  # Replace the original word with the shuffled word in the list of words
  words[word_index] = shuffled_word

# Join the words into a single string
shuffled_sentence = ' '.join(words)

# Convert the original words dictionary to a JSON string
original_words_json = json.dumps(original_words_dict)

# Open a new text file in write mode
with open('original_words.txt', 'w') as f:
  # Write the JSON string to the file
  f.write(original_words_json)

# Print the shuffled sentence
print(shuffled_sentence)
