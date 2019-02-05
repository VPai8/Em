from gensim.models.word2vec import Word2Vec
import sys
import json
model = Word2Vec.load('emb')
string=sys.argv[1]
string=string.lower()
try:
	values=model.most_similar(string)
except KeyError:
	values=[(string,"not found in vocabulary")]
json_string = json.dumps(values)
print(json_string)

