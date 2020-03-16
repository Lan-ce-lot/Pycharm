import nltk
import ssl
print('down')
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('averaged_perceptron_tagger')
# nltk.download("punkt")
# print('down')

# import nltk
# print(1)

# print(1)
# # 先分句再分词
# sents = nltk.sent_tokenize("And now for something completely different. I love you.")
# word = []
# for sent in sents:
#     word.append(nltk.word_tokenize(sent))
# print(word)
#
# # 分词
# text = nltk.word_tokenize("And now for something completely different.")
# print(text)
# # 词性标注
# tagged = nltk.pos_tag(text)
# print(tagged[0:6])
# # 命名实体识别
# entities = nltk.chunk.ne_chunk(tagged)
# print(entities)
