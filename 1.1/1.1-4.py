def main(A, B):
    carried = 0
    num = 0
    C = [0 for j in range(len(A)+1)]
    for i in reversed(range(len(A))):
        num = A[i]+B[i]+carried
        if num >= 2:
            C[i+1] = num-2
            carried = 1
        else:
            C[i+1] = num
            carried = 0
    C[0] = carried
    return C


# Пример ввода - 11101 <enter> 11001
first = list(map(int, str(input())))
second = list(map(int, str(input())))
print(main(first, second))
