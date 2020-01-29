count = 0
len_count = 0
len_list = []
list = []
#把資料放入list, 是更方便之後的處理

with open('reviews.txt', 'r', encoding = 'UTF-8') as f:
	for review in f:
		list.append(review)
		len_count += 1
		if len_count % 100000 == 0:
			print('暫時處理數目為',len(list))
		len_list.append(len(review))
		#print(len_list)

x = sum(len_list) / len(len_list)
print('total 平均數是', round(x, 2), '\n')
print(list[0])

update_list = {}

for i in list:
	words = i.strip('\n').split(' ')
	# 將list入面既i拎出黎, 分返做字
	for word in words:
		if word in update_list:
			update_list[word] += 1
		else:
			update_list[word] = 1

for list in update_list:
	if update_list[list] > 1000:
		print(list, ':', update_list[list])
# print(update_list)


# suck = []
# for d in list:
# 	if 'suck' in d:
# 		suck.append(d)
# print('total 有suck的評論共：', len(suck), '項。')

# print(suck[0])
# print(suck[1])
# print(suck[2])


# x100 = []
# for d in list:
# 	if len(d) < 100:
# 		x100.append(d)
# print('total 少於100的評論共：', len(x100), '項。')
# print(list[0])
# print(list[1])
# print(list[2])