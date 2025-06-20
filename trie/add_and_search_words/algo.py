class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False

    def __repr__(self):
        return f"Node(children={set(self.children.keys())})"

class WordDictionary:
    def __init__(self):
        self.root = Node()
        self.root.children['.'] = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        wildcard_node = self.root.children['.']
        for ch in word:
            if not '.' in wildcard_node.children:
                wildcard_node.children['.'] = Node()

            if not ch in node.children:
                node.children[ch] = Node()

            wildcard_node.children[ch] = node.children[ch]
            node.children['.'] = wildcard_node.children['.']

            wildcard_node = wildcard_node.children['.']
            node = node.children[ch]

        node.end_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            print(f"looking for {ch} in {node}")
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return True
