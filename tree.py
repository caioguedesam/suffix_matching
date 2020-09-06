class Node:
    def __init__(self, start = -1, end = -1, parent = None):
        self.start = start
        self.end = end
        self.children = {}
        self.parent = parent
        self.discovered = False

    def GetChildCount(self):
        return len(self.children.values())

    # Descobre a substring acumulada desde a raiz até esse nó, com posição de início e fim.
    def GetAccumulatedSubstring(self, text):
        currentSubstring = ''
        currentNode = self
        #start = self.start
        # Volta na árvore até a raiz.
        while(currentNode.parent != None):
            # Adiciona a substring acumulada e o novo início da substring.
            currentSubstring = text[currentNode.start:currentNode.end + 1] + currentSubstring
            #start = currentNode.start
            #print(start)

            # Continua a operação no próximo nó pai.
            currentNode = currentNode.parent

        # Retorna a substring e sua posição de início.
        return [currentSubstring, self.end - len(currentSubstring) + 1, self.end]

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
        self.root.children[text[0]] = Node(0, len(text) - 1)

        # Depois, adiciona todos os sufixos restantes um por um (algoritmo ingênuo).
        for i in range(1, len(text) - 1):
            currentNode = self.root
            j = i
            while j < len(text):
                # Caso haja algum nó para continuar o sufixo saindo do nó atual:
                if text[j] in currentNode.children:
                    # Nós indicados com o primeiro caractere, que não se repete em árvores de sufixo.
                    child = currentNode.children[text[j]]
                    # Descobre até onde vai o sufixo atual nesse nó.
                    k = j + 1
                    while k - j < (child.end - child.start + 1) and text[k] == text[child.start + (k - j)]:
                        k += 1
                    # Caso o sufixo atual seja consumido por esse nó, continua procurando no próximo.
                    if k - j == (child.end - child.start + 1):
                        currentNode = child
                        j = k
                    # Caso o contrário, houve um casamento parcial entre o sufixo do nó e o adicionado.
                    else:
                        # Nesse caso, faz um nó pai com o casamento parcial e adiciona
                        # o restante a adicionar e o sufixo que sobrou do nó como filhos desse novo nó.
                        childRest = text[child.start + (k-j)]
                        insertedRest = text[k]
                        mid = Node(child.start, child.start + (k - j - 1), currentNode)

                        mid.children[insertedRest] = Node(k, len(text) - 1, mid)
                        mid.children[childRest] = child
                        
                        child.parent = mid
                        child.start = mid.end + 1

                        currentNode.children[text[j]] = mid
                # Caso não tenha nenhum nó que continue o sufixo, cria um novo nó com o restante. 
                else:
                    currentNode.children[text[j]] = Node(j, len(text) - 1, currentNode)

    
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
