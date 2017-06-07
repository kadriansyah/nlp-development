import nltk
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        # initialize the base class
        HTMLParser.__init__(self)

        self.file = file
        self.start_tag = ''

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        self.start_tag = tag

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        self.start_tag = ''

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        tokens = nltk.word_tokenize(data)
        for token in tokens:
            if self.start_tag == '':
                print(token + '\t' + 'O')
                self.file.write(token + '\t' + 'O' + '\n')
            else:
                print(token + '\t' + self.start_tag.upper())
                self.file.write(token + '\t' + self.start_tag.upper() + '\n')

file = open('output.txt','w')
parser = MyHTMLParser()
with open('train.txt', 'r') as myfile:
    data = myfile.read()
    parser.feed(data)
myfile.close()
file.close()
# parser.feed('Pengamat politik dari <ORGANIZATION>Universitas Gadjah Mada</ORGANIZATION>, <PERSON>Arie Sudjito</PERSON>, menilai, keinginan Ketua Umum <ORGANIZATION>Partai Golkar</ORGANIZATION> <PERSON>Aburizal Bakrie</PERSON> untuk maju kembali sebagai ketua umum merupakan pemaksaan kehendak.')
