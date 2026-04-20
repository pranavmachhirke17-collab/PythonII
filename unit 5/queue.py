from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

     
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to queue")      


    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
            return self.queue.popleft()
        else:
            return "Queue is empty"

    def display(self):
        return list(self.queue)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)   
print("Queue:", q.display())

print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())
print("Dequeued:", q.safe_dequeue())

print("Dequeued:", q.safe_dequeue())
