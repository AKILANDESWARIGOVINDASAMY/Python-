from nltk.corpus import genesis
import nltk
import os


def createUserTextCorpora(filecontent1, filecontent2):
    file1 = open("//nltk_data//content1.txt", "w")  # write mode
    file1.write(filecontent1)
    file1 = open("//nltk_data//content2.txt", "w")  # write mode
    file1.write(filecontent2)
    print(genesis.fileid())
    text_corpus = nltk.corpus.words('/nltk_data/content1.txt, /nltk_data/content2.txt')
    print(text_corpus)

    return text_corpus, no_of_words_corpus1, no_of_unique_words_corpus1, no_of_words_corpus2, no_of_unique_words_corpus2


if __name__ == '__main__':
    filecontent1 = input()

    filecontent2 = input()

    path = os.path.join(os.getcwd(), "nltk_data")
    os.makedirs(path, exist_ok=True)
    for file in os.listdir(path):
        os.remove(path + "\\" + file)

    text_corpus, no_of_words_corpus1, no_of_unique_words_corpus1, no_of_words_corpus2, no_of_unique_words_corpus2 = createUserTextCorpora(
        filecontent1, filecontent2)
    expected_corpus_files = ['content1.txt', 'content2.txt']
    if type(text_corpus) == nltk.corpus.reader.plaintext.PlaintextCorpusReader and sorted(
            list(text_corpus.fileids())) == expected_corpus_files:
        print(no_of_words_corpus1)
        print(no_of_unique_words_corpus1)
        print(no_of_words_corpus2)
        print(no_of_unique_words_corpus2)