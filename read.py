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
print('档案读取完了，总共有', len(data), '笔资料')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

good = [d for d in data if 'good' in d]
bad = ['bad' in d for d in data]


print('留言平均长度为', sum_len / len(data))
print('一共有', len(new), '笔留言长度小于100')
print('一共有', len(good), '笔留言提到了good')

#文字计数功能
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

while True:
	word = input('请问你想查什么字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现的次数为', wc[word])
	else:
		print('这个字没有出现！')
print('感谢使用查询功能')

