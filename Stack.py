from Node import *
class Stack:

    #creates a new empty stack
    def createStack(self):
        #In a empty stack the top pointer is null
        self.stackPoint = Node(None, None)
    #Add an item to the stack
    def push(self, stack, value):
        newNode = Node(None, None)
        newNode.setValue(value)
        newNode.setNext(stack.stackPoint)
        stack.stackPoint = newNode
        print "You added number %d \n" % (value)

    #removes the top item from the stack
    def pop(self, stack):
        print "You removed %d \n" %(stack.stackPoint.value)
        node = stack.stackPoint
        stack.stackPoint = node.nextNode
        print "New top %d \n" %(stack.stackPoint.value)
    #gets minimun value in stack
    def getMin(self, stack):
        minValue = Node(None, None)
        if(stack.stackPoint == None):
            print "Empty Stack"
            return False
        else:
            node = stack.stackPoint
            minValue = node
            while(node.value is not None):
                if(node.value < minValue.value  ):
                    minValue = node
                node = node.nextNode

            print "The minimun value is %d" % (minValue.value)