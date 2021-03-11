def outer():
    val = 0
    val2 = 9

    def inner():
        outer.val = 5


    inner()
    return val


print(outer())
