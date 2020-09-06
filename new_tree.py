class Node:
    def __init__(self, substring = '', start = -1, end = -1):
        self.substring = substring
        self.start = start
        self.end = end
        self.children = {}

    def PrintNode(self, pre = ''):
        print(pre + ' ' + self.substring + ' (' + str(self.start) + ',' + str(self.end) + ')')
        for child in self.children.values():
            newPre = pre + '+'
            child.PrintNode(newPre)

class Tree:
    def __init__(self, text):
        text += '$'
        self.root = Node()
        # Make first node as longest suffix possible (entire text)
        self.root.children[text[0]] = Node(text, 0, len(text) - 1)
        print('adding ' + text[0:])

        # Add rest of suffixes from longest to shortest
        for i in range(1, len(text) - 1):
            print('adding ' + text[i:])
            # Always start at root when adding new node
            currentNode = self.root
            j = i
            while j < len(text):
                if text[j] in currentNode.children:
                    child = currentNode.children[text[j]]
                    childSubstring = child.substring
                    # Walk along edge until mismatch or edge label ends
                    k = j + 1
                    while k - j < len(childSubstring) and text[k] == childSubstring[k-j]:
                        k += 1
                    if k - j == len(childSubstring):
                        # Edge label ended, keep searching on child
                        currentNode = child
                        j = k
                    else:
                        # Mismatch
                        childRest = childSubstring[k-j]
                        insertedRest = text[k]
                        mid = Node(childSubstring[:k-j])
                        mid.start = child.start
                        mid.end = mid.start + (k - j - 1)

                        mid.children[insertedRest] = Node(text[k:], k, len(text) - 1)
                        mid.children[childRest] = child
                        child.start = mid.end + 1

                        child.substring = childSubstring[k-j:]
                        currentNode.children[text[j]] = mid
                else:
                    # Fell off, make a new node hanging from current
                    currentNode.children[text[j]] = Node(text[j:], j, len(text) - 1)
    
    def PrintTree(self):
        self.root.PrintNode()

t = Tree('minimize')
t.PrintTree()
