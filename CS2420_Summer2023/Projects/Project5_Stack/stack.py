class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, item):
        stack = self.stack_list
        stack.insert(0, item)

    def pop(self):
        stack = self.stack_list
        if len(stack) == 0:
            raise IndexError("Cannot pop stack, stack is empty.")
        return stack.pop(0)

    def top(self):
        stack = self.stack_list
        if len(stack) == 0:
            raise IndexError("Cannot top stack, stack is empty.")
        return stack[0]

    def size(self):
        stack = self.stack_list
        return len(stack)

    def clear(self):
        self.stack_list = []
