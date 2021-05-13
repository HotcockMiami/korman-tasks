def selection_sort(lst):
    for i in range(len(lst)):
        maxx_index = i
        for j in range(i+1, len(lst)):
            if lst[j]<lst[maxx_index]:
                maxx_index = j
        _ = lst[i]
        lst[i] = lst[maxx_index]
        lst[maxx_index] = _
    print(lst)


lst = [4, 3, 4, 5, 2, 9, 12, 1, 3]
selection_sort(lst)
