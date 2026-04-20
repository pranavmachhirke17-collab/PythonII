class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"pushed {item} to stack")

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Cannot pop.")
            return None
        else:
            return self.stack.pop()
        
    def display(self):
        print("Stack:", self.stack)

s = stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())

print("popped:" , s.safe_pop())

