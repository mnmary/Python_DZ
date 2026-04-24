class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, v):
        self.items.append(v)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

def check_pair(s):
    open_brackets = ['(','{','[']
    closed_brackets = [')','}',']']
    pairs = {')':'(','}':'{',']':'['}
    stack_open_brackets = Stack()
    for char in s:
        #print(char)
        if char in open_brackets:
            #print("open bracket")
            stack_open_brackets.push(char)
        elif char in closed_brackets:
            #print("pairs: "+ pairs[char])
            #print(f"peek: {stack_open_brackets.peek()}")
            if pairs[char] != stack_open_brackets.peek() or stack_open_brackets.is_empty():
                return "Несбалансировано"
            #print("is OK: pop "+ stack_open_brackets.peek())
            stack_open_brackets.pop()
    return "Сбалансировано"

import unittest

class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")
    def tearDown(self):
        print("method tearDown")
    def test_balance1(self):
        self.assertEqual(check_pair("(((([{}]))))"), "Сбалансировано")
    def test_balance2(self):
        self.assertEqual(check_pair("[([])((([[[]]])))]{()}"), 'Сбалансировано')
    def test_balance3(self):
        self.assertEqual(check_pair("{{[()]}}"), 'Сбалансировано')

    def test_balance4(self):
        self.assertEqual(check_pair("}{}"), 'Несбалансировано')
    def test_balance5(self):
        self.assertEqual(check_pair("{{[(])]}}"), 'Несбалансировано')
    def test_balance6(self):
        self.assertEqual(check_pair("[[{())}]"), 'Несбалансировано')

if __name__ == '__main__':
    unittest.main()
