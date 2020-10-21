l = [1, 2, 3, 4, 5]


def fun(start, n, l, new_list):
    if(len(new_list) == n):
        print(new_list)
        return

    if(start >= len(l)):
        return

    x = [*new_list, l[start]]

    fun(start+1, n, l, x)

    fun(start+1, n, l, new_list)


fun(0, 3, l, [])
