with open('article.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
count = word_count[most_common_word]

print("Наиболее часто встречающееся слово:", most_common_word)
print("Количество:", count)

