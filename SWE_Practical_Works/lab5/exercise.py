# Stack Class
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
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


# Queue Class
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


# Function to evaluate postfix expression
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.push(result)

    return stack.pop()


# Queue implementation using two stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")
        return self.stack2.pop()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def size(self):
        return self.stack1.size() + self.stack2.size()


# Task scheduler using queue
class TaskScheduler:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task):
        self.queue.enqueue(task)

    def process_tasks(self):
        while not self.queue.is_empty():
            task = self.queue.dequeue()
            print(f"Processing task: {task}")


# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = Stack()
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    for token in expression.split():
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':  # Left parenthesis
            stack.push(token)
        elif token == ')':  # Right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Discard '('
        else:  # Operator
            while (not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)

    # Pop any remaining operators in the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


# Testing all functionalities

# Test Postfix Evaluation
print("Postfix Evaluation:", evaluate_postfix("3 4 + 2 * 7 /"))  # Should evaluate to ((3 + 4) * 2) / 7

# Test Queue with Two Stacks
queue_with_stacks = QueueWithStacks()
queue_with_stacks.enqueue(1)
queue_with_stacks.enqueue(2)
queue_with_stacks.enqueue(3)
print("Dequeue from QueueWithStacks:", queue_with_stacks.dequeue())  # Should print 1

# Test Task Scheduler
scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
print("Task Scheduler:")
scheduler.process_tasks()  # Should process each task in the order they were added

# Test Infix to Postfix Conversion
print("Infix to Postfix:", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # Expected "3 4 2 * 1 5 - / +"
