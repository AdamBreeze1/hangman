import nltk

# Download the NLTK words dataset (if not already downloaded)
nltk.download('words')

# Get the list of English words
from nltk.corpus import words
english_words = words.words()

# Filter for words over 3 letters
common_words = [word for word in english_words if len(word) > 3]