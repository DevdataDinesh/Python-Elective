input_string = input("Enter a string: ")
words = input_string.lower().split()
word_frequencies = {}
for word in words:
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1
print("Word frequencies: ", word_frequencies)