import numpy as np

#defining the stack class
class queue():
    def __init__(self):
        self.pending = list()

    def add(self, child):
        self.pending.insert(0, child)

    def remove(self):
        if self.pending:
            return self.pending.pop()
        return None

    def peek(self):
        if self.pending:
            return self.pending[-1]

    def size(self):
        return len(self.pending)

class node():
    def __init__(self, current, parent):
        self.current = current
        self.parent = parent


def moveleft(node1):
    if locy == 0:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx][locy - 1]
        child[locx][locy - 1] = node1[locx][locy]
        #print(currentnode)
        return child


def moveright(node1):
    if locy != sh[1] -1:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx][locy + 1]
        child[locx][locy + 1] = node1[locx][locy]
        #print(currentnode)
        return child

def moveup(node1):
    if locx != 0:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx - 1][locy]
        child[locx - 1][locy] = node1[locx][locy]
        #print(currentnode)
        return child

def movedown(node1):
    if locx != sh[0]-1:
        return
    else:
        child = node1.copy()
        child[locx][locy] = node1[locx + 1][locy]
        child[locx + 1][locy] = node1[locx][locy]
        #print(currentnode)
        return child
