import re
import math

'''
doc = "I am well, I know"
returns a term frequency dict for doc {'i':2,'am':1,'well':1,'know':1}
'''


def tokenize(doc, total_word_freq):
    pass


# corpus like
'''
corpus = ["I am well, I know","I wonder!"]
returns a term frequency dict for corpus
{'i':2,'am':1,'well':1,'know':1,'wonder':1}
'''


def create_term_dict_for_corpus(corpus, corpus_doc_dicts=[]):
    pass


def tfidf(term, row_index, corpus_doc_dicts, total_word_freq):
    pass


corpus = ["I am well, I know", "I wonder!", "have you ever thought", "oh my my",
          "I'm so excited for you"]
total_word_freq, corpus_doc_dicts = create_term_dict_for_corpus(corpus)
tfidf("wonder", 1, corpus_doc_dicts, total_word_freq)  # == 0.46438561897747244
