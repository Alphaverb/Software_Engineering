def censor_text(text, banned_words):
    for word in banned_words:
        block = "*" * len(word)
        text = text.replace(word, block)
    return text

with open('input.txt', encoding='utf-8') as f:
    data = f.read()
    banned_words = data.split()
    text = ("Hello, world! Python IS the programming language of thE future. My\nEMAIL is....\nPYTHON is awesome!!!!")
    text_low = text.lower()

censored_text = censor_text(text_low, banned_words)

index = 0
result = ''

for letter in censored_text:
    if letter == '*':
        result += letter
        index += 1
    else:
        result += text[index]
        index += 1

print(result)
