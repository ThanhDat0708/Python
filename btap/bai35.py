# Bai 35: Noi ba tu dien thanh mot tu dien
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}

result = {}
for items in (first, second, third):
    result.update(items)

print(result)
