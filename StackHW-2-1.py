class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])
    def top(self):
        if not self.is_empty():
            last = len(self.items)-1
            print(self.items[last])
        else:
            print("stack empty")
    def peek(self):
        if not self.is_empty():
        #last = len(self.items)-1
            print(self.items[-1])
        else:
            print("stack empty")
    def minElement(self):

# complete here
        if 'narf' in self.items:
            for x in range(len(self.items) - 1, 0, -1):
                last_element = self.items[x]
            
                    
        else:
            for x in range(len(self.items) - 1, -1, -1):
                last_element = self.items[x]
        
        return last_element
        

#ints = Stack()
#num = ['w', 'q', 'c', 'b', 'a', 'i']

#for i in num:
    #ints.push(i)
#print(ints.items)
#print(ints.minElement())

#ints.minElement()

