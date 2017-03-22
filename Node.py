'''
This class defines the each node of the stack.
'''
class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

    def setNext(self, nextNode):
        if(isinstance(nextNode, Node)):
            self.nextNode = nextNode
        else:
            self.nextNode = None

    def setValue(self, value):
        if(isinstance(value, int) or value is None):
            self.value = value
        else:
            print "Enter a valid number!"