class stack:
    def __init__(self):
        self._items=[]
    def push(self,item):
        self.itemsappend()
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._items[-1]
    def is_empty(self):
        return len(self._items)==0
    def size(self):
        return len(self._items)

