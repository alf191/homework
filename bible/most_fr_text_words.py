#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""


from pathlib import Path


f = Path(__file__).parent.absolute() / "king_james_bible.txt"
BIBLE = f.read_text()


def most_freq_bible_words(n: int) -> list:
    pass


if __name__ == "__main__":
    print(*most_freq_bible_words(10), sep="\n")
    
import string
    
words = open('Phyton1.txt').read().lower().translate(str.maketrans('', '', string.punctuation + '—')).split()
most_fr_text_words = []
for word in words:
  if word not in most_fr_text_words:
    most_fr_text_words.append(word)
    counts = []
    for t_word in most_fr_text_words:
        count = 0
        for word in words:
            if word == t_word:
                count += 1
        counts.append((count, t_word))
    counts.sort()
    counts.reverse()
for i in range(min(10, len(counts))):
    count, word = counts[i]
    print(word, count)
