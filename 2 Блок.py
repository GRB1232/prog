def find_longest_word(slova):
    with open(file_name, 'r') as slova:
        text = slova.read()
        words = text.split()
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]
        return max_length, longest_words

file_name = 'slova.txt'
length, longest_words = find_longest_word(file_name)
print("Самое длинное слово имеет длину", length, "и это слово(а):", longest_words)
