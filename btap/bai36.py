# Bai 36: Dem so lan xuat hien cua tung ky tu trong chuoi
text = "w3resource"
character_counts = {}

for character in text:
    character_counts[character] = character_counts.get(character, 0) + 1

print(character_counts)
