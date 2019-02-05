import logging
from gensim.utils import simple_preprocess
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec

class MySentences(object):
    def __init__(self,fname):
        self.fname = fname
    def __iter__(self):
        for line in open(self.fname,'r'):
                tokenized_list = simple_preprocess(line)
                yield tokenized_list

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
sentences = MySentences('lyrics.txt')
model = Word2Vec(sentences,min_count = 0, workers=cpu_count())
model.save('emb')