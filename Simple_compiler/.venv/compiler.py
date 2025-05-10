import re
from dataclasses import dataclass
from typing import List, Union

@dataclass
class Token:
    type: str
    value: str

class ASTNode:
    pass

@dataclass
class NumberNode(ASTNode):
    value: float

@dataclass
class BinOpNode(ASTNode):

    left: ASTNode
    op: str
    right: ASTNode

def lexer(code: str) -> List[Token]:

    tokens = []

    code = code.replace(" ", "")

    token_spec = [
                 ("NUMBER", r"\d+(\.\d+)?"),
                 ("OPERATOR", r"[+\-*/]"),
                 ]

    tok_regex = "|".join("(?P<%s>%s)" % pair for pair in token_spec)

    for mo in re.finditer(tok_regex, code):

        kind = mo.lastgroup
        value = mo.group()

        if kind == "NUMBER":
            tokens.append(Token("NUMBER", value))

        elif kind == "OPERATOR":
            tokens.append(Token("OPERATOR", value))

    return tokens

class Parser:

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def current_token(self) -> Union[Token, None]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, token_type: str) -> Token:
        token = self.current_token()

        if token and token.type == token_type:
            self.pos += 1
            return token
        raise ValueError(f"Expected {token_type}, got {token}")

    def factor(self) -> ASTNode:

        token = self.consume("NUMBER")
        return NumberNode(float(token.value))

    def term(self) -> ASTNode:

        node = self.factor()

        while (token := self.current_token()) and token.value in ("*", "/"):

            op = self.consume("OPERATOR").value
            right = self.factor()
            node = BinOpNode(node, op, right)

        return node

    def expr(self) -> ASTNode:

        node = self.term()

        while (token := self.current_token()) and token.value in ("+", "-"):

            op = self.consume("OPERATOR").value
            right = self.term()
            node = BinOpNode(node, op, right)

        return node

    def parse(self) -> ASTNode:

        return self.expr()

def generate_code(node: ASTNode) -> str:

    if isinstance(node, NumberNode):
        return str(node.value)

    elif isinstance(node, BinOpNode):

        left_code = generate_code(node.left)
        right_code = generate_code(node.right)

        return f"({left_code} {node.op} {right_code})"

def compile_expression(expression: str) -> tuple[str, float]:

    tokens = lexer(expression)

    parser = Parser(tokens)
    ast = parser.parse()

    python_code = generate_code(ast)

    result = eval(python_code)
    return python_code, result


def main():

    print("Simple Arithmetic Compiler")
    print("Enter arithmetic expressions (e.g., '2 + 3 * 4'). Type 'exit' to quit.")

    while True:

        try:

            expression = input("Enter expression: ").strip()
            if expression.lower() == "exit":
                print("Exiting...")
                break

            if not expression:
                print("Error: Empty input. Please enter a valid expression.")
                continue

            code, result = compile_expression(expression)

            print(f"Generated Code: {code}")
            print(f"Result: {result}\n")

        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()