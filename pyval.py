

operators = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b)
}

priorities = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def evaluate(expression):
    infix = _parse_tokens(expression.replace(' ', ''))
    postfix = _postfix(infix)   
    stack = []

    for token in postfix:
        if _is_number(token):
            stack.append(ExpressionNode(token))
        if token in operators:
            t1, t2 = stack.pop(), stack.pop()
            node = ExpressionNode(token)
            node.left, node.right = t1, t2
            stack.append(node)

    return stack.pop().result()


class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def result(self):
        if _is_number(self.value):
            return _to_number(self.value)
        else:
            return operators[self.value](
                    self.left.result(), self.right.result())


def _postfix(tokens):
    stack = ['(']
    tokens.append(')')
    postfix = []

    for token in tokens:
        if _is_number(token):
            postfix.append(token)
        elif token == '(':
            stack.append('(')
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while _priority(token) <= _priority(stack[-1]):
                postfix.append(stack.pop())
            stack.append(token)

    return postfix


def _priority(token):
    if token in priorities:
        return priorities[token] 
    return 0
    

def _parse_tokens(exp):
    tokens = []
    last_num = ""

    for char in exp:
        if char in operators or char in ('(', ')'):
            if last_num:
                tokens.append(last_num)
                last_num = ""
            tokens.append(char)
        else:
            last_num += char

    if last_num:
        tokens.append(last_num)

    return tokens


def _to_number(str):
    try:
        return int(str)
    except ValueError:
        return float(str)


def _is_number(str):
    try:
        complex(str)
        return True
    except ValueError:
        return False
