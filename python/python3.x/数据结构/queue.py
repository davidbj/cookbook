class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.head is None:
            raise Exception('The queue is Null')
        node = self.head
        self.head = node.next
        return node.data

if __name__ == "__main__":
    queue = Queue()
    [queue.put(i) for i in range(10)]
    for _ in range(10):
        print(queue.pop())
