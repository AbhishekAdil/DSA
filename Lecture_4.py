# linked list

# 1) insert data at beginning

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None       # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)

    ll.print()

# print 67--->89--->5--->


# 2) insert value from the end of the linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None      # created variable head   # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

    #inserting at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)      # None = next
            return
        
        itr = self.head
        while itr.next:       # means linkedlist is not empty
            itr = itr.next    # i am at the last element

        itr.next = Node(data, None)

if __name__ == "__main__":
    ll = LinkedList()

    # inserting at the beginning
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)
    
    # insering at the last
    ll.insert_at_end(55)
    ll.insert_at_end(44)
    ll.insert_at_end(33)


    ll.print()

# print 67--->89--->5--->55--->44--->33--->


# 3) Insert list of values as an input and it will create a new fresh linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None      # created variable head   # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

    #inserting at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)      # None = next
            return
        
        itr = self.head
        while itr.next:       # means linkedlist is not empty
            itr = itr.next    # i am at the last element

        itr.next = Node(data, None)


    # insert a list of values , and it will create a new fresh linked list
    def insert_value(self, data_list):
        self.head = None    # wipping out all the current values
        for data in data_list:
            self.insert_at_end(data)

if __name__ == "__main__":
    ll = LinkedList()

    # inserting at the beginning
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)
    
    # insering at the last
    ll.insert_at_end(55)
    ll.insert_at_end(44)
    ll.insert_at_end(33)

    ll.insert_value(["banana", "mango", "grapes", "orange"])

    ll.print()

# print banana--->mango--->grapes--->orange--->


# 4) define a function to find the lenght of the linked list

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None      # created variable head   # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

    #inserting at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)      # None = next
            return
        
        itr = self.head
        while itr.next:       # means linkedlist is not empty
            itr = itr.next    # i am at the last element

        itr.next = Node(data, None)


    # insert a list of values , and it will create a new fresh linked list
    def insert_value(self, data_list):
        self.head = None    # wipping out all the current values
        for data in data_list:
            self.insert_at_end(data)

    # to find the lenght of the linked list
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

if __name__ == "__main__":
    ll = LinkedList()

    # inserting at the beginning
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)
    
    # insering at the last
    ll.insert_at_end(55)
    ll.insert_at_end(44)
    ll.insert_at_end(33)

    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print()

    # printing the lenght of the linked list
    print("length", ll.get_length())

# print banana--->mango--->grapes--->orange--->
# length 4

# 5) define a function to remove a element from the linkedlist

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None      # created variable head   # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

    #inserting at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)      # None = next
            return
        
        itr = self.head
        while itr.next:       # means linkedlist is not empty
            itr = itr.next    # i am at the last element

        itr.next = Node(data, None)


    # insert a list of values , and it will create a new fresh linked list
    def insert_value(self, data_list):
        self.head = None    # wipping out all the current values
        for data in data_list:
            self.insert_at_end(data)

    # to find the lenght of the linked list
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    # remove an element at a given index

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next   # making next element the head
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next   # making the next element (agar condition satisfy ho jayegi to next element ki jagah uske next element ko mil jayegi)
                break

            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()

    # inserting at the beginning
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)
    
    # insering at the last
    ll.insert_at_end(55)
    ll.insert_at_end(44)
    ll.insert_at_end(33)

    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.remove_at(2)    # removing the element at index number 2
    ll.print()

    # printing the lenght of the linked list
    print("length", ll.get_length())

# print banana--->mango--->grapes--->orange--->
# banana--->mango--->orange--->
# length 3



# 6) insert a value at a perticular index 

class Node:
    def __init__(self, data = None, next = None):
        self.data = data       # data can contain integer, string and complex objects
        self.next = next       # pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None      # created variable head   # head of the linkedlist

    def insert_at_beginning(self, data):   #it takes data value , and inserting that value at the beginning of the linked list
        node = Node(data, self.head)     # new value inserted in the linkedlist become its new head
        self.head = node

    #defining print function
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        # if it is not None
        itr = self.head                                # itr -> iterator variable
        # for printing the linked list
        llstr = ""                    # linked list string
        
        while itr:
            llstr += str(itr.data) +  "--->"
            itr = itr.next

        print(llstr)

    #inserting at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)      # None = next
            return
        
        itr = self.head
        while itr.next:       # means linkedlist is not empty
            itr = itr.next    # i am at the last element

        itr.next = Node(data, None)


    # insert a list of values , and it will create a new fresh linked list
    def insert_value(self, data_list):
        self.head = None    # wipping out all the current values
        for data in data_list:
            self.insert_at_end(data)

    # to find the lenght of the linked list
    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    # remove an element at a given index

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next   # making next element the head
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next   # making the next element (agar condition satisfy ho jayegi to next element ki jagah uske next element ko mil jayegi)
                break

            itr = itr.next
            count += 1


    # insert a value at a perticular index

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count =0
        itr = self.head
        while itr:
            if count == index - 1:  # beacause when your are inserting the element in the linked list, you want to modify the next pointer of the previous element
                node = Node(data, itr.next)
                itr.next = node
                break


            itr = itr.next   # jaha bhi itr end hoga uske
            count += 1  

            

if __name__ == "__main__":
    ll = LinkedList()

    # inserting at the beginning
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(67)
    
    # insering at the last
    ll.insert_at_end(55)
    ll.insert_at_end(44)
    ll.insert_at_end(33)

    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print()

    ll.remove_at(2)   # removing the element at index number 2
    ll.print()

    ll.insert_at(0, "figs")   # inserting a element at a perticular index number 
    ll.print()

    ll.insert_at(2, "jackfruit")   # inserting a element at a perticular index number 
    ll.print()

    # printing the lenght of the linked list
    print("length", ll.get_length())

# print banana--->mango--->grapes--->orange--->
# banana--->mango--->orange--->
# figs--->banana--->mango--->orange--->
# figs--->banana--->jackfruit--->mango--->orange--->
# length 5



# Systematic and combine of all the above methods

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None          

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head         # itr = iteration
        llstr = ''              # llstr -> LinkedList string
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()


