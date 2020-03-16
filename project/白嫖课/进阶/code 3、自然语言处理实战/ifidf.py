import jieba.analyse

f = open('十九大报告节选.txt', "rb")
sentence = f.read()

##keywords = jieba.analyse.extract_tags(sentence, topK=15, withWeight=True, allowPOS=('n','nr','ns'))

keywords = jieba.analyse.extract_tags(sentence, topK=15, withWeight=True, allowPOS=())

for item in keywords:
    print(item[0],item[1])
