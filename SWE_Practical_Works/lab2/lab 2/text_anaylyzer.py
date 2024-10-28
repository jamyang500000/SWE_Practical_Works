def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('C:\\Users\\DELL\\Desktop\\SWE_Practical_Works\\SWE_Practical_Works\\lab2\\lab 2\\sample.txt')
print(content[:100])  # Print the first 100 characters
def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('C:\\Users\\DELL\\Desktop\\SWE_Practical_Works\\SWE_Practical_Works\\lab2\\lab 2\\sample.txt')
