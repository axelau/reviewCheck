count = 0
list = []

with open('reviews.txt', 'r', encoding = 'UTF-8') as f:
	for review in f:
		list.append(review)

print(list[0])
print(list[1])
print(list[2])