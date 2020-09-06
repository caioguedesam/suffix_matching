class Node:
    def __init__(self, substring = '', start = -1, end = -1, parent = None):
        self.start = start
        self.end = end
        self.children = {}
        self.parent = parent
        self.discovered = False

    def GetChildCount(self):
        return len(self.children.values())

    def GetAccumulatedSubstring(self, text):
        currentSubstring = ''
        currentNode = self
        while(currentNode.parent != None):
            currentSubstring = text[currentNode.start:currentNode.end + 1] + currentSubstring
            currentNode = currentNode.parent
        return currentSubstring

    def PrintNode(self, pre = ''):
        nodeString = pre + ' (' + str(self.start) + ',' + str(self.end) + ')'
        print(nodeString)
        for child in self.children.values():
            newPre = pre + '+'
            child.PrintNode(newPre)

class Tree:
    # Construção da árvore com o texto dado.
    def __init__(self, text):
        # Inicia a construção adicionando o caractere de término de sufixo
        # e adicionando uma raiz vazia.
        text += '$'
        self.root = Node()

        # Primeiro, coloca o primeiro sufixo que é o texto inteiro.
        self.root.children[text[0]] = Node(text, 0, len(text) - 1)

        # Add rest of suffixes from longest to shortest
        for i in range(1, len(text) - 1):
            # Always start at root when adding new node
            currentNode = self.root
            j = i
            while j < len(text):
                if text[j] in currentNode.children:
                    child = currentNode.children[text[j]]
                    childSubstring = text[child.start:(child.end + 1)]
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
                        mid = Node(childSubstring[:k-j], child.start, child.start + (k - j - 1), currentNode)

                        mid.children[insertedRest] = Node(text[k:], k, len(text) - 1, mid)
                        mid.children[childRest] = child
                        child.parent = mid
                        child.start = mid.end + 1

                        currentNode.children[text[j]] = mid
                else:
                    # Fell off, make a new node hanging from current
                    currentNode.children[text[j]] = Node(text[j:], j, len(text) - 1, currentNode)

    
    # Função para busca recursiva na árvore à procura do nó interno com a maior profundidade.
    # Entende-se profundidade como o tamanho da substring acumulada até o nó atual.
    # A busca em si é uma simples DFS.
    def SearchRecursion(self, currentNode, currentDepth, maxDepth, maxDepthNode):
        currentNode.discovered = True

        if currentNode != self.root:
            currentDepth += currentNode.end - currentNode.start + 1
            # Caso a profundidade atual passe a máxima encontrada, vira a nova máxima.
            if currentDepth > maxDepth[0]:
                maxDepth[0] = currentDepth
                maxDepthNode[0] = currentNode

        # Continua a busca.
        for child in currentNode.children.values():
            # Considera apenas os nós internos (onde pode haver ums substring repetida).
            if child.discovered == False and len(child.children) >= 2:
                self.SearchRecursion(child, currentDepth, maxDepth, maxDepthNode)

    # Realiza a busca a partir da raiz da árvore.
    def Search(self):
        maxDepthNode = [self.root]
        self.SearchRecursion(self.root, 0, [0], maxDepthNode)
        return maxDepthNode[0]

    def PrintTree(self):
        self.root.PrintNode()
