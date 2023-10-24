# write a python programe with class name stack with method for 
# pushing and poping element from the stack also implement the interior 
# of the stack class that return the element in lifo order 
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty."

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty."

    def size(self):
        return len(self.items)

    def display_lifo_order(self):
        lifo_order = list(reversed(self.items))
        return lifo_order

# Create a stack and perform operations
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack Contents (LIFO Order):", stack.display_lifo_order())

popped_item = stack.pop()
print("Popped Item:", popped_item)

print("Stack Contents (LIFO Order):", stack.display_lifo_order())

stack.push(4)
print("Stack Contents (LIFO Order):", stack.display_lifo_order())

peeked_item = stack.peek()
print("Peeked Item:", peeked_item)

print("Stack Size:", stack.size())

# Empty the stack
while not stack.is_empty():
    popped_item = stack.pop()
    print("Popped Item:", popped_item)

print("Stack Contents (LIFO Order):", stack.display_lifo_order())
