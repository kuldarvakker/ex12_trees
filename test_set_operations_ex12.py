"""."""

import pytest

from operators.leaf import Leaf
from operators.add import Add
from operators.mul import Mul
from operators.div import Div
from operators.sub import Sub
from operators.or_ import Or
from operators.pow import Pow
from operators.xor import Xor


@pytest.mark.timeout(1.0)
def test_subtract_subtracts_when_given_subtraction():
    """."""
    assert Sub(Sub(Leaf(5), Leaf(6)), Sub(Leaf(5), Leaf(6))).apply() == 0


@pytest.mark.timeout(1.0)
def test_xor_bitwise_xor_when_given_logical_xor():
    """."""
    assert Xor(Xor(Leaf(500), Leaf(5)), Xor(Leaf(20), Leaf(4))).apply() == 481


@pytest.mark.timeout(1.0)
def test_pow_raises_to_power_when_given_exponents():
    """."""
    assert Pow(Pow(Leaf(3), Leaf(2)), Pow(Leaf(2), Leaf(4))).apply() == 1853020188851841

@pytest.mark.timeout(1.0)
def test_set_leaf_apply_yields_set_when_given_a_set():
    """."""
    assert Leaf({6}).apply() == {6}


@pytest.mark.timeout(1.0)
def test_set_add_adds_when_given_leaves_with_sets():
    """."""
    assert Add(Leaf({5}), Leaf({6})).apply() == {5, 6}
    assert Add(Leaf({5}), Leaf(6)).apply() == {5, 6}


@pytest.mark.timeout(1.0)
def test_set_multiply_multiplies_when_given_leaves_with_sets__second_single_element():
    """."""
    assert Mul(Leaf({5, 6}), Leaf({3})).apply() == {frozenset({5, 3}), frozenset({6, 3})}


@pytest.mark.timeout(1.0)
def test_set_multiply_multiplies_when_given_leaves_with_sets__second_multiple_elements():
    """."""
    assert Mul(Leaf({5, 6}), Leaf({3, 4})).apply() == {frozenset({5, 3}), frozenset({6, 3}), frozenset({5, 4}),
                                                       frozenset({6, 4})}


@pytest.mark.timeout(1.0)
def test_set_div_divides_when_given_leaves_with_sets():
    """."""
    assert Div(Leaf({5, 6}), Leaf({6})).apply() == {5}


@pytest.mark.timeout(1.0)
def test_set_division_subtracts_when_given_subtraction_with_int():
    """."""
    assert Div(Sub(Leaf({5}), Leaf({7})), Div(Leaf(5), Leaf(6))).apply() == {5}


@pytest.mark.timeout(1.0)
def test_set_subtract_subtracts_when_given_subtraction_with_int():
    """."""
    assert Sub(Sub(Leaf({5}), Leaf({7})), Sub(Leaf(5), Leaf(6))).apply() == {5}


@pytest.mark.timeout(1.0)
def test_set_multiply_multiplies_when_given_leaves_with_sets__second_number():
    """."""
    assert Mul(Leaf({5, 6}), Leaf(4)).apply() == {frozenset({5, 4}), frozenset({6, 4})}
