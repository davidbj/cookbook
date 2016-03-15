class Node:
    '''创建一个元素节点'''

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    '''实现栈的具体功能.
       首先定义一个栈顶,每次push的时候,将新元素节点定义为栈顶.pop的时候,将栈顶的元素pop出来,将栈顶更改为它的       next元素节点.
    '''

    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        try:
            self.top = node.next
            return node.data
        except AttributeError as e:
            print('The stack already is null.')


if __name__ == "__main__":
    stack = Stack()
    stack.push('I love Python')
    print(stack.pop())
    print(stack.pop())
