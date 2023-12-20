import os
import lark

class Formula(lark.Transformer):
  def __init__(self, variables: dict, visit_tokens: bool = True) -> None:
    super().__init__(visit_tokens)
    self.variables = variables
  def add(self, tree):
    lhs, rhs = tree
    return lhs + rhs
  def sub(self, tree):
    lhs, rhs = tree
    return lhs - rhs
  def mul(self, tree):
    lhs, rhs = tree
    return lhs * rhs
  def div(self, tree):
    lhs, rhs = tree
    return lhs / rhs
  def pow(self, tree):
    lhs, rhs = tree
    return lhs ** rhs
  def factor(self, tree):
    return tree[0]
  def variable(self, tree):
    return self.variables[str(tree[0].value)]
  def number(self, tree):
    return float(tree[0].value)

def calculate(formula: str, variables: dict):
  file_path = os.path.dirname(__file__) + "/formula.lark"
  parser = lark.Lark(open(file_path, "r"), parser="lalr")
  tree = parser.parse(formula)
  return int(Formula(variables).transform(tree))
