"""
Baby Vocab - A simple program to read words from
a file and print a histogram of their occurrences.
This program reads words from a file named "words.txt",
counts how many times each word appears, and prints
a histogram where each word is represented by a bar 
of 'x' characters proportional to its count.
"""

def main():
    words = load_words_from_file("words.txt")
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    for word, amount in count.items():
        print_histogram_bar(word, amount)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()