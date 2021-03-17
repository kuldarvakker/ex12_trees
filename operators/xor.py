"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Xor(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.__name__ = "Xor"

    @property
    def priority(self):
        """priority of the operation."""
        return 9

    @property
    def associativity(self):
        """."""
        return True

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x ^ y, "^")

    @property
    def actions(self):
        """No additional actions needs to be defined here."""
        return {}
