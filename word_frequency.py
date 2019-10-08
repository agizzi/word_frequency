import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def clean_text(text):
        text = text.strip(string.punctuation)
        if text[-2:] == "'s":
            text = text[:-2]
        return text


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pass
    print('Hey!!')
    with open(file) as text_file:
        text_contents = text_file.read().lower()
        words = (text_contents.split())


    def clean_text(text):
        text = text.strip(string.punctuation)
        if text[-2:] == "'s":
            text = text[:-2]
        return text

    clean_words = []

    for word in words:
        clean_words.append(clean_text(word))

    go_words = [word for word in clean_words if word not in STOP_WORDS]

    word_count = {}

    for go_word in go_words:
            word_count.update({go_word: go_words.count(go_word)})

    # print(word_count)
    words_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print(words_sorted)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
