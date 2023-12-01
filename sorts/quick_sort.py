def quick_sort(arr: list):
    array_division(0, len(arr) - 1, arr)


def array_division(left: int, right: int, arr: list):
    support = len(arr[left + (right - left) // 2])
    l = left
    r = right
    while l <= r:
        flag = -1
        while l < right and len(arr[l]) <= support:
            if len(arr[l]) == support:
                flag = l
            l += 1
        if len(arr[l]) < support and flag != -1:
            l = flag
        flag = -1
        while left < r and len(arr[r]) >= support:
            if len(arr[r]) == support:
                flag = r
            r -= 1
        if len(arr[l]) > support and flag != -1:
            r = flag
        if l <= r:
            swap(l, r, arr)
            l += 1
            r -= 1
    if r > left:
        array_division(left, r, arr)
    if right > l:
        array_division(l, right, arr)


def swap(i: int, j: int, arr: list):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arr = input().split()
quick_sort(arr)
print(*arr)