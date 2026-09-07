# Bai 8: Tim cac tu dai hon n ky tu

def long_words(text, minimum_length):
    return [word for word in text.split() if len(word) > minimum_length]


text = "Con cao nau nhanh nhay qua con cho luoi bieng"
print(long_words(text, 3))
