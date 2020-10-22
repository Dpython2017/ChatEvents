from functools import reduce
from index import InvertedTree
from datetime import datetime


def intersection(arg):
    print(arg)
    """
        Searches for the common summary id's across all dataset.
        :param arg: list of found keywords with count
        :type: list of dictionaries
        :rtype:list

    """
    d = iter(arg)
    common = reduce(set.intersection, d, set(next(d)))

    return common


def get_max_summary(summary, count, main_set):
    """
        Returns summary id with max count
        :param summary: word
        :param count: k expected output
        :param main_set: set of summary ids

        :type summary:list
        :type count: int
        :type main_set: set
    """
    for item in summary:
        val = sorted(item.items(), key=lambda x: x[1], reverse=True)[:count]
        for i in val:
            main_set.add(i[0])

    return main_set


class SearchSummary(InvertedTree):
    """ Class extends to Inverted tree """
    def __init__(self):
        super().__init__()
        self.insert()
        self.cache = {}

    def search(self, string, k):
        """
            Accepts the search parameters and the number of expected output
            :param string: search string
            :param k : Number of summaries to be returned

            :type string: str
            :type k : int

            :rtype: tuple

        """
        summary_set = []
        key = string.split(" ")
        for i in key:
            if i in self.cache:
                pass
            if i in self.tree:
                summary_set.append(self.tree[i])
                self.cache[i] = {None: datetime.now()}

        common = intersection(summary_set)

        if len(common) < k:
            count = k - len(common)
            common = get_max_summary(summary_set, count, common)

        common = list(common)
        for i in range(k):
            print(self.get_summary(common[i]))


s = SearchSummary()
s.search("control of your life", 2)
