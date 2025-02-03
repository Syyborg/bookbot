with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    lower_case = file_contents.lower()
    words = file_contents.split()
    word_count = len(words)
    char_count = {}
    for char in lower_case:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else: char_count[char] = 1 
    print("Word Count Report:")
    print(f"Total Words: {word_count}")

    print("\nCharacter Count Report:")
    for char in sorted(char_count.keys()):
        print(f"'{char}': {char_count[char]}")
