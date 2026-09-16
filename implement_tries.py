class TrieNode:
    def _init_(self):
        self.children = {}
        self.end = False


class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.end

    def starts_with(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


trie = Trie()

trie.insert("apple")
trie.insert("app")

print("Search apple:", trie.search("apple"))
print("Search app:", trie.search("app"))
print("Search bat:", trie.search("bat"))
print("Starts with ap:", trie.starts_with("ap"))
