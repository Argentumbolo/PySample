def func(arr, f, cond):
    if cond is True:
        return [f(2 * x) for x in arr]
    elif cond is False:
        return [f(x) for x in arr]
    elif cond is None:
        return [f(x) * 2 for x in arr]
    else:
        return [x for x in arr]
