data = []
count = 0
sum_len = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		sum_len += len(line)
		if count % 100000 == 0:
			print(len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('档案读取完了，总共有', len(data), '笔资料')
print('留言平均长度为', sum_len / len(data))
print('一共有', len(new), '笔留言长度小于100')