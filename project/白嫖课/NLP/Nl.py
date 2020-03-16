from nltk.tokenize import WordPunctTokenizer


def wordtokenizer(sentence):
    # 分段
    words = WordPunctTokenizer().tokenize(sentence)
    return words


if __name__ == '__main__':
    print(wordtokenizer("My name is Tom."))