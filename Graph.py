class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')' + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        print(edge)
        for i, j in enumerate(self.nodes):
            print(i, j, end = ' ')
        #for key in self.edges.items():
        #    print(key, end = '  ')
        print('NAMES', src.getName(), dest.getName())
        if src not in self.nodes or dest not in self.nodes:
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        print('Graph edge =', edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, edge)
        print('Here')
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
#for n in nodes:
    #print n
#    g.addNode(n)

n1 = Node("ABC")
n2 = Node("ACB")
n3 = Node("BAC")
n4 = Node("BCA")
n5 = Node("CAB")
n6 = Node("CBA")

g.addNode(n1)
g.addNode(n2)
g.addNode(n3)
g.addNode(n4)
g.addNode(n5)
g.addNode(n6)

g.addEdge(Edge(n1, n2))

#e1 = Edge(Node("ABC"), Node("ACB"))
#e2 = Edge(Node("ABC"), Node("BAC"))
#e3 = Edge(Node("BAC"), Node("BCA"))
#e5 = Edge(Node("CAB"), Node("CBA"))

#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#g.addEdge(e5)
