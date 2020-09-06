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
        self.root.children[text[0]] = Node(text)
        print('adding ' + text[0:])

        # Add rest of suffixes from longest to shortest
        for i in range(1, len(text) - 1):
            print('adding ' + text[i:])
            # Always start at root when adding new node
            currentNode = self.root
            # j = currentNode substring start index
            j = i
            while j < len(text):
                # Check for an edge to 
                if text[j] in currentNode.children:
                    # Get children associated with character in position j
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
                        # Separate rests without shared prefix
                        childRest = childSubstring[k-j]
                        insertedRest = text[k]
                        # Create new midpoint to split with current shared prefix
                        mid = Node(childSubstring[:k-j])

                        # Midpoint now has two new children
                        mid.children[insertedRest] = Node(text[k:])
                        mid.children[childRest] = child

                        child.substring = childSubstring[k-j:]
                        currentNode.children[text[j]] = mid
                else:
                    # Fell off, make a new node hanging from current
                    currentNode.children[text[j]] = Node(text[j:])
    
    def PrintTree(self):
        self.root.PrintNode()

t = Tree('abcxab')
t.PrintTree()
