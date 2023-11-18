import random

def generate(words, sentences):
    new_sentence = []
    for sentence in sentences:
        generated = sentence.replace('_', random.choice(words), 1)
        generated_again = generated.replace('_', random.choice(words), 1)
        new_sentence.append(generated_again)
    return new_sentence


with open('input.txt', 'r', encoding='utf-8') as file:
    words = file.read().split(', ')

sentences = [
    "Если бы у меня тогда был _, жизнь стала бы чуточку проще.",
    "Я решил подарить ей на день рождения _. Она была в полном восторге, я уверен!",
    "Заказал тогда по скидке _, но пришел _. Наверное, это знак."
    ]

new_sentences = generate(words, sentences)

for sentence in new_sentences:
    print(sentence)