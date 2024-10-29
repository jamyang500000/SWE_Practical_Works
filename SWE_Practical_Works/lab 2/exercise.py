from collections import Counter

# Read file function
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Count lines function
def count_lines(content):
    return len(content.split('\n'))

# Count words function
def count_words(content):
    return len(content.split())

# Count unique words function
def count_unique_words(content):
    words = content.lower().split()
    unique_words = set(words)
    return len(unique_words)

# Find longest word function
def longest_word(content):
    words = content.split()
    return max(words, key=len)

# Count occurrences of a specific word function
def count_specific_word(content, target_word):
    words = content.lower().split()
    return words.count(target_word.lower())

# Average word length function
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Percentage of words longer than average
def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100

# Most common word function
def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Main analysis function
def analyze_text(filename, target_word):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    num_unique_words = count_unique_words(content)
    common_word, common_count = most_common_word(content)
    longest = longest_word(content)
    specific_word_count = count_specific_word(content, target_word)
    avg_length = average_word_length(content)
    percentage_longer = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Occurrences of '{target_word}': {specific_word_count}")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than average: {percentage_longer:.2f}%")

# Run the analysis with a specific word to count
analyze_text('C:\\Users\\DELL\\Desktop\\SWE_Practical_Works\\SWE_Practical_Works\\lab2\\lab 2\\sample.txt', 'specific')
