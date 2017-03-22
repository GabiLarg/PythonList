from Stack import *


def usage():
    print   "Let me tell you how it works\n" \
            "We start with an empty stack\n" \
            "Then you can add numbers typing push <number you want> (we only accept integers)\n" \
            "You can remove top item by typing pop\n" \
            "If you want I can tell you the min number in our beutiful stack by typing min\n" \
            "I will be waiting you type anythin, but ig you want you leave just type 0\n\n" \
            "Enjoy!"

def main():


    usage()
    stack = Stack()
    stack.createStack()
    userInput = raw_input("Start here:")
    while(userInput != "0" ):
        args = userInput.split(" ")
        if(len(args)>1):
            if(args[0] == "push"):
                stack.push(stack, int(args[1]))
            elif(args[0] in ["pop", "min"]):
                print "This commands only accept 1 argument"
            else:
                print "Sorry! You are doing it wrong"
        else:
            if(args[0] == "pop"):
                stack.pop(stack)
            elif(args[0] == "min"):
                stack.getMin(stack)
            else:
                print "You didn't read, right?\n"\
                "Here we go!\n"
                usage()
        userInput = raw_input("_")
    print "Bye Bye!"

main()

