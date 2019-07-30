import re


class Appearance:

    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency

    def __repr__(self):
        return str(self.__dict__)


class Database:
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        return str(self.__dict__)

    def get(self, id):
        return self.db.get(id, None)

    def add(self, document):
        return self.db.update({document['id']: document})

    def remove(self, document):
        return self.db.pop(document['id'], None)


class InvertedIndex:

    def __init__(self, db):
        self.index = dict()
        self.db = db

    def __repr__(self):
        return str(self.index)

    def index_doc(self, document):
        clean_txt = re.sub(r'[^\w\s]', '', document['text'])
        # print(clean_txt)
        terms = clean_txt.split(' ')
        # print(terms)
        appearances_dict = dict()
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)
            # print(appearances_dict[term])
        update_dict = {key: [appearance] if key not in self.index else self.index[key] + [appearance] for
                       (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)
        # print(self.index)
        # Add the document into the database
        self.db.add(document)
        # print(appearances_dict)
        # print(update_dict)

        return document

    def lookup_query(self, query):
        return {term: self.index[term] for term in query.split(' ') if term in self.index}


def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def main():
    db = Database()
    index = InvertedIndex(db)
    document1 = {
        'id': '1',
        'text': 'The big sharks of Belgium drink beer.'
    }
    document2 = {
        'id': '2',
        'text': 'Belgium has great beer. They drink beer all the time.'
    }
    index.index_doc(document1)
    index.index_doc(document2)

    search_term = input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)

    for term in result.keys():
        for appearance in result[term]:
            document = db.get(appearance.docId)
            print(highlight_term(appearance.docId, term, document['text']))
        print("-----------------------------")


main()

# https://www.geeksforgeeks.org/inverted-index/
# reference: https://medium.com/@fro_g/writing-a-simple-inverted-index-in-python-3c8bcb52169a
# highlighting command line: https://gist.github.com/vratiu/9780109
