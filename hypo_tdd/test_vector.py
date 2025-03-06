# Vector
# v.magnitude
# const * v
# v1 + v2

from hypothesis import given, strategies as st
import math


def sqrt(x: float) -> float:
    return math.sqrt(x)


@given(st.floats(min_value=0, allow_infinity=False, allow_nan=False))
def test_sqrt(x):
    result = sqrt(x)
    assert math.isclose(result * result, x, rel_tol=1e-6)


class Vector:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)


def test_vector_init():
    v = Vector((1,1))
    assert v.magnitude == math.sqrt(2)
