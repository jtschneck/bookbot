def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read().lower()
    word_count = count_words(file_contents)
    letter_counts = count_letters(file_contents)
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document\n")
    for letter in letter_counts:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times")
    print("--- End report ---")


def count_words(text):
    return len(text.split())

def sort_on(count_dict):
    return count_dict["count"]

def count_letters(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    ret = []
    for char, count in counts.items():
        if char.isalpha():
            ret.append({"char": char, "count": count})
    ret.sort(key=sort_on, reverse=True)
    return ret



main()