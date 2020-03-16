import jieba

f = open("三国演义.txt", "rb")
txt = f.read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:      #排除单个字的分词结果
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
        
items = list(counts.items())
items.sort(key = lambda items: items[1], reverse = True) #降序
for i in range(20):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
