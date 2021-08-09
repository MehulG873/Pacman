import sys
import copy
class Node(object):
    def __init__(self, pos):
        self.pos = pos
        self.neighbours = []
    def addNeighbour(self, n):
        self.neighbours.append(n)
        #print(f"Neighbours: {self.neighbours}")
    def __repr__(self):
        return f"Node Position: {self.pos}"
def shortestDijkastra(graph, iNode, fNode):
    """ print()
    print()
    print()
    print()
    print()
    print()
    print()
    print() """
    unvisited = set()
    distance = dict()
    for key in graph:
        unvisited.add(graph[key])
        distance[graph[key]] = sys.maxsize
    distance[fNode] = 0
    currentNode = fNode
    while iNode in unvisited:
        for neighbour in currentNode.neighbours:
            #print(currentNode.neighbours)
            if neighbour in unvisited:
                nodeDistance = distance[currentNode]
                if (distance[neighbour] > nodeDistance + 1):
                    distance[neighbour] = nodeDistance + 1
        unvisited.remove(currentNode)
        if iNode not in unvisited:
            break
        else:
            minDist = sys.maxsize
            minNode = None
            for key in distance:
                if distance[key] < minDist and key in unvisited:
                    minDist = distance[key]
                    minNode = key
            currentNode = minNode
    minDistance = sys.maxsize
    minNode = None
    for neighbour in iNode.neighbours:
        if (distance[neighbour] < minDistance):
            minDistance = distance[neighbour]
            minNode = neighbour
    print(minNode)
    return minNode

def longestDijkastra(graph, iNode, fNode):
    """ print()
    print()
    print()
    print()
    print()
    print()
    print()
    print() """
    unvisited = set()
    distance = dict()
    for key in graph:
        unvisited.add(graph[key])
        distance[graph[key]] = sys.maxsize
    distance[fNode] = 0
    currentNode = fNode
    while iNode in unvisited:
        for neighbour in currentNode.neighbours:
            #print(currentNode.neighbours)
            if neighbour in unvisited:
                nodeDistance = distance[currentNode]
                if (distance[neighbour] > nodeDistance + 1):
                    distance[neighbour] = nodeDistance + 1
        unvisited.remove(currentNode)
        if iNode not in unvisited:
            break
        else:
            minDist = sys.maxsize
            minNode = None
            for key in distance:
                if distance[key] < minDist and key in unvisited:
                    minDist = distance[key]
                    minNode = key
            currentNode = minNode
    maxDistance = 0
    maxNode = None
    for neighbour in iNode.neighbours:
        if (distance[neighbour] > maxDistance):
            maxDistance = distance[neighbour]
            maxNode = neighbour
    print(maxNode)
    return maxNode
def generateGraph(board):
    graph = dict()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != "X":
                graph[(row, col)] = Node((row, col))
    for pos in graph:
        row, col = pos
        #print(row, col)
        changes = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        node = graph[pos]
        for change in changes:
            if (row + change[0], col + change[1]) in graph:
                neighbour = graph[(row + change[0], col + change[1])]
                #print(f"Neighbour: {neighbour}")
                node.addNeighbour(neighbour)
    """ for pos in graph:
        row, col = pos
        node = graph[(row, col)]
        for dr in range(-1, 2, 2):
            if row + dr >= 0 and row + dr < len(board) and (board[row + dr][col] != "X"):
                print(f"Node: {node} Neighbour: {graph[(row + dr, col)]}")
                node.addNeighbour(graph[(row + dr, col)])
        for dc in range(-1, 2, 2):
            if col + dc >= 0 and col + dc < len(board[0]) and (board[row][col + dc] != "X"):
                print(f"Node: {node} Neighbour: {graph[(row, col + dc)]}")
                node.addNeighbour(graph[(row, col + dc)]) """
    return graph
