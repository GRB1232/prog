
def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]
        return max_length, longest_words