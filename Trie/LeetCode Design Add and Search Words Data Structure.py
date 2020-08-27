from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        root = self.root
        for w in word :
            if not w in root.children :
                root.children[w] = TrieNode()
            root = root.children[w]
        
        root.isEnd = True
        
        

    def searchHelp(self, word: str,root : TrieNode()) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # actually implements prefix and suffix search due to . but also to note that . could be somewhere in the middle so its not exactly that
        # so the question comes around to how deal with the dot and that's all what this question is about 
        # root = self.root          
        for idx,val in enumerate(word):
            if val not in root.children and val != '.':
                return False
            
            if val == '.':
                for w in root.children:
                    if self.searchHelp(word[idx+1:],root.children[w]) :
                        return True 
                    
                return False
            
            else:
                root = root.children[val]
                
        return root.isEnd
        
    def search(self, word: str) -> bool:
        root = self.root
        return self.searchHelp(word,root)


                    
            
            
        
        
        
        
        
        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
