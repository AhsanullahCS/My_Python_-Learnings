class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

start = None
end = None

def Insert_At_Start(data):
    global start,end
    new_node = node(data)

    if start == None:
        start = end = new_node
        return
    start.previous = new_node
    new_node.next = start
    start = new_node

def Insert_At_End(data):
    global start,end
    new_node = node(data)
    
    if start == None:
        start = end = new_node
        return
    end.next = new_node
    new_node.previous = end
    end = new_node

def Insert_At_Specific_Position(position, value):
    global start,end
    new_node = node(value)
    
    if start == None:
        start = end = new_node
        return
    
    if position == 1:
        new_node.next = start
        start.previous = new_node
        start = end = new_node
        return

    temp = start
    for i in range(1, position-1):
        if temp == None:
            print("NOT VALID POSITION")
            return
        temp = temp.next
    if temp == None or temp.next == None:
        print("NOT VALID POSITION")
        return
    
    old_next  = temp.next
    
    temp.next = new_node
    new_node.previous = temp
    new_node.next = old_next
    old_next.previous = new_node


def Print():
    if start == None:
        print("NO DATA TO PRINT")
        return
    temp = start
    while temp is not None:
        print(temp.data)
        temp = temp.next

def Search(value):
    if start == None:
       print("NO DATA TO PRINT")
       return
    found = False
    count = 1
    temp = start
    while temp is not None:
        if temp.data == value:
            found = True
            break
        count = count+1
        temp = temp.next
    if found:
        print(f"THE NUMBER YOU ENTER {value} IS FOUND AT LOCATION NUMBER {count}")
    else:
        print(f"THE NUMBER YOU ENTER {value} IS NOT FOUND")

def Delete_At_start():
    global start,end
    
    if start == None:
        print("NO NODE TO DELETE")
        return
    
    if start == end:
        start = end = None
        return

    start = start.next
    start.previous = None

def Delete_At_End():
    global start,end
    
    if start == None:
        print("NO NODE TO DELETE")
        return
    
    if start == end:
        start = end = None
        return
    
    end = end.previous
    end.next = None

def Delete_At_Specific_Position(delpos):
    global start,end
    
    if start == None:
        print("NO NODE TO DELETE")
        return
    
    if delpos == 1:
        if start == end:
            start = end = None 
            return

        start = start.next
        start.previous = None
        return
    
    temp = start
    for i in range(1,delpos-1):
        if temp == None:
            return
        temp = temp.next

    if temp == None or temp.next == None:
        return
    
    deleteNode = temp.next

    temp.next = deleteNode.next
    deleteNode.next.previous = temp


if __name__ == "__main__":
    Insert_At_Start(10)
    Insert_At_End(20)
    Insert_At_End(30)
    Insert_At_End(40)
    Insert_At_End(50)
    Delete_At_Specific_Position(3)

    Print()