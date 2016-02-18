import operator

__author__ = 'dhruv'
# I'm changing the style!

operations = {"+": operator.add, "*": operator.mul, "-": operator.sub,
              "/": operator.truediv}


class Parser:
    """ Parser for Arithmetic Expressions, using Dijkstra's Two-Stack Algorithm
    """

    def __init__(self):
        self.operator_stack = []
        self.value_stack = []

    def parse(self, s: str):
        # Remove left-parentheses, spaces, and ensure the whole expression ends
        # with a right-parenthesis
        s = s.replace(" ", "").replace("(", "").replace(")", "@)@")
        for o in operations.keys():
            s = s.replace(o, "@" + o + "@")

        iterator = iter(s.split("@"))
        while True:
            try:
                value = next(iterator)
            except StopIteration:
                break

            if value in operations.keys():
                # If operator
                self.operator_stack.append(operations[value])

            elif value.isdigit():
                # Assume only integer values for now
                self.value_stack.append(float(value))

            elif value == ")":
                value1 = self.value_stack.pop()
                value2 = self.value_stack.pop()
                operation = self.operator_stack.pop()

                new_value = operation(value2, value1)
                self.value_stack.append(new_value)

        if not len(self.value_stack) == 1:
            raise(Exception("Invalid Expression"))
        else:
            return self.value_stack[0]