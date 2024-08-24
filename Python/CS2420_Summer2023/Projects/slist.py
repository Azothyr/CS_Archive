class SList:
    class SListNode:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, value):
        new_node = self.SListNode(value)
        if self._head is None or value < self._head.value:
            new_node.next = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1

    def find(self, value):
        current = self._head
        while current:
            if current.value == value:
                return current.value
            current = current.next
        return None

    def remove(self, value):
        if self._head is None:
            return False
        if self._head.value == value:
            self._head = self._head.next
            self._size -= 1
            return True
        current = self._head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def remove_all(self, value):
        if self._head is None:
            return
        while self._head and self._head.value == value:
            self._head = self._head.next
            self._size -= 1
        current = self._head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
            else:
                current = current.next

    def __str__(self):
        if self._head is None:
            return "[]"
        current = self._head
        result = "["
        while current.next:
            result += str(current.value) + ", "
            current = current.next
        result += str(current.value) + "]"
        return result

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def __len__(self):
        return self._size
