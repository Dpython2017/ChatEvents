# {'Practicing':{summary_id:count}}
import json


class InvertedTree:
    """ Implementation of inverted tree"""

    def __init__(self):
        self.tree = {}
        self.file = open('data.json')
        self.data = json.load(self.file)

    def __pre_processing(self, word):
        """
            Method removes the articles and supporting words from the sentence.
            If the word is a skip word it is not added to the tree.

            :param word: word from the book summary
            :rtype: bool
        """
        skip_words = {'a': None, 'the': None, 'this': None, 'an': None, 'them': None, 'these': None, 'to': None,
                      'in': None, 'on': None, 'you': None, 'at': None, 'and': None, 'your': None, 'than': None,
                      'sentences': None, 'for': None, 'is': None, 'as': None, 'what': None, 'most': None, 'of': None,
                      'we': None, 'that': None, 'those': None, 'by': None, 'are': None, 'with': None, 'ie': None,
                      'not': None, 'our': None, 'us': None, 'their': None, 'it': None, 'off': None, 'how': None,
                      'but': None, 'he': None, 'was': None, 'be': None, 'do': None, 'can': None, 'when': None,
                      'will': None, 'make': None, 'does': None, 'else': None, 'get': None, 'into': None, 'each': None,
                      'go': None, 'there': None, 'more': None, 'if': None, 'then': None, 'any': None, 'too': None,
                      'also': None, 'until': None, 'or': None, 'yes': None, 'his': None, 'book': None,'three':None}

        if word in skip_words:
            return False
        return True

    def __stemming(self, word):
        pass

    def __translation(self, word):
        """
            Method removes punctuations from the word each word is iterated thru and punctuations
            in the list are removed from the word.

            :param word: word from the summary
            :rtype: str
        """
        punctuations = ['[', ']', '\'', '\"', '?', '(', ')', ' ', ',', '.', '“', '”', '-', '+', '’']
        new_word = ''
        for i in word:

            if i not in punctuations:
                new_word += i
        return new_word

    def __word_occurrence(self, summary, summary_id):
        """
            Implementation populates the tree with keywords and its occurrences
            :param summary: summary for a given book
            :param summary_id: id of the summary
        """
        summary = summary.lower()
        summary = summary.split(" ")

        for i in range(len(summary)):
            word = self.__translation(summary[i])
            if self.__pre_processing(word):
                if word in self.tree:
                    if summary_id in self.tree[word]:
                        self.tree[word][summary_id] += 1
                    else:
                        self.tree[word][summary_id] = 1
                else:
                    self.tree[word] = {summary_id: 1}

        return self.tree

    def insert(self):
        """ Public method that calls the word_occurrence implementation and creates a tree"""
        summaries = self.data['summaries']
        for summary in summaries:
            self.__word_occurrence(summary['summary'], summary['id'])

    def print_tree(self):
        for key, val in self.tree.items():
            print(key, val)

    def get_summary(self, id):
        """
            Getter that take in the summary id and returns the summary
            :param id: summary id
            :rtype: str

        """
        return self.data['summaries'][id]






