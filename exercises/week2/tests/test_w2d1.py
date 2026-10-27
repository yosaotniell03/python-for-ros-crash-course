import ast
import inspect

import pytest

from w2d1_lists import average, closest, count_below


@pytest.mark.parametrize(
    "readings, expected",
    [([2.0, 4.0], 3.0), ([1.5], 1.5), ([], 0.0), ([1.0, 2.0, 6.0], 3.0)],
)
def test_average(readings, expected):
    assert average(readings) == pytest.approx(expected)


@pytest.mark.parametrize(
    "readings, limit, expected",
    [([0.5, 2.0, 0.3, 5.0], 1.0, 2), ([], 1.0, 0), ([1.0, 1.0], 1.0, 0), ([0.2, 0.4], 1.0, 2)],
)
def test_count_below(readings, limit, expected):
    assert count_below(readings, limit) == expected


@pytest.mark.parametrize(
    "readings, expected",
    [([2.5, 0.8, 3.1], 0.8), ([250.0, 300.0], 250.0), ([3.0, 2.0, 1.0], 1.0), ([0.5, 0.9, 0.7], 0.5)],
)
def test_closest(readings, expected):
    tree = ast.parse(inspect.getsource(closest))
    has_loop = any(isinstance(node, (ast.For, ast.While)) for node in ast.walk(tree))
    uses_min = any(
        (isinstance(node, ast.Name) and node.id in ("min", "sorted"))
        or (isinstance(node, ast.Attribute) and node.attr == "sort")
        for node in ast.walk(tree)
    )
    assert has_loop and not uses_min, "closest must find the smallest value with a for or while loop, not with min(), sorted() or sort()"
    assert closest(readings) == expected
