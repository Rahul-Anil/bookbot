from collections import defaultdict


def read_file(file_path) -> str:
    with open(file_path) as f:
        return f.read()


def letter_count(text: str) -> dict[str, int]:
    counts = defaultdict(int)
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            counts[letter] += 1
    return counts


def main():
    file_path = "books/frankenstein.txt"
    text = read_file(file_path=file_path)
    word_count = len(text.split())

    counts = letter_count(text=text)
    counts: list[tuple[str, int]] = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for letter, count in counts:
        print(f"The '{letter}' character was found {count} times")


if __name__ == "__main__":
    main()
