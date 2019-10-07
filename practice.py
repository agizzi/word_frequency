STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
# print(STOP_WORDS)

print('Hey!!')
text_file = open("seneca_falls.txt", "r")

if text_file.mode == "r":
    text_contents = text_file.read().lower()


words = (text_contents.split())
# print(words)


def clean_text(text):
    # Given a test, return teh text with no spaces or punctuation and all lowercased.
    # text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep


clean_words = []

for word in words:
    clean_words.append(clean_text(word))

go_words = [word for word in clean_words if word not in STOP_WORDS]


word_count = {}

for go_word in go_words:
    word_count.update({go_word: go_words.count(go_word)})

print(word_count)
