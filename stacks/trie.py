class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not crawl.children[index]:
                crawl.children[index] = self.getNode()
            crawl = crawl.children[index]
        crawl.isEndOfWord = True

    def search(self, key):
        crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]
        return crawl != None and crawl.isEndOfWord


def main():
    keys = ["there", "a", "the", "anaswe", "any", "by", "their"]
    t = Trie()
    for key in keys:
        t.insert(key)

    print "{} --- {}".format("the", t.search("the"))
    print "{} --- {}".format("there", t.search("there"))
    print "{} --- {}".format("ther", t.search("ther"))
    #print "{} --- {}".format("any", t.search("any"))
    #print "{} --- {}".format("thee", t.search("thee"))

#main()