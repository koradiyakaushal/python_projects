arr = [15, 8, 9, 1, 12, 11]


def bubble_sort(l):
    for _ in range(len(l)):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]


bubble_sort(arr)
print(arr)