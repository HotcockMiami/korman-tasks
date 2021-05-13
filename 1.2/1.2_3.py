lst = [4, 1, 6, 5, 30, 2, 10, 3, 1]
lst = sorted(lst)
i = 0
while i<len(lst)-1:
    if lst[i]==lst[i+1]:
        print('yes')
        exit()
    i+=1
print('no')