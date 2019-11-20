from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups

class KNN:
    def __init__(self):
        newsgroups_train = fetch_20newsgroups(subset='train')
        newsgroups_test = fetch_20newsgroups(subset='test')
        self.Labels = newsgroups_train.target_names
        X_train = newsgroups_train.data
        y_train = y_train = newsgroups_train.target
        self.text_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', KNeighborsClassifier()),
                        ])

        self.text_clf.fit(X_train, y_train)
    
    def predict(self, _str):
        test = [_str]
        print("test data ", test)
        pre_label_idx = self.text_clf.predict(test)
        pre_label_str = self.Labels[int(pre_label_idx)]
        return pre_label_str
