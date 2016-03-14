#!/usr/bin/env python


class Node:
    '''创建一个新的元素节点.'''

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''实现一个链表数据结构.'''

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''向链表末尾新增元素.
           1. 如果链表为空,head和tail都指向该元素节点.
           2. 如果链表非空,将新元素节点添加到现在链表末尾元素后面，
              然后更改现在元素节点的末尾节点为新元素节点,将tail更
              改为新节点.
        '''
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        '''将链表生成一个迭代器.'''
        if self.head is None:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def insert(self, idx, data):
        '''在链表指定索引位置插入一个新的元素.
           1. 如果插入的索引位置大于链表总长度,则报错.
           2. 如果插入的索引位置等于0,则该元素为head节点.
           3. 如果插入的节点是末尾元素节点,则tail指向新元
              素节点.
        '''
        cur = self.head
        cur_idx = 0
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(data)
        if idx == 0:
            self.head = node
            node.next = cur
        else:
            node.next = cur.next
            cur.next = node
            if node.next is None:
                self.tail = node

    def remove(self, idx):
        '''向链表中删除一个元素节点.'''
        cur = self.head
        cur_idx = 0
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur

if __name__ == "__main__":
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    print([i for i in lst.iter()])
    lst.insert(0, 0)
    print([i for i in lst.iter()])
    lst.remove(1)
    print([i for i in lst.iter()])
