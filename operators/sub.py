"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Sub(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.__name__ = "Sub"

    @property
    def priority(self):
        """priority of the operation."""
        return 4

    @property
    def associativity(self):
        """."""
        return False

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x - y, "-")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, int): lambda x, y: x  # set without the element
        }
