from file import func

def test_func():
    assert func([1, 2, 3, 4, 5], (lambda x: x**2), True)  == [  4, 16, 36, 64, 100]
    assert func([1, 2, 3, 4, 5], (lambda x: x**2), None)  == [  2,  8, 18, 32,  50]
    assert func([1, 2, 3, 4, 5], (lambda x: x**2), False) == [  1,  4,  9, 16,  25]
    assert func([1, 2, 3, 4, 5], (lambda x: x**2),    "") == [  1,  2,  3,  4,   5]
    #------------------------------------------------------------------------------
    assert func([5, 4, 3, 2, 1], (lambda x: x**2), True)  == [100, 64, 36, 16,   4]
    assert func([5, 4, 3, 2, 1], (lambda x: x**2), None)  == [ 50, 32, 18,  8,   2]
    assert func([5, 4, 3, 2, 1], (lambda x: x**2), False) == [ 25, 16,  9,  4,   1]
    assert func([5, 4, 3, 2, 1], (lambda x: x**2),    "") == [  5,  4,  3,  2,   1]
    #------------------------------------------------------------------------------
    assert func([], (lambda x: x**2), True)  == []
    assert func([], (lambda x: x**2), None)  == []
    assert func([], (lambda x: x**2), False) == []
    assert func([], (lambda x: x**2),    "") == []
