# File: 02.py
def task2():
    from collections import Counter
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.lower().split()
    counter = Counter(words)
    for word, count in counter.most_common():
        print(f"{word}: {count}")
