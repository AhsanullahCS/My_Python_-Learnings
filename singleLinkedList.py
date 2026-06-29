class node:
    def __init__(self,data):
        self.data = data
        self.next = None

start = None
end   = None

def Insert_At_End(data):
    global start, end
    new_node = node(data)

    if start is None:
        start = new_node
        end = new_node
    else:
        end.next = new_node
        end = new_node   # update tail pointer

def Insert_At_Start(data):
    global start, end
    new_node = node(data)
    if start is None:
        start = new_node
        end = new_node
    else:
        new_node.next = start
        start = new_node    

def Insert_At_Specific_Position(userposition , dataadd):
    global start , end
    new_node = node(dataadd)

    if start == None:
        return 
    
    if userposition == 1:
        new_node.next = start
        start = new_node
        return
    
    temp = start

    for i in range(1,userposition-1, 1):
        if temp is None:
            print("LOCATION NOT FOUND")
            return
        temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

def Delete_At_Specific_Position(deleteposition):
    global start , end
    if start == None:
        return 
    
    if deleteposition == 1:
        temp = start
        start = start.next
        print(f"THE NUMBER {temp} at your given position {deleteposition} is removed")
        return 
    
    temp = start
    for i in range(1,deleteposition-1,1):
        if temp is None:
            return
        temp = temp.next

    if temp is None or temp.next is None:
        print("INVALID POSITION")
        return 
    delete = temp.next.data
    temp.next = temp.next.next
    print(f"THE NUMBER {delete} at your given position {deleteposition} is removed")

def PrintAll():
    result  = []
    temp = start
    while temp is not None:
        result.append(temp.data)
        temp = temp.next
    print(result)

def Delete_At_Start():
    global start , end

    if start is None:
        print("List is empty")
        return None
    
    delete_data = start.data
    start = start.next
    if start is None:
        end = None
    print(f"THE DATA AT START {delete_data} IS DELETED")     

def Delete_At_End():
    global start,end
    if start is None:
        print("List is empty")
        return None

    delete_node = end.data
    if start.data == delete_node:
        start = end = None
    else:
        temp = start
        while temp.next != end:
            temp = temp.next
    temp.next = None    
    end = temp
    print(f"THE DATA AT END {delete_node} IS DELETED")    

def Search(data):
    temp = start
    position = 1
    found = False

    while temp is not None:
        if temp.data == data:
            found = True
            print(f"THE NUMBER IS YOU ENTER {data} IS FOUND AT POSITION {position}")
        position = position + 1 
        temp = temp.next
    if not found:
        print(f"THE NUMBER IS YOU ENTER {data} IS MOT FOUND")

if __name__ == "__main__":
    Insert_At_End(10)
    Insert_At_End(20)
    Insert_At_End(30)
    Insert_At_End(40)
    Insert_At_End(50)

    Insert_At_Specific_Position(3 , 80)

    Delete_At_Specific_Position(3)
    PrintAll()
