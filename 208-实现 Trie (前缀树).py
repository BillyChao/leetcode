# -*- coding: utf-8 -*-

"""
@Time    : 2020/7/15 下午2:14
@Author  : mc
@File    : 208-实现 Trie (前缀树).py
@Software: PyCharm
"""


class TrieNode:
    """
    TrieNode，每个节点保存一个map，其中包含当前节点后的所有分支
    每一个节点有一个flag状态标记，True表示从根节点到当前节点的路径表示一个完整的词
    """

    def __init__(self):
        self.words = {}
        self.flag = False

    def add(self, word, index, length):
        node = TrieNode()
        if index == length:
            self.flag = True
            return
        if word[index] in self.words:
            node = self.words[word[index]]
        else:
            self.words[word[index]] = node
        node.add(word, index + 1, length)

    def __dict__(self):
        js = {}
        for k, v in self.words.items():
            js[k] = v.__dict__()
        return js


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
        self.root.add(word, 0, len(word))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.root
        for c in word:
            if c in tmp.words:
                tmp = tmp.words[c]
            else:
                return False
        return tmp.flag

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.root
        for c in prefix:
            if c in tmp.words:
                tmp = tmp.words[c]
            else:
                return False
        return True

    def __dict__(self):
        return self.root.__dict__()


# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    obj = Trie()
    word = 'apple'
    prefix = 'app'
    obj.insert('apple')
    obj.insert('book')
    obj.insert('sdasa')
    print(obj.__dict__())
    print(obj.search('boo'))
    print(obj.startsWith('boapple'))
    obj.insert('app')
    print(obj.search('app'))
