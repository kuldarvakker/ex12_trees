"""."""
from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    """The main node class."""

    def __init__(self, *args):
        """:param make use of *args and store them in a way that it is easy to use them."""
        self.__value = args  # Tuple of values
        pass

    @property
    @abstractmethod
    def default_operator(self):
        """abstract method which should be overridden to return the default_operator object."""
        #  return lambda *x: x
        pass

    @abstractmethod
    def apply(self):
        """abstract method which should be overridden to compute the value of the given abstract tree."""
        pass

    def class_str(self):
        """:return class string representation of the object."""
        return f"{self.__name__}({', '.join([x.class_str() for x in self.__value])})"

    def __eq__(self, other):
        """:return True when 2 object trees have the same shape and values."""
        params = [x for x in self.__value]
        types = tuple(type(x) for x in params)
        if types == other:
            return True
        return False

    def __ne__(self, other):
        """:return True when 2 object trees have a different shape and/or values."""
        params = [x for x in self.__value]
        types = (type(x) for x in params)
        if types != other:
            return True
        return False

    def __encase(self, node):
        """."""
        if node.priority < self.priority or node.priority == self.priority and node.associativity is True:
            return str(node)
        return str(f"({node})")

    def __str__(self):
        """."""
        return f" {self.default_operator} ".join([self.__encase(x) for x in self.__value])

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def associativity(self):
        """abstract method witch should be overridden to return a boolean whether the node is associative or not."""
        pass
