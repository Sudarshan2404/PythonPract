class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

class CircularLL:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes"))
        for i in range(n):
            data = int(input(f"Enter Value for node {i+1} "))
            self.insert_end(data)
        print("Created a Circular Linked List")

    def insert_beg(self,data):
        new = Node(data)
        new.next = self.head
        self.head.next = new
        self.head = new

    def insert_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def delete(self,value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        if temp.data == value:           
            while temp.next != self.head:
                temp = temp.next
            if temp.next == self.head:
                self.head = None
                return
            
            temp.next = self.head.next
            self.head = self.head.next

        while temp.next != self.head:
            prev = temp
            temp = temp.next

            if temp.data == value:
                prev.next = temp.next   
                print(f"{value} deleted")
                return
        print("Value was not found")

    def search(self,value):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        pos = 1
        
        if temp.data == value:
          print(f"{value} found at {pos + 1}")
          return
        
        while True:
            temp = temp.next
            pos += 1
            if temp.data == value:
                break
            if temp.next == self.head:
                break

        if temp.data != value:
             print("Value not found")
             return

        print(f"{value} found at {pos}")

    def display(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -------> ")
            temp = temp.next
            if temp == self.head:
                break
        print("Back To Head")

l = CircularLL()
while True:
    print("Menu")
    print("1. Create a Linked List \n2. Insert at beginning \n3. Insert at end \n4. Delete from list \n5. Search \n6. Display \n7. Exit")
    n = int(input("Enter Choice:- "))
    if n == 1:
        l.create()
    elif n == 2:
        a = int(input("Enter Value to be Inserted"))
        l.insert_beg(a)
    elif n == 3:
        a = int(input("Enter Value to be Inserted at end"))
        l.insert_end(a)
    elif n == 4:
        a = int(input("Enter Value to be deleted"))
        l.delete(a)
    elif n == 5:
        a = int(input("Enter Value to be searched"))
        l.search(a)
    elif n == 6:
        l.display()
    elif n == 7:
        break
    else:
        print("Invalid Choice")
print("Exited the menu")