"""."""
from abc import abstractmethod
from tree_node import TreeNode


class Operator(TreeNode):
    """Custom operation wrapper."""

    def __init__(self, *args):
        """Store the given arguments somehow."""
        super().__init__(*args[0])
        self.__value = args[0]  # Usually tuple of 2 elements

    def apply(self):
        """Make use of the *args to compute the value of the given subtree. Recursion is your friend."""
        params = [x.apply() for x in self.__value]
        types = tuple(type(x) for x in params)
        if self.actions.get(types):
            return self.actions[types](*params)
        else:
            return self.default_operator(*[x.apply() for x in self.__value])

    @property
    def associativity(self):
        """
        Boolean whether the operation is associative or not.

        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        """
        return True
        #  Sulgude tegemiseks ülemine

    @property
    @abstractmethod
    def actions(self):
        """
        All custom implemented actions on different data structures.

        For example set - int does not exist, but we can implement it.
        :return a dictionary of functions where key is accepted parameters and value is a function which takes the
        aforementioned parameters as inputs and computes a value with them.
        """
        pass
