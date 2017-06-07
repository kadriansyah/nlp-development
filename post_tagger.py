import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import ne_chunk
from nltk import RegexpParser
from nltk import StanfordPOSTagger
from nltk import StanfordNERTagger

stanfordPOSTagger = StanfordPOSTagger("stanford-postagger-full-2016-10-31/alodokter-train.tagger", "/Users/SUMOTEKHNOLOGISOLUSI/Projects/personal/standford NLP/stanford-postagger-full-2016-10-31/stanford-postagger-3.7.0.jar")

text = 'Seusai makan, sistem pencernaan Anda akan memecah karbohidrat menjadi gula atau glukosa yang bisa diserap oleh aliran darah. Zat tersebut sangat penting untuk sumber energi sel-sel tubuh Anda. Darah mengalirkan zat gula ini menuju sel-sel tubuh guna menjadikannya energi. Namun, zat gula ini harus melewati sebuah pintu untuk memasuki sel-sel tersebut. Hormon yang berperan dalam membuka pintu itu adalah insulin. Insulin dihasilkan oleh pankreas. Setelah memasuki sel, zat gula ini akan dibakar menjadi energi yang bisa Anda pakai. Gula yang lebih akan disimpan di hati untuk dipakai di kemudian hari.'
# sentences = nltk.sent_tokenize(text)
# sentences = [nltk.word_tokenize(sent) for sent in sentences]
# sentences = [stanfordPOSTagger.tag(sent) for sent in sentences]
# sentences = [tuple(item[1].split('/')) for sent in sentences for item in sent]
# print(sentences)
# print(ne_chunk(sentences))

# print('\n')
#
stanfordNERTagger = StanfordNERTagger('stanford-ner-2016-10-31/classifiers/alodokter-ner-model.ser.gz', 'stanford-ner-2016-10-31/stanford-ner-3.7.0.jar')
sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [stanfordNERTagger.tag(sent) for sent in sentences]
sentences = [item for sent in sentences for item in sent]
print(sentences)
# print(ne_chunk(sentences))

# grammar = r"""
#     NP: {<DET>?<ADJ>*<NOUN>}
# """
# grammar = r"""
#     NP: {<NOUN>+}
# """
# cp = RegexpParser(grammar)
# result = cp.parse(sentences)
# print(result)
