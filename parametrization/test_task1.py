import pytest
from task import triangle_sum

# def ids_a(val):
#     return "a=({0})".format(str(val))
#
# def ids_b(val):
#     return "b=({0})".format(str(val))
#
# def ids_c(val):
#     return "c=({0})".format(str(val))


@pytest.mark.parametrize("a, b, c, expect",[
    (2,2,2,True),
    (-1,-1,-1,False),
    (0,0,0,False),
    (1,1,5,False)
])
def test_triangle_sum(a,b,c,expect):
    assert triangle_sum(a,b,c) == expect
