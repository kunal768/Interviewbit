from collections import defaultdict
class TrieNode :
    def __init__(self):
        self.children = defaultdict()
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for w in word :
            if not w in root.children :
                root.children[w] = TrieNode()
            root = root.children[w]
        root.isEnd = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for w in word :
            if w in root.children:
                root = root.children[w]
            else:
                root = None 
                return False
        # isEnd hona chahiye and null bhi nhi hona chahaie
        return root and root.isEnd
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for w in prefix :
            if w in root.children :
                root = root.children[w]
            else:
                return False
        
        return True 
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
