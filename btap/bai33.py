# Bai 33: Sap xep tu dien theo gia tri tang dan va giam dan
import operator

items = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Tu dien ban dau:", items)

sorted_items = sorted(items.items(), key=operator.itemgetter(1))
print("Tu dien tang theo gia tri:", sorted_items)

sorted_items = dict(sorted(items.items(), key=operator.itemgetter(1), reverse=True))
print("Tu dien giam theo gia tri:", sorted_items)
