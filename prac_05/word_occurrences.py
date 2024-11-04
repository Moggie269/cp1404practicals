"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   9:30 minutes
"""

word_to_count = {}
string = 'this is a collection of words of nice words this is a fun thing it is'
longest_word = -1
for word in string.split():
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1
    if len(word) > longest_word:
        longest_word = len(word)
for word, count in sorted(word_to_count.items()):
    print(f'{word:{longest_word}} : {count}')