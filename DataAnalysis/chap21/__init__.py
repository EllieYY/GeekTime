from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import nltk
import jieba


tfidf_vec = TfidfVectorizer()

documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)

print('不重复的词：', tfidf_vec.get_feature_names())
print('每个单词的ID：', tfidf_vec.vocabulary_)
print('每个单词的 tfidf 值:', tfidf_matrix.toarray())

word_list = nltk.word_tokenize(documents)
nltk.pos_tag(word_list)

# 停用词表，通常通过外部文件读取。



# clf = MultinomialNB(alpha=0.001).fit()










