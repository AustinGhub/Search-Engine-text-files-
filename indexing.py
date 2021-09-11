import collections,re,array,struct,csv,math
import pathlib


hit = collections.namedtuple("Hit", "offsets")


def wordFind(texts):
    return re.findall(r"\w+", texts.lower())

def indexer():
    documents = []
    index = collections.defaultdict(list)
    terms = {}
    words = []

    dir = 'large-sample'
    dir = pathlib.Path(dir)
    tinydir = dir/".tiny"
    tinydir.mkdir(exist_ok=True)

    for path in dir.glob("**/*.txt"):
        text = path.read_text(encoding = "utf-8", errors = "replace")
        doc_words = wordFind(text) #holds the value of the words
        #print(doc_words)
        words.append(doc_words)

    csv_writing(words)
    
def csv_writing(wordList: list):
    with open("terms.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for word in wordList:
            writer.writerow(word)

indexer()

