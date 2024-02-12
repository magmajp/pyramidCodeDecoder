#Object for holding line data and sorting it into a Linked List
class Node:
    def __init__(self, num, text, next=None):
        self.num = num
        self.text = text
        self.next = next

    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    
    def getNum(self):
        return self.num
    
    def getText(self):
        return self.text


def decode(message_file):

    #reads given file
    file = open(message_file, "r")

    #splits file into a list of lines
    lines = file.readlines()

    #initializes the root of the Linked List
    root = None

    for line in lines:

        #splits the line into number and text, makes the number an int and removes the new line character from the end of the line
        split = line.split(' ',2)
        num = int(split[0])
        text = split[1][:-1]

        #creates a node with the number and text value
        node = Node(num,text)

        #inserts the Node into the sorted Linked List
        if root is None:
            root = node
        elif root.num > node.num:
            node.next = root
            root = node
        else:
            current = root
            while current.next is not None and current.next.num < node.num:
                current = current.next
            
            node.next = current.next
            current.next = node
    
    #finds nodes based on pyramid numbers and adds their text to the output
    current = root
    needed = 1
    layer = 1
    output = ""
    for x in range(0,len(lines)):
        if x == needed-1:
            output = output + " " + current.text
            layer = layer + 1
            needed = needed + layer
        current = current.next
            
    return output
        





print(decode("coding_qual_input.txt"))