count = 0
len_count = 0
len_list = []
list = []

with open('reviews.txt', 'r', encoding = 'UTF-8') as f:
	for review in f:
		list.append(review)
		len_count += 1
		if len_count % 100000 == 0:
			print(len(list))
		len_list.append(len(review))
		#print(len_list)

x = sum(len_list) / len(len_list)
print('total 平均數是', round(x, 2))

print(list[0])
print(list[1])
print(list[2])