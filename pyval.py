

operators = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b),
    '**': (lambda a, b:  a ** b),
    '^': (lambda a, b: a ** b)
}

priorities = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '**': 3,
    '^': 3
}

op_chars = {char for op in operators for char in op}


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
                    self.right.result(), self.left.result())


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
    next_token = ""
    pos = 0

    while pos < len(exp):
        if _is_number(exp[pos]):
            next_token, pos = _read_next_value(exp, pos)
        elif exp[pos] in op_chars:
            next_token, pos = _read_next_operator(exp, pos)
        elif exp[pos] in ('(', ')'):
            next_token = exp[pos]
        else:
            raise ValueError("Unrecognized character at position " + str(pos))

        tokens.append(next_token)
        pos += 1
    
    return tokens


def _read_next_value(exp, pos):
    token = ""
    while pos < len(exp) and (_is_number(exp[pos]) or exp[pos] == '.'):
        token += exp[pos]
        pos += 1
    return token, pos - 1


def _read_next_operator(exp, pos):
    token = ""
    while (pos < len(exp) and exp[pos] in op_chars):
        token += exp[pos]
        pos += 1
    return token, pos - 1


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
