# arithmetic-expression-evaluator
Expression Evaluator using Dijkstra's Two-Stack Algorithm

## USAGE
----

Call method Parser.parse(s: str).

Format of s: A valid arithmetic expression, with each operation (+, -, *, /) enclosed
by parentheses.

Example:
Python```
>>> s = "(1 + ((2 * (4/6)) + 3))"
>>> Parser().parse(s)
[out]: 5.3333
```