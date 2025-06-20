from utils.debug import CallTracker

tracker = CallTracker()

class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False

    def __repr__(self):
        return f"Node(children={set(self.children.keys())})"

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]

        node.end_word = True

    def search(self, word: str) -> bool:
        return dfs_search(word, 0, self.root)

@tracker.track
def dfs_search(word: str, index: int, node: Node) -> bool:
    assert index <= len(word)

    if index == len(word):
        return node.end_word

    ch = word[index]

    print(f"looking for {ch} in {node}")

    # in the case of wildcard
    if ch == '.':
        # Special case for single '.' - check if any word exists
        if len(word) == 1:
            return any(node.children.values())

        # find at least one match where a sub search on child matches the character after '.'
        return any(dfs_search(word, index+1, child_node) for child_node in node.children.values())
    else:
        if ch not in node.children:
            return False
        return dfs_search(word, index+1, node.children[ch])
